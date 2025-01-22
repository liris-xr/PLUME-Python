from plume_python.decoder.sample_stream_reader import SampleStreamReader
from plume.sample.unity.frame_pb2 import Frame as FrameSample
from plume_python.decoder.sample import Sample
from plume_python.decoder.frame.frame_decoder import decode_frame
from plume_python.proxy.unity.frame import Frame
from typing import Generator, Optional

class RecordDecoder:
    def __init__(self, filepath: str):
        self.frames_samples_reader = SampleStreamReader.open(filepath)
        self.markers_samples_reader = SampleStreamReader.open(filepath)
        self.signals_samples_reader = SampleStreamReader.open(filepath)
        self.inputs_samples_reader = SampleStreamReader.open(filepath)

        self.last_decoded_frame: Optional[Frame] = None

    def close(self):
        self.frames_samples_reader.close()
        self.markers_samples_reader.close()
        self.signals_samples_reader.close()
        self.inputs_samples_reader.close()

    @property
    def frames(self) -> Generator[Frame, None, None]:

        frame_sample: Sample[FrameSample]
        frame_sample = self.frames_samples_reader.parse(FrameSample)
        
        if frame_sample is None:
            return

        if self.last_decoded_frame is None:
            frame = Frame(frame_number=frame_sample.payload.frame_number, time_ns=frame_sample.time_ns)
        else:
            frame = self.last_decoded_frame.shallow_copy()

        decode_frame(frame, frame_sample.payload)

        self.last_decoded_frame = frame
        yield frame

    @property
    def markers(self):
        pass

    @property
    def signals(self):
        pass

    @property
    def inputs(self):
        pass