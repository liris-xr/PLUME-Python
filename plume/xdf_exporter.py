import xml.etree.ElementTree as ET
from samples.common.marker_pb2 import Marker 
from samples.lsl.stream_sample_pb2 import StreamSample
from samples.lsl.stream_open_pb2 import StreamOpen
from samples.lsl.stream_close_pb2 import StreamClose

from xdf_writer import *
from record import Record

def to_xdf(output_buf, record: Record):
    datetime_str = record.record_header.payload.created_at.ToDatetime().astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')
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

    for stream_open_sample in record.GetSamplesByDescriptor(StreamOpen.DESCRIPTOR):
        stream_info = stream_open_sample.payload.stream_info
        xml_header = ET.fromstring(stream_open_sample.payload.xml_header)
        stream_id = np.uint64(stream_info.lsl_stream_id) + 1 # reserve id = 1 for the marker stream
        channel_format = xml_header.find("channel_format").text
        stream_channel_format[stream_id] = channel_format
        stream_min_time[stream_id] = None
        stream_max_time[stream_id] = None
        stream_sample_count[stream_id] = 0
        write_stream_header(output_buf, stream_open_sample.payload.xml_header, stream_id)

    for stream_sample in record.GetSamplesByDescriptor(StreamSample.DESCRIPTOR):
        stream_info = stream_sample.payload.stream_info
        stream_id = np.uint64(stream_info.lsl_stream_id) + 1
        channel_format = stream_channel_format[stream_id]
        attr = stream_sample.payload.WhichOneof('values')
        t = stream_sample.header.time / 1_000_000_000.0 #convert time to seconds

        if stream_min_time[stream_id] is None or t < stream_min_time[stream_id]:
            stream_min_time[stream_id] = t
        if stream_max_time[stream_id] is None or t > stream_max_time[stream_id]:
            stream_max_time[stream_id] = t

        if stream_id not in stream_sample_count:
            stream_sample_count[stream_id] = 1
        else:
            stream_sample_count[stream_id] += 1

        val = getattr(stream_sample.payload, attr).value
        write_stream_sample(output_buf, val, t, channel_format, stream_id)

    for marker_sample in record.GetSamplesByDescriptor(Marker.DESCRIPTOR):
        channel_format = stream_channel_format[marker_stream_id]
        t = marker_sample.header.time / 1_000_000_000.0 #convert time to seconds

        if stream_min_time[marker_stream_id] is None or t < stream_min_time[marker_stream_id]:
            stream_min_time[marker_stream_id] = t
        if stream_max_time[marker_stream_id] is None or t > stream_max_time[marker_stream_id]:
            stream_max_time[marker_stream_id] = t

        if marker_stream_id not in stream_sample_count:
            stream_sample_count[marker_stream_id] = 1
        else:
            stream_sample_count[marker_stream_id] += 1

        val = marker_sample.payload.label
        write_stream_sample(output_buf, val, t, channel_format, marker_stream_id)

    for stream_close_sample in record.GetSamplesByDescriptor(StreamClose.DESCRIPTOR):
        stream_info = stream_close_sample.payload.stream_info
        stream_id = np.uint64(stream_info.lsl_stream_id) + 1
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