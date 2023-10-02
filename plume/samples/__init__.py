import sys
import pkgutil
import importlib
from glob import glob
from os.path import abspath, basename, dirname, isfile, isdir, join

# protoc doesn't allow for generating *_pb2.py in a custom package. Thus we use this hacky trick to fix imports
sys.path.insert(0, abspath(dirname(__file__)))

from .unity import *
from .lsl import *
from .common import *

messages = [basename(f)[:-3] for f in glob(join(dirname(__file__), "*_pb2.py"))]
__all__ = messages
