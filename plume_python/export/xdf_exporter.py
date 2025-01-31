from plume_python.export.xdf_writer import XDFWriter

from plume_python.decoder.record_reader import RecordReader
from plume_python.proxy.unity.input_action import InputAction, InputActionType

XDF_STREAM_XML_HEADER_TEMPLATE = """<?xml version="1.0"?>
<info>
    <source_id>{source_id}</source_id>
    <name>{name}</name>
    <type>{type}</type>
    <channel_count>{channel_count}</channel_count>
    <channel_format>{channel_format}</channel_format>
    <nominal_srate>{nominal_srate}</nominal_srate>
</info>
"""
def _create_stream_xml_header(
    source_id: str,
    name: str,
    type: str,
    channel_count: int,
    channel_format: str,
    nominal_srate: float,
) -> str:
    return XDF_STREAM_XML_HEADER_TEMPLATE.format(
        source_id=source_id,
        name=name,
        type=type,
        channel_count=channel_count,
        channel_format=channel_format,
        nominal_srate=nominal_srate,
    )

def export_xdf_from_record(
    input_filepath: str,
    output_filepath: str,
    include_markers: bool = True
):

    with RecordReader(input_filepath) as record_reader:
        with XDFWriter(output_filepath, record_reader.metadata.start_time) as xdf_writer:

            markers_stream_xml_header = _create_stream_xml_header(
                source_id="plume_xdf_exporter",
                name="Markers",
                type="Markers",
                channel_count=1,
                channel_format="string",
                nominal_srate=0.0,
            )
            markers_stream_id = xdf_writer.get_or_create_stream(markers_stream_xml_header)

            if include_markers:
                for marker in record_reader.markers:
                    xdf_writer.write_stream_sample(markers_stream_id, marker.label, marker.time_s)

            for signal in record_reader.signals:
                stream_id = xdf_writer.get_or_create_stream(signal.stream_info.raw_xml_header)
                xdf_writer.write_stream_sample(stream_id, signal.values, signal.time_s)


if __name__ == "__main__":
    export_xdf_from_record("tests/record.plm", "example.xdf")
