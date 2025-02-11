from plume.sample.common.marker_pb2 import Marker as MarkerSample
from plume.decoder.sample_stream_reader import SampleStreamReader
from plume.proxy.common.marker import Marker

from typing import Iterator

class MarkerDecoder(Iterator[Marker]):

    _stream_reader: SampleStreamReader

    def __init__(self, filepath: str):
        self._stream_reader = SampleStreamReader.open(filepath)

    def close(self):
        self._stream_reader.close()

    def __next__(self) -> Marker:
        marker_sample, time_ns = self._stream_reader.parse_next(MarkerSample)

        if marker_sample is None:
            raise StopIteration

        return Marker(label=marker_sample.label, time_ns=time_ns)
    