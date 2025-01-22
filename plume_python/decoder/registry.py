from __future__ import annotations

from typing import TypeVar, Dict, Type, Callable
from google.protobuf.message import Message
from google.protobuf.descriptor import Descriptor

from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder

T = TypeVar("T", bound=Message)
_frame_data_decoder_registry: Dict[Type[T], FrameDataDecoder[T]] = {}

def register_frame_data_decoder(type: Type[T]) -> Callable[[Type[FrameDataDecoder[T]]], Type[FrameDataDecoder[T]]]:
    def decorator(cls: Type[FrameDataDecoder[T]]) -> Type[FrameDataDecoder[T]]:
        _frame_data_decoder_registry[type] = cls()
        return cls
    return decorator

def get_frame_data_decoder(type: Type[T]):
    cls = _frame_data_decoder_registry.get(type)
    if cls is None:
        raise ValueError(f"No decoder found for {type}")
    return cls