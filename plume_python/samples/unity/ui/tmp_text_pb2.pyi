from unity import identifiers_pb2 as _identifiers_pb2
from common import vector4_pb2 as _vector4_pb2
from common import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TMPTextCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TMPTextDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TMPTextUpdate(_message.Message):
    __slots__ = ["id", "text", "font_id", "font_style", "font_size", "auto_size", "font_size_min", "font_size_max", "color", "character_spacing", "word_spacing", "line_spacing", "paragraph_spacing", "wrapping_enabled", "alignment", "overflow", "horizontal_mapping", "vertical_mapping", "margin"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FONT_ID_FIELD_NUMBER: _ClassVar[int]
    FONT_STYLE_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
    AUTO_SIZE_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_MIN_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_MAX_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SPACING_FIELD_NUMBER: _ClassVar[int]
    WORD_SPACING_FIELD_NUMBER: _ClassVar[int]
    LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPH_SPACING_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_MAPPING_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_MAPPING_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    text: str
    font_id: _identifiers_pb2.AssetIdentifier
    font_style: int
    font_size: float
    auto_size: bool
    font_size_min: float
    font_size_max: float
    color: _color_pb2.Color
    character_spacing: float
    word_spacing: float
    line_spacing: float
    paragraph_spacing: float
    wrapping_enabled: bool
    alignment: int
    overflow: int
    horizontal_mapping: int
    vertical_mapping: int
    margin: _vector4_pb2.Vector4
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., text: _Optional[str] = ..., font_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., font_style: _Optional[int] = ..., font_size: _Optional[float] = ..., auto_size: bool = ..., font_size_min: _Optional[float] = ..., font_size_max: _Optional[float] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., character_spacing: _Optional[float] = ..., word_spacing: _Optional[float] = ..., line_spacing: _Optional[float] = ..., paragraph_spacing: _Optional[float] = ..., wrapping_enabled: bool = ..., alignment: _Optional[int] = ..., overflow: _Optional[int] = ..., horizontal_mapping: _Optional[int] = ..., vertical_mapping: _Optional[int] = ..., margin: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...) -> None: ...
