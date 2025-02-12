from plume.sample.common import vector3_pb2 as _vector3_pb2
from plume.sample.common import quaternion_pb2 as _quaternion_pb2
from plume.sample.common import vector2_pb2 as _vector2_pb2
from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RectTransformCreate(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class RectTransformDestroy(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class RectTransformUpdate(_message.Message):
    __slots__ = ("component", "parent_transform", "sibling_idx", "local_position", "local_rotation", "local_scale", "anchor_min", "anchor_max", "anchored_position", "size_delta", "pivot")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    SIBLING_IDX_FIELD_NUMBER: _ClassVar[int]
    LOCAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROTATION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SCALE_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_MIN_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_MAX_FIELD_NUMBER: _ClassVar[int]
    ANCHORED_POSITION_FIELD_NUMBER: _ClassVar[int]
    SIZE_DELTA_FIELD_NUMBER: _ClassVar[int]
    PIVOT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    parent_transform: _identifiers_pb2.ComponentIdentifier
    sibling_idx: int
    local_position: _vector3_pb2.Vector3
    local_rotation: _quaternion_pb2.Quaternion
    local_scale: _vector3_pb2.Vector3
    anchor_min: _vector2_pb2.Vector2
    anchor_max: _vector2_pb2.Vector2
    anchored_position: _vector2_pb2.Vector2
    size_delta: _vector2_pb2.Vector2
    pivot: _vector2_pb2.Vector2
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., parent_transform: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., sibling_idx: _Optional[int] = ..., local_position: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., local_rotation: _Optional[_Union[_quaternion_pb2.Quaternion, _Mapping]] = ..., local_scale: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., anchor_min: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., anchor_max: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., anchored_position: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., size_delta: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., pivot: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ...) -> None: ...
