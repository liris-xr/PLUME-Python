from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AntialiasingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ANTIALIASING_MODE_NONE: _ClassVar[AntialiasingMode]
    ANTIALIASING_MODE_FAST_APPROXIMATE_ANTIALIASING: _ClassVar[AntialiasingMode]
    ANTIALIASING_MODE_SUBPIXEL_MORPHOLOGICAL_ANTI_ALIASING: _ClassVar[AntialiasingMode]

class AntialiasingQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ANTIALIASING_QUALITY_LOW: _ClassVar[AntialiasingQuality]
    ANTIALIASING_QUALITY_MEDIUM: _ClassVar[AntialiasingQuality]
    ANTIALIASING_QUALITY_HIGH: _ClassVar[AntialiasingQuality]
ANTIALIASING_MODE_NONE: AntialiasingMode
ANTIALIASING_MODE_FAST_APPROXIMATE_ANTIALIASING: AntialiasingMode
ANTIALIASING_MODE_SUBPIXEL_MORPHOLOGICAL_ANTI_ALIASING: AntialiasingMode
ANTIALIASING_QUALITY_LOW: AntialiasingQuality
ANTIALIASING_QUALITY_MEDIUM: AntialiasingQuality
ANTIALIASING_QUALITY_HIGH: AntialiasingQuality
