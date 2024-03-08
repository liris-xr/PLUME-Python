import xml.etree.ElementTree as ET
from plume.record import LslSample, LslOpenStream, LslCloseStream, MarkerSample
from plume.export.xdf_writer import *
from datetime import datetime

def lsl_samples_to_xdf(output_buf, markers: list[MarkerSample], lsl_open_streams: list[LslOpenStream], lsl_close_streams: list[LslCloseStream], lsl_samples: list[LslSample], record_start_time: datetime):
    datetime_str = record_start_time.astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')
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

    for lsl_open_stream in lsl_open_streams:
        xml_header = ET.fromstring(lsl_open_stream.xml_header)
        stream_id = np.uint64(lsl_open_stream.stream_id) + 1 # reserve id = 1 for the marker stream
        channel_format = xml_header.find("channel_format").text
        stream_channel_format[stream_id] = channel_format
        stream_min_time[stream_id] = None
        stream_max_time[stream_id] = None
        stream_sample_count[stream_id] = 0
        write_stream_header(output_buf, lsl_open_stream.xml_header, stream_id)

    for lsl_sample in lsl_samples:
        stream_id = np.uint64(lsl_sample.stream_id) + 1
        channel_format = stream_channel_format[stream_id]
        t = lsl_sample.timestamp / 1_000_000_000.0 #convert time to seconds

        if stream_min_time[stream_id] is None or t < stream_min_time[stream_id]:
            stream_min_time[stream_id] = t
        if stream_max_time[stream_id] is None or t > stream_max_time[stream_id]:
            stream_max_time[stream_id] = t

        if stream_id not in stream_sample_count:
            stream_sample_count[stream_id] = 1
        else:
            stream_sample_count[stream_id] += 1

        val = lsl_sample.channel_values
        write_stream_sample(output_buf, val, t, channel_format, stream_id)

    for marker_sample in markers:
        channel_format = stream_channel_format[marker_stream_id]
        t = marker_sample.timestamp / 1_000_000_000.0 #convert time to seconds

        if stream_min_time[marker_stream_id] is None or t < stream_min_time[marker_stream_id]:
            stream_min_time[marker_stream_id] = t
        if stream_max_time[marker_stream_id] is None or t > stream_max_time[marker_stream_id]:
            stream_max_time[marker_stream_id] = t

        if marker_stream_id not in stream_sample_count:
            stream_sample_count[marker_stream_id] = 1
        else:
            stream_sample_count[marker_stream_id] += 1

        val = marker_sample.label
        write_stream_sample(output_buf, val, t, channel_format, marker_stream_id)

    for lsl_close_stream in lsl_close_streams:
        stream_id = np.uint64(lsl_close_stream.stream_id) + 1
        sample_count = stream_sample_count[stream_id]
        write_stream_footer(output_buf, stream_min_time[stream_id], stream_max_time[stream_id], sample_count, stream_id)

    # Write marker stream footer
    # stream_id = 1 is reserved for the marker stream
    write_stream_footer(output_buf, stream_min_time[marker_stream_id], stream_max_time[marker_stream_id], stream_sample_count[marker_stream_id], marker_stream_id)

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
    write_stream_header(output_buf, xml, marker_stream_id) # stream_id = 1 is reserved for the marker stream