import sys
from os import walk, path
from importlib.util import spec_from_file_location, module_from_spec
from google.protobuf import descriptor_pool as _descriptor_pool


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


sys.path.append(path.abspath(path.dirname(__file__)))
default_descriptor_pool = build_descriptor_pool(path.dirname(__file__))
