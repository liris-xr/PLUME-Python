from unity import identifiers_pb2 as _identifiers_pb2
from unity import rendering_pb2 as _rendering_pb2
from common import vector3_pb2 as _vector3_pb2
from common import vector4_pb2 as _vector4_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TerrainCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TerrainDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class TerrainUpdate(_message.Message):
    __slots__ = ["id", "enabled", "terrain_data_id", "tree_distance", "tree_billboard_distance", "tree_cross_fade_length", "tree_maximum_full_lod_count", "detail_object_distance", "detail_object_density", "heightmap_pixel_error", "heightmap_maximum_lod", "basemap_distance", "lightmap_index", "realtime_lightmap_index", "lightmap_scale_offset", "realtime_lightmap_scale_offset", "keep_unused_rendering_resources", "shadow_casting_mode", "reflection_probe_usage", "material_template_id", "draw_heightmap", "allow_auto_connect", "grouping_id", "draw_instanced", "normalmap_texture_id", "draw_trees_and_foliage", "patch_bounds_multiplier", "tree_lod_bias_multiplier", "collect_detail_patches"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TERRAIN_DATA_ID_FIELD_NUMBER: _ClassVar[int]
    TREE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TREE_BILLBOARD_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TREE_CROSS_FADE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TREE_MAXIMUM_FULL_LOD_COUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_OBJECT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_OBJECT_DENSITY_FIELD_NUMBER: _ClassVar[int]
    HEIGHTMAP_PIXEL_ERROR_FIELD_NUMBER: _ClassVar[int]
    HEIGHTMAP_MAXIMUM_LOD_FIELD_NUMBER: _ClassVar[int]
    BASEMAP_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_INDEX_FIELD_NUMBER: _ClassVar[int]
    REALTIME_LIGHTMAP_INDEX_FIELD_NUMBER: _ClassVar[int]
    LIGHTMAP_SCALE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    REALTIME_LIGHTMAP_SCALE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    KEEP_UNUSED_RENDERING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SHADOW_CASTING_MODE_FIELD_NUMBER: _ClassVar[int]
    REFLECTION_PROBE_USAGE_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    DRAW_HEIGHTMAP_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AUTO_CONNECT_FIELD_NUMBER: _ClassVar[int]
    GROUPING_ID_FIELD_NUMBER: _ClassVar[int]
    DRAW_INSTANCED_FIELD_NUMBER: _ClassVar[int]
    NORMALMAP_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    DRAW_TREES_AND_FOLIAGE_FIELD_NUMBER: _ClassVar[int]
    PATCH_BOUNDS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    TREE_LOD_BIAS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    COLLECT_DETAIL_PATCHES_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    terrain_data_id: _identifiers_pb2.AssetIdentifier
    tree_distance: float
    tree_billboard_distance: float
    tree_cross_fade_length: float
    tree_maximum_full_lod_count: int
    detail_object_distance: float
    detail_object_density: float
    heightmap_pixel_error: float
    heightmap_maximum_lod: int
    basemap_distance: float
    lightmap_index: int
    realtime_lightmap_index: int
    lightmap_scale_offset: _vector4_pb2.Vector4
    realtime_lightmap_scale_offset: _vector4_pb2.Vector4
    keep_unused_rendering_resources: bool
    shadow_casting_mode: _rendering_pb2.ShadowCastingMode
    reflection_probe_usage: _rendering_pb2.ReflectionProbeUsage
    material_template_id: _identifiers_pb2.AssetIdentifier
    draw_heightmap: bool
    allow_auto_connect: bool
    grouping_id: int
    draw_instanced: bool
    normalmap_texture_id: _identifiers_pb2.AssetIdentifier
    draw_trees_and_foliage: bool
    patch_bounds_multiplier: _vector3_pb2.Vector3
    tree_lod_bias_multiplier: float
    collect_detail_patches: bool
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ..., terrain_data_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., tree_distance: _Optional[float] = ..., tree_billboard_distance: _Optional[float] = ..., tree_cross_fade_length: _Optional[float] = ..., tree_maximum_full_lod_count: _Optional[int] = ..., detail_object_distance: _Optional[float] = ..., detail_object_density: _Optional[float] = ..., heightmap_pixel_error: _Optional[float] = ..., heightmap_maximum_lod: _Optional[int] = ..., basemap_distance: _Optional[float] = ..., lightmap_index: _Optional[int] = ..., realtime_lightmap_index: _Optional[int] = ..., lightmap_scale_offset: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., realtime_lightmap_scale_offset: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., keep_unused_rendering_resources: bool = ..., shadow_casting_mode: _Optional[_Union[_rendering_pb2.ShadowCastingMode, str]] = ..., reflection_probe_usage: _Optional[_Union[_rendering_pb2.ReflectionProbeUsage, str]] = ..., material_template_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., draw_heightmap: bool = ..., allow_auto_connect: bool = ..., grouping_id: _Optional[int] = ..., draw_instanced: bool = ..., normalmap_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., draw_trees_and_foliage: bool = ..., patch_bounds_multiplier: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., tree_lod_bias_multiplier: _Optional[float] = ..., collect_detail_patches: bool = ...) -> None: ...
