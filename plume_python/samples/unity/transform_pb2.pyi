from common import vector3_pb2 as _vector3_pb2
from common import quaternion_pb2 as _quaternion_pb2
from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransformCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TransformDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TransformUpdate(_message.Message):
    __slots__ = ["id", "parent_transform_id", "sibling_idx", "local_position", "local_rotation", "local_scale"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TRANSFORM_ID_FIELD_NUMBER: _ClassVar[int]
    SIBLING_IDX_FIELD_NUMBER: _ClassVar[int]
    LOCAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ROTATION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SCALE_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    parent_transform_id: _identifiers_pb2.ComponentIdentifier
    sibling_idx: int
    local_position: _vector3_pb2.Vector3
    local_rotation: _quaternion_pb2.Quaternion
    local_scale: _vector3_pb2.Vector3
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., parent_transform_id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., sibling_idx: _Optional[int] = ..., local_position: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., local_rotation: _Optional[_Union[_quaternion_pb2.Quaternion, _Mapping]] = ..., local_scale: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ...) -> None: ...
