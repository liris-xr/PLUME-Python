from plume_python.reader.sample_stream_reader import SampleStreamReader
from plume.sample.unity.frame_pb2 import Frame as FrameSample
from plume_python.proxy.unity.frame import Frame
from plume_python.decoder.frame.frame_decoder import decode_frame
from typing import Generator


class RecordDecoder:
    def __init__(self, filepath: str):
        self._frames_samples_reader = SampleStreamReader.open(filepath)
        self._markers_samples_reader = SampleStreamReader.open(filepath)
        self._signals_samples_reader = SampleStreamReader.open(filepath)
        self._inputs_samples_reader = SampleStreamReader.open(filepath)

        self._decoded_frame = Frame()

    def close(self):
        self._frames_samples_reader.close()
        self._markers_samples_reader.close()
        self._signals_samples_reader.close()
        self._inputs_samples_reader.close()

    @property
    def frames(self) -> Generator[Frame, None, None]:

        while True:
            frame_sample, time_ns = self._frames_samples_reader.parse_next(FrameSample)

            if frame_sample is None:
                return

            decode_frame(self._decoded_frame, frame_sample, time_ns)
            yield self._decoded_frame

    @property
    def markers(self):
        pass

    @property
    def signals(self):
        pass

    @property
    def inputs(self):
        pass
