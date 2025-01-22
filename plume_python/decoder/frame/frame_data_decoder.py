from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from google.protobuf.message import Message
from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.gameobject import GameObject

T = TypeVar("T", bound=Message)

class FrameDataDecoder(ABC, Generic[T]):

    @abstractmethod
    def decode(self, frame: Frame, data: T):
        raise NotImplementedError

    def get_or_create_gameobject(self, frame: Frame, uuid: str) -> GameObject:
        if uuid in frame._gameobjects.keys():
            return frame._gameobjects[uuid]
        else:
            gameobject = GameObject(uuid=uuid)
            frame._gameobjects[uuid] = gameobject
            return gameobject
        
    def create_component(self, frame: Frame, component: Component):
        if component.uuid in frame._components.keys():
            return
        frame._components[component.uuid] = component