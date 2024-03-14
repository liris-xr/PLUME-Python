from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightmapsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHTMAPS_MODE_NON_DIRECTIONAL: _ClassVar[LightmapsMode]
    LIGHTMAPS_MODE_COMBINED_DIRECTIONAL: _ClassVar[LightmapsMode]
LIGHTMAPS_MODE_NON_DIRECTIONAL: LightmapsMode
LIGHTMAPS_MODE_COMBINED_DIRECTIONAL: LightmapsMode

class LightmapsUpdate(_message.Message):
    __slots__ = ["lightmaps_mode", "lightmaps_data"]
    LIGHTMAPS_MODE_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAPS_DATA_FIELD_NUMBER: _ClassVar[int]
    lightmaps_mode: LightmapsMode
    lightmaps_data: _containers.RepeatedCompositeFieldContainer[LightmapData]
    def __init__(self, lightmaps_mode: _Optional[_Union[LightmapsMode, str]] = ..., lightmaps_data: _Optional[_Iterable[_Union[LightmapData, _Mapping]]] = ...) -> None: ...

class LightmapData(_message.Message):
    __slots__ = ["lightmap_color_texture_id", "lightmap_dir_texture_id", "lightmap_shadow_mask_texture_id"]
    LIGHTMAP_COLOR_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_DIR_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_SHADOW_MASK_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    lightmap_color_texture_id: _identifiers_pb2.AssetIdentifier
    lightmap_dir_texture_id: _identifiers_pb2.AssetIdentifier
    lightmap_shadow_mask_texture_id: _identifiers_pb2.AssetIdentifier
    def __init__(self, lightmap_color_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., lightmap_dir_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., lightmap_shadow_mask_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...
