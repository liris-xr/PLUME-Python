from __future__ import annotations
from plume_python.proxy.unity.scene import SceneCollection
from typing import Optional


class Frame:
    _time_ns: int
    _frame_number: int
    _scenes: SceneCollection

    def __init__(
        self,
        time_ns: int = 0,
        frame_number: int = 0,
        scenes: Optional[SceneCollection] = None,
    ):
        self._time_ns = time_ns
        self._frame_number = frame_number
        self._scenes = scenes if scenes else SceneCollection()

    def deepcopy(self) -> Frame:
        copy = Frame(
            time_ns=self._time_ns,
            frame_number=self._frame_number,
            scenes=self._scenes.deepcopy(),
        )
        return copy

    @property
    def frame_number(self) -> int:
        return self._frame_number

    @property
    def frame_number(self) -> int:
        return self._frame_number

    @property
    def scenes(self) -> SceneCollection:
        return self._scenes

    @property
    def time_ns(self) -> int:
        return self._time_ns

    @property
    def time_s(self) -> float:
        return self._time_ns / 1e9
