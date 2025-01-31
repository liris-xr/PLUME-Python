from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.common.marker import Marker
from plume_python.proxy.lsl.stream import LslStreamSample
from plume_python.proxy.unity.input_action import InputAction

from plume_python.decoder.frame.frame_decoder import FrameDecoder
from plume_python.decoder.marker_decoder import MarkerDecoder
from plume_python.decoder.lsl_stream_decoder import LslStreamDecoder
from plume_python.decoder.input_action_decoder import InputActionDecoder

from typing import Generator


class RecordDecoder:
    
    def __init__(self, filepath: str):
        self.filepath = filepath

    @property
    def frames(self) -> Generator[Frame, None, None]:
        frame_decoder = FrameDecoder(self.filepath)
        try:
            for frame in frame_decoder:
                yield frame
        finally:
            frame_decoder.close()

    @property
    def markers(self) -> Generator[Frame, None, None]:
        marker_decoder = MarkerDecoder(self.filepath)
        try:
            for marker in marker_decoder:
                yield marker
        finally:
            marker_decoder.close()

    @property
    def signals(self) -> Generator[LslStreamSample, None, None]:
        signal_decoder = LslStreamDecoder(self.filepath)
        try:
            for signal in signal_decoder:
                yield signal
        finally:
            signal_decoder.close()

    @property
    def input_actions(self) -> Generator[InputAction, None, None]:
        input_action_decoder = InputActionDecoder(self.filepath)
        try:
            for input_action in input_action_decoder:
                yield input_action
        finally:
            input_action_decoder.close()
