from unity import identifiers_pb2 as _identifiers_pb2
from common import vector2_pb2 as _vector2_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScaleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SCALE_MODE_CONSTANT_PIXEL_SIZE: _ClassVar[ScaleMode]
    SCALE_MODE_SCALE_WITH_SCREEN_SIZE: _ClassVar[ScaleMode]
    SCALE_MODE_CONSTANT_PHYSICAL_SIZE: _ClassVar[ScaleMode]

class ScreenMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SCREEN_MATCH_MODE_MATCH_WIDTH_OR_HEIGHT: _ClassVar[ScreenMatchMode]
    SCREEN_MATCH_MODE_EXPAND: _ClassVar[ScreenMatchMode]
    SCREEN_MATCH_MODE_SHRINK: _ClassVar[ScreenMatchMode]

class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNIT_CENTIMETERS: _ClassVar[Unit]
    UNIT_MILLIMETERS: _ClassVar[Unit]
    UNIT_INCHES: _ClassVar[Unit]
    UNIT_POINTS: _ClassVar[Unit]
    UNIT_PICAS: _ClassVar[Unit]
SCALE_MODE_CONSTANT_PIXEL_SIZE: ScaleMode
SCALE_MODE_SCALE_WITH_SCREEN_SIZE: ScaleMode
SCALE_MODE_CONSTANT_PHYSICAL_SIZE: ScaleMode
SCREEN_MATCH_MODE_MATCH_WIDTH_OR_HEIGHT: ScreenMatchMode
SCREEN_MATCH_MODE_EXPAND: ScreenMatchMode
SCREEN_MATCH_MODE_SHRINK: ScreenMatchMode
UNIT_CENTIMETERS: Unit
UNIT_MILLIMETERS: Unit
UNIT_INCHES: Unit
UNIT_POINTS: Unit
UNIT_PICAS: Unit

class CanvasScalerCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasScalerDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasScalerUpdate(_message.Message):
    __slots__ = ["id", "ui_scale_mode", "reference_pixels_per_unit", "scale_factor", "reference_resolution", "screen_match_mode", "match_width_or_height", "physical_unit", "fallback_screen_dpi", "default_sprite_dpi", "dynamic_pixels_per_unit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    UI_SCALE_MODE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_PIXELS_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_WIDTH_OR_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_UNIT_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_SCREEN_DPI_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SPRITE_DPI_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PIXELS_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    ui_scale_mode: ScaleMode
    reference_pixels_per_unit: float
    scale_factor: float
    reference_resolution: _vector2_pb2.Vector2
    screen_match_mode: ScreenMatchMode
    match_width_or_height: float
    physical_unit: Unit
    fallback_screen_dpi: float
    default_sprite_dpi: float
    dynamic_pixels_per_unit: float
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., ui_scale_mode: _Optional[_Union[ScaleMode, str]] = ..., reference_pixels_per_unit: _Optional[float] = ..., scale_factor: _Optional[float] = ..., reference_resolution: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., screen_match_mode: _Optional[_Union[ScreenMatchMode, str]] = ..., match_width_or_height: _Optional[float] = ..., physical_unit: _Optional[_Union[Unit, str]] = ..., fallback_screen_dpi: _Optional[float] = ..., default_sprite_dpi: _Optional[float] = ..., dynamic_pixels_per_unit: _Optional[float] = ...) -> None: ...
