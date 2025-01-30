from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.common.marker import Marker
from plume_python.proxy.lsl.stream import LslStreamSample
from plume_python.proxy.unity.input_action import InputAction

from plume_python.decoder.frame.frame_decoder import FrameDecoder
from plume_python.decoder.marker_decoder import MarkerDecoder
from plume_python.decoder.lsl_stream_decoder import LslStreamDecoder
from plume_python.decoder.input_action_decoder import InputActionDecoder

from typing import Iterator


class RecordDecoder:
    def __init__(self, filepath: str):
        self._frame_decoder = FrameDecoder(filepath)
        self._marker_decoder = MarkerDecoder(filepath)
        self._signal_decoder = LslStreamDecoder(filepath)
        self._input_action_decoder = InputActionDecoder(filepath)

    def close(self):
        self._frame_decoder.close()
        self._marker_decoder.close()
        self._signal_decoder.close()
        self._input_action_decoder.close()

    @property
    def frames(self) -> Iterator[Frame]:
        return self._frame_decoder

    @property
    def markers(self) -> Iterator[Marker]:
        return self._marker_decoder

    @property
    def signals(self) -> Iterator[LslStreamSample]:
        return self._signal_decoder

    @property
    def input_actions(self) -> Iterator[InputAction]:
        return self._input_action_decoder
