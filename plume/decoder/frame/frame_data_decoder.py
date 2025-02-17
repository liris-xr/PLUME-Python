from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from google.protobuf.message import Message
from plume.proxy.unity.frame import Frame

TU = TypeVar("TU", bound=Message)


class FrameDataDecoder(ABC, Generic[TU]):
    @abstractmethod
    def decode(self, frame: Frame, data: TU) -> Frame:
        raise NotImplementedError
