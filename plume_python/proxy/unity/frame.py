from __future__ import annotations
from typing import List, Dict
from plume_python.proxy.unity.scene import Scene
from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.gameobject import GameObject

from dataclasses import dataclass

@dataclass(frozen=True)
class Frame:
    frame_number: int
    time_ns: int

    scenes: Dict[str, Scene] = {}
    gameobjects: Dict[str, GameObject] = {}
    components: Dict[str, Component] = {}

    def __init__(self, frame_number: int, time_ns: int):
        self._frame_number = frame_number
        self._time_ns = time_ns
        self._scenes = {}
        self._gameobjects = {}
        self._components = {}

    def shallow_copy(self) -> Frame:
        frame_copy = Frame(self._frame_number, self._time_ns)
        frame_copy._scenes = self._scenes.copy()
        frame_copy._gameobjects = self._gameobjects.copy()
        frame_copy._components = self._components.copy()
        return frame_copy

    @property
    def time_s(self) -> float:
        return self._time_ns / 1e9
    
    @property
    def frame_number(self) -> int:
        return self._frame_number
    
    @property
    def scenes(self) -> List[Scene]:
        return self._scenes.copy()
