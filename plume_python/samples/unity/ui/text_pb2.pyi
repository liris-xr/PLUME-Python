from unity import identifiers_pb2 as _identifiers_pb2
from common import color_pb2 as _color_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HorizontalWrapMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    HORIZONTAL_WRAP_MODE_WRAP: _ClassVar[HorizontalWrapMode]
    HORIZONTAL_WRAP_MODE_OVERFLOW: _ClassVar[HorizontalWrapMode]

class VerticalWrapMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VERTICAL_WRAP_MODE_TRUNCATE: _ClassVar[VerticalWrapMode]
    VERTICAL_WRAP_MODE_OVERFLOW: _ClassVar[VerticalWrapMode]

class TextAnchor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TEXT_ANCHOR_UPPER_LEFT: _ClassVar[TextAnchor]
    TEXT_ANCHOR_UPPER_CENTER: _ClassVar[TextAnchor]
    TEXT_ANCHOR_UPPER_RIGHT: _ClassVar[TextAnchor]
    TEXT_ANCHOR_MIDDLE_LEFT: _ClassVar[TextAnchor]
    TEXT_ANCHOR_MIDDLE_CENTER: _ClassVar[TextAnchor]
    TEXT_ANCHOR_MIDDLE_RIGHT: _ClassVar[TextAnchor]
    TEXT_ANCHOR_LOWER_LEFT: _ClassVar[TextAnchor]
    TEXT_ANCHOR_LOWER_CENTER: _ClassVar[TextAnchor]
    TEXT_ANCHOR_LOWER_RIGHT: _ClassVar[TextAnchor]

class FontStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FONT_STYLE_NORMAL: _ClassVar[FontStyle]
    FONT_STYLE_BOLD: _ClassVar[FontStyle]
    FONT_STYLE_ITALIC: _ClassVar[FontStyle]
    FONT_STYLE_BOLD_AND_ITALIC: _ClassVar[FontStyle]
HORIZONTAL_WRAP_MODE_WRAP: HorizontalWrapMode
HORIZONTAL_WRAP_MODE_OVERFLOW: HorizontalWrapMode
VERTICAL_WRAP_MODE_TRUNCATE: VerticalWrapMode
VERTICAL_WRAP_MODE_OVERFLOW: VerticalWrapMode
TEXT_ANCHOR_UPPER_LEFT: TextAnchor
TEXT_ANCHOR_UPPER_CENTER: TextAnchor
TEXT_ANCHOR_UPPER_RIGHT: TextAnchor
TEXT_ANCHOR_MIDDLE_LEFT: TextAnchor
TEXT_ANCHOR_MIDDLE_CENTER: TextAnchor
TEXT_ANCHOR_MIDDLE_RIGHT: TextAnchor
TEXT_ANCHOR_LOWER_LEFT: TextAnchor
TEXT_ANCHOR_LOWER_CENTER: TextAnchor
TEXT_ANCHOR_LOWER_RIGHT: TextAnchor
FONT_STYLE_NORMAL: FontStyle
FONT_STYLE_BOLD: FontStyle
FONT_STYLE_ITALIC: FontStyle
FONT_STYLE_BOLD_AND_ITALIC: FontStyle

class TextCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TextDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TextUpdate(_message.Message):
    __slots__ = ["id", "text", "font_id", "font_style", "font_size", "color", "line_spacing", "support_rich_text", "alignment", "align_by_geometry", "horizontal_overflow", "vertical_overflow", "resize_text_for_best_fit", "resize_text_min_size", "resize_text_max_size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    FONT_ID_FIELD_NUMBER: _ClassVar[int]
    FONT_STYLE_FIELD_NUMBER: _ClassVar[int]
    FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ALIGN_BY_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_OVERFLOW_FIELD_NUMBER: _ClassVar[int]
    RESIZE_TEXT_FOR_BEST_FIT_FIELD_NUMBER: _ClassVar[int]
    RESIZE_TEXT_MIN_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESIZE_TEXT_MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    text: str
    font_id: _identifiers_pb2.AssetIdentifier
    font_style: FontStyle
    font_size: int
    color: _color_pb2.Color
    line_spacing: float
    support_rich_text: bool
    alignment: TextAnchor
    align_by_geometry: bool
    horizontal_overflow: HorizontalWrapMode
    vertical_overflow: VerticalWrapMode
    resize_text_for_best_fit: bool
    resize_text_min_size: int
    resize_text_max_size: int
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., text: _Optional[str] = ..., font_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., font_style: _Optional[_Union[FontStyle, str]] = ..., font_size: _Optional[int] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., line_spacing: _Optional[float] = ..., support_rich_text: bool = ..., alignment: _Optional[_Union[TextAnchor, str]] = ..., align_by_geometry: bool = ..., horizontal_overflow: _Optional[_Union[HorizontalWrapMode, str]] = ..., vertical_overflow: _Optional[_Union[VerticalWrapMode, str]] = ..., resize_text_for_best_fit: bool = ..., resize_text_min_size: _Optional[int] = ..., resize_text_max_size: _Optional[int] = ...) -> None: ...
