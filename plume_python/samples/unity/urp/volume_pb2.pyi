from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VolumeCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class VolumeDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class VolumeUpdate(_message.Message):
    __slots__ = ["id", "is_global", "colliders", "blend_distance", "weight", "priority", "shared_profile_id"]
    class Colliders(_message.Message):
        __slots__ = ["ids"]
        IDS_FIELD_NUMBER: _ClassVar[int]
        ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.ComponentIdentifier]
        def __init__(self, ids: _Optional[_Iterable[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_GLOBAL_FIELD_NUMBER: _ClassVar[int]
    COLLIDERS_FIELD_NUMBER: _ClassVar[int]
    BLEND_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SHARED_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    is_global: bool
    colliders: VolumeUpdate.Colliders
    blend_distance: float
    weight: float
    priority: float
    shared_profile_id: _identifiers_pb2.AssetIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., is_global: bool = ..., colliders: _Optional[_Union[VolumeUpdate.Colliders, _Mapping]] = ..., blend_distance: _Optional[float] = ..., weight: _Optional[float] = ..., priority: _Optional[float] = ..., shared_profile_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...

class VolumeUpdateEnabled(_message.Message):
    __slots__ = ["id", "enabled"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ...) -> None: ...
