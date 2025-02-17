from plume.sample.lsl.lsl_stream_pb2 import StreamOpen, StreamClose, StreamSample
from plume.decoder.sample_stream_reader import SampleStreamReader
from plume.proxy.lsl.stream import LslStreamSample, LslStreamInfo, StreamChannelFormat

from typing import Dict, Iterator
import xml.etree.ElementTree as ET

from uuid import UUID

from warnings import warn

class LslStreamDecoder(Iterator[LslStreamSample]):

    _stream_reader: SampleStreamReader

    def __init__(self, filepath: str):
        self._stream_reader = SampleStreamReader.open(filepath)
        self._streams_info: Dict[str, LslStreamInfo] = {}

    def close(self):
        self._stream_reader.close()

    def __next__(self) -> LslStreamSample:

        while True:
            signal_sample, time_ns = self._stream_reader.parse_next([StreamOpen, StreamSample])

            if signal_sample is None:
                raise StopIteration

            if isinstance(signal_sample, StreamOpen):
                if signal_sample.stream_id not in self._streams_info:
                    self._streams_info[signal_sample.stream_id] = self._decode_stream_open(signal_sample)
            elif isinstance(signal_sample, StreamSample):
                if signal_sample.stream_id not in self._streams_info:
                    warn(f"Stream {signal_sample.stream_id} not found in stream open")
                    stream_info = None
                else:
                    stream_info = self._streams_info[signal_sample.stream_id]
                
                values_field = signal_sample.WhichOneof("values")
                values = getattr(signal_sample, values_field).value

                return LslStreamSample(
                    stream_info=stream_info,
                    time_ns=time_ns,
                    values=values
                )

    def _decode_stream_open(self, stream_open: StreamOpen) -> LslStreamInfo:
        
        root = ET.fromstring(stream_open.xml_header)

        name_str = root.findtext("name")
        type_str = root.findtext("type")
        channel_count_str = root.findtext("channel_count")
        channel_format_str = root.findtext("channel_format")
        source_id_str = root.findtext("source_id")
        nominal_sample_rate_str = root.findtext("nominal_srate")
        version_str = root.findtext("version")
        created_at_str = root.findtext("created_at")
        uid_str = root.findtext("uid")
        hostname_str = root.findtext("hostname")
        v4address_str = root.findtext("v4address")
        v4data_port_str = root.findtext("v4data_port")
        v4service_port_str = root.findtext("v4service_port")
        v6address_str = root.findtext("v6address")
        v6data_port_str = root.findtext("v6data_port")
        v6service_port_str = root.findtext("v6service_port")
        desc_str = root.findtext("desc")
        
        stream_info = LslStreamInfo(
            name=name_str,
            type=type_str,
            channel_count=int(channel_count_str) if channel_count_str else None,
            nominal_sample_rate=float(nominal_sample_rate_str) if nominal_sample_rate_str else None,
            channel_format=StreamChannelFormat.from_string(channel_format_str) if channel_format_str else None,
            source_id=source_id_str,
            created_at=float(created_at_str) if created_at_str else None,
            uid=UUID(uid_str) if uid_str else None,
            version=version_str,
            hostname=hostname_str,
            v4address=v4address_str,
            v4data_port=v4data_port_str,
            v4service_port=v4service_port_str,
            v6address=v6address_str,
            v6data_port=v6data_port_str,
            v6service_port=v6service_port_str,
            desc=desc_str,
            raw_xml_header=stream_open.xml_header
        )

        return stream_info
    