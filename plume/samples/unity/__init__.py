from glob import glob
from os.path import basename, dirname, join

from .xritk import *
from .ui import *

messages = [basename(f)[:-3] for f in glob(join(dirname(__file__), "*_pb2.py"))]
__all__ = messages