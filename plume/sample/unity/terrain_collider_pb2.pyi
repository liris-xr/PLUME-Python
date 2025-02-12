from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TerrainColliderCreate(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TerrainColliderDestroy(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TerrainColliderUpdate(_message.Message):
    __slots__ = ("component", "enabled", "terrain_data", "material")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_DATA_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    terrain_data: _identifiers_pb2.AssetIdentifier
    material: _identifiers_pb2.AssetIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ..., terrain_data: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., material: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...
