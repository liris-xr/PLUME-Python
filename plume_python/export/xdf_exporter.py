from plume_python.export.xdf_writer import *
from plume_python.record import Record
from plume_python.samples.common import marker_pb2
from plume_python.samples.lsl import lsl_stream_pb2


def export_xdf_from_record(output_buf, record: Record):
    datetime_str = record.get_metadata().start_time.ToDatetime().astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')
    # Add a colon separator to the offset segment
    datetime_str = "{0}:{1}".format(datetime_str[:-2], datetime_str[-2:])

    stream_channel_format = {}
    stream_min_time = {}
    stream_max_time = {}
    stream_sample_count = {}

    write_file_header(output_buf, "1.0", datetime_str)

    marker_stream_id = np.uint64(1)
    write_marker_stream_header(output_buf, marker_stream_id)
    stream_channel_format[marker_stream_id] = "string"
    stream_min_time[marker_stream_id] = None
    stream_max_time[marker_stream_id] = None
    stream_sample_count[marker_stream_id] = 0

    for lsl_open_stream in record[lsl_stream_pb2.StreamOpen]:
        xml_header = ET.fromstring(lsl_open_stream.payload.xml_header)
        stream_id = np.uint64(lsl_open_stream.payload.stream_id) + 1  # reserve id = 1 for the marker stream
        channel_format = xml_header.find("channel_format").text
        stream_channel_format[stream_id] = channel_format
        stream_min_time[stream_id] = None
        stream_max_time[stream_id] = None
        stream_sample_count[stream_id] = 0
        write_stream_header(output_buf, lsl_open_stream.payload.xml_header, stream_id)

    for lsl_sample in record[lsl_stream_pb2.StreamSample]:
        stream_id = np.uint64(lsl_sample.payload.stream_id) + 1
        channel_format = stream_channel_format[stream_id]
        t = lsl_sample.timestamp / 1_000_000_000.0  # convert time to seconds

        if stream_min_time[stream_id] is None or t < stream_min_time[stream_id]:
            stream_min_time[stream_id] = t
        if stream_max_time[stream_id] is None or t > stream_max_time[stream_id]:
            stream_max_time[stream_id] = t

        if stream_id not in stream_sample_count:
            stream_sample_count[stream_id] = 1
        else:
            stream_sample_count[stream_id] += 1

        if channel_format == "string":
            val = np.array([x for x in lsl_sample.payload.string_values.value], dtype=np.str_)
        elif channel_format == "int8":
            val = np.array([x for x in lsl_sample.payload.int8_values.value], dtype=np.int8)
        elif channel_format == "int16":
            val = np.array([x for x in lsl_sample.payload.int16_values.value], dtype=np.int16)
        elif channel_format == "int32":
            val = np.array([x for x in lsl_sample.payload.int32_values.value], dtype=np.int32)
        elif channel_format == "int64":
            val = np.array([x for x in lsl_sample.payload.int64_values.value], dtype=np.int64)
        elif channel_format == "float32":
            val = np.array([x for x in lsl_sample.payload.float_values.value], dtype=np.float32)
        elif channel_format == "double64":
            val = np.array([x for x in lsl_sample.payload.double_values.value], dtype=np.float64)
        else:
            raise ValueError(f"Unsupported channel format: {channel_format}")

        write_stream_sample(output_buf, val, t, channel_format, stream_id)

    for marker_sample in record[marker_pb2.Marker]:
        t = marker_sample.timestamp / 1_000_000_000.0  # convert time to seconds

        if stream_min_time[marker_stream_id] is None or t < stream_min_time[marker_stream_id]:
            stream_min_time[marker_stream_id] = t
        if stream_max_time[marker_stream_id] is None or t > stream_max_time[marker_stream_id]:
            stream_max_time[marker_stream_id] = t

        if marker_stream_id not in stream_sample_count:
            stream_sample_count[marker_stream_id] = 1
        else:
            stream_sample_count[marker_stream_id] += 1

        val = np.array([marker_sample.payload.label], dtype=np.str_)
        write_stream_sample(output_buf, val, t, "string", marker_stream_id)

    for lsl_close_stream in record[lsl_stream_pb2.StreamClose]:
        stream_id = np.uint64(lsl_close_stream.payload.stream_id) + 1
        sample_count = stream_sample_count[stream_id]
        write_stream_footer(output_buf, stream_min_time[stream_id], stream_max_time[stream_id], sample_count, stream_id)

    # Write marker stream footer
    # stream_id = 1 is reserved for the marker stream
    write_stream_footer(output_buf, stream_min_time[marker_stream_id], stream_max_time[marker_stream_id],
                        stream_sample_count[marker_stream_id], marker_stream_id)


def write_marker_stream_header(output_buf, marker_stream_id):
    info_el = ET.Element("info")
    name_el = ET.SubElement(info_el, "name")
    type_el = ET.SubElement(info_el, "type")
    channel_format_el = ET.SubElement(info_el, "channel_format")
    channel_count_el = ET.SubElement(info_el, "channel_count")
    nominal_srate_el = ET.SubElement(info_el, "nominal_srate")
    name_el.text = "Markers"
    type_el.text = "Marker"
    channel_format_el.text = "string"
    channel_count_el.text = "1"
    nominal_srate_el.text = "0.0"
    xml = ET.tostring(info_el, encoding=STR_ENCODING, xml_declaration=True)
    write_stream_header(output_buf, xml, marker_stream_id)  # stream_id = 1 is reserved for the marker stream
