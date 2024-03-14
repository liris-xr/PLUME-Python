from common import vector2_pb2 as _vector2_pb2
from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RectTransformCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class RectTransformDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class RectTransformUpdate(_message.Message):
    __slots__ = ["id", "anchor_min", "anchor_max", "anchored_position", "size_delta", "pivot"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_MIN_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_MAX_FIELD_NUMBER: _ClassVar[int]
    ANCHORED_POSITION_FIELD_NUMBER: _ClassVar[int]
    SIZE_DELTA_FIELD_NUMBER: _ClassVar[int]
    PIVOT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    anchor_min: _vector2_pb2.Vector2
    anchor_max: _vector2_pb2.Vector2
    anchored_position: _vector2_pb2.Vector2
    size_delta: _vector2_pb2.Vector2
    pivot: _vector2_pb2.Vector2
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., anchor_min: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., anchor_max: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., anchored_position: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., size_delta: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., pivot: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ...) -> None: ...
