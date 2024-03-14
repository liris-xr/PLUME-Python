from unity import identifiers_pb2 as _identifiers_pb2
from common import bounds_pb2 as _bounds_pb2
from common import vector4_pb2 as _vector4_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RendererUpdate(_message.Message):
    __slots__ = ["id", "enabled", "materials", "local_bounds", "lightmap_index", "lightmap_scale_offset", "realtime_lightmap_index", "realtime_lightmap_scale_offset"]
    class Materials(_message.Message):
        __slots__ = ["ids"]
        IDS_FIELD_NUMBER: _ClassVar[int]
        ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.AssetIdentifier]
        def __init__(self, ids: _Optional[_Iterable[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_BOUNDS_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_INDEX_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_SCALE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    REALTIME_LIGHTMAP_INDEX_FIELD_NUMBER: _ClassVar[int]
    REALTIME_LIGHTMAP_SCALE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    materials: RendererUpdate.Materials
    local_bounds: _bounds_pb2.Bounds
    lightmap_index: int
    lightmap_scale_offset: _vector4_pb2.Vector4
    realtime_lightmap_index: int
    realtime_lightmap_scale_offset: _vector4_pb2.Vector4
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ..., materials: _Optional[_Union[RendererUpdate.Materials, _Mapping]] = ..., local_bounds: _Optional[_Union[_bounds_pb2.Bounds, _Mapping]] = ..., lightmap_index: _Optional[int] = ..., lightmap_scale_offset: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., realtime_lightmap_index: _Optional[int] = ..., realtime_lightmap_scale_offset: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...) -> None: ...
