import importlib.util
from importlib.util import spec_from_file_location
from typing import Type, TypeVar

import importlib

import plume.sample
from google.protobuf.message import Message

from google.protobuf import symbol_database

import os
import glob

T = TypeVar("T", bound=Message)
_db = symbol_database.Default()


def _register_pb2_modules_from_module(module):
    """
    Import all generated *_pb2.py modules dynamically.
    """
    if hasattr(module, "__path__"):
        package_path = module.__path__[0]
    else:
        package_path = module.__file__

    pb2_files = glob.glob(os.path.join(package_path, "**/*_pb2.py"), recursive=True)

    for pb2_file in pb2_files:
        try:
            module_name = pb2_file.split("/")[-1].replace(".py", "")
            spec = spec_from_file_location(module_name, pb2_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except ImportError as e:
            print(f"Warning: Could not import {pb2_file}: {e}")


def get_descriptor_from_type_name(type_name: str):
    try:
        return _db.GetSymbol(type_name).DESCRIPTOR
    except KeyError:
        return None


def get_message_class_from_type_name(type_name: str) -> Type[T]:
    try:
        return _db.GetSymbol(type_name)
    except KeyError:
        return None


_register_pb2_modules_from_module(plume.sample)
