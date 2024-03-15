import sys
from importlib.util import spec_from_file_location, module_from_spec
from os import walk, path
from typing import Type, TypeVar

from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf.message_factory import GetMessageClass
from google.protobuf.message import Message

T = TypeVar('T', bound=Message)


def build_descriptor_pool(root_folder):
    """
    Import all generated *_pb2.py modules dynamically.
    """
    for root, dirs, files in walk(root_folder):
        for file in files:
            if file.endswith("_pb2.py"):
                # Dynamically import the module
                module_name = file[:-6]  # Remove "_pb2.py" from the file name
                spec = spec_from_file_location(module_name, path.join(root, file))
                module = module_from_spec(spec)
                spec.loader.exec_module(module)
    return _descriptor_pool.Default()


def sample_types_from_names(names: list[str]) -> set[Type[T]]:
    types: set[Type[T]] = set()

    for name in names:
        descriptor = None

        derivatives = [name,
                       f"plume.{name}",
                       f"plume.sample.{name}",
                       f"plume.sample.{name}",
                       f"plume.sample.lsl.{name}",
                       f"plume.sample.unity.{name}",
                       f"plume.sample.unity.settings.{name}",
                       f"plume.sample.unity.urp.{name}",
                       f"plume.sample.unity.xritk.{name}",
                       f"plume.sample.unity.ui.{name}",
                       f"plume.sample.common.{name}"]

        for derivative in derivatives:
            try:
                descriptor = default_descriptor_pool.FindMessageTypeByName(derivative)
                if descriptor is not None:
                    types.add(GetMessageClass(descriptor))
                    break
            except KeyError:
                pass

        if descriptor is None:
            raise Exception(f"Sample type not found for '{name}'.")

    return types


sys.path.append(path.abspath(path.dirname(__file__)))
default_descriptor_pool = build_descriptor_pool(path.dirname(__file__))
