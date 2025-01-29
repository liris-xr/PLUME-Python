from __future__ import annotations

import importlib.util
from typing import TypeVar, Dict, Type, Callable
from google.protobuf.message import Message
from pathlib import Path
from glob import glob
import importlib
import pkgutil

from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder

T = TypeVar("T", bound=Message)
_frame_data_decoder_registry: Dict[Type[T], FrameDataDecoder[T]] = {}


def register_frame_data_decoder(
    type: Type[T],
) -> Callable[[Type[FrameDataDecoder[T]]], Type[FrameDataDecoder[T]]]:
    def decorator(cls: Type[FrameDataDecoder[T]]) -> Type[FrameDataDecoder[T]]:
        _frame_data_decoder_registry[type] = cls()
        return cls

    return decorator


def get_frame_data_decoder(type: Type[T]):
    cls = _frame_data_decoder_registry.get(type)
    if cls is None:
        raise ValueError(f"No decoder found for {type}")
    return cls


def _register_all_frame_data_decoders():

    path = Path(__file__).parent

    modules_path = [
        p for p in glob(f"{path}/**/*.py", recursive=True) if p != str(Path(__file__))
    ]

    for module_path in modules_path:
        module_name = Path(module_path).stem
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)


_register_all_frame_data_decoders()
