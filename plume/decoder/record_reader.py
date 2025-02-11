from plume.proxy.unity.frame import Frame
from plume.proxy.lsl.stream import LslStreamSample
from plume.proxy.unity.input_action import InputAction
from plume.proxy.record_metadata import RecordMetadata
from plume.proxy.common.marker import Marker

from plume.decoder.frame.frame_decoder import FrameDecoder
from plume.decoder.marker_decoder import MarkerDecoder
from plume.decoder.lsl_stream_decoder import LslStreamDecoder
from plume.decoder.input_action_decoder import InputActionDecoder
from plume.decoder.record_metadata_decoder import decode_record_metadata

from typing import Generator
from functools import cached_property


class RecordReader:

    def __init__(self, filepath: str):
        self.filepath = filepath

        self._decoders = []

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        for decoder in self._decoders:
            decoder.close()

    @cached_property
    def metadata(self) -> RecordMetadata:
        return decode_record_metadata(self.filepath)

    @property
    def frames(self) -> Generator[Frame, None, None]:
        frame_decoder = FrameDecoder(self.filepath)
        self._decoders.append(frame_decoder)
        try:
            for frame in frame_decoder:
                yield frame
        finally:
            frame_decoder.close()
            self._decoders.remove(frame_decoder)

    @property
    def markers(self) -> Generator[Marker, None, None]:
        marker_decoder = MarkerDecoder(self.filepath)
        self._decoders.append(marker_decoder)
        try:
            for marker in marker_decoder:
                yield marker
        finally:
            marker_decoder.close()
            self._decoders.remove(marker_decoder)

    @property
    def signals(self) -> Generator[LslStreamSample, None, None]:
        signal_decoder = LslStreamDecoder(self.filepath)
        self._decoders.append(signal_decoder)
        try:
            for signal in signal_decoder:
                yield signal
        finally:
            signal_decoder.close()
            self._decoders.remove(signal_decoder)

    @property
    def input_actions(self) -> Generator[InputAction, None, None]:
        input_action_decoder = InputActionDecoder(self.filepath)
        self._decoders.append(input_action_decoder)
        try:
            for input_action in input_action_decoder:
                yield input_action
        finally:
            input_action_decoder.close()
            self._decoders.remove(input_action_decoder)
