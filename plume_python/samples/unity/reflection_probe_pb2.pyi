from unity import identifiers_pb2 as _identifiers_pb2
from common import bounds_pb2 as _bounds_pb2
from common import color_pb2 as _color_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReflectionProbeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFLECTION_PROBE_MODE_BAKED: _ClassVar[ReflectionProbeMode]
    REFLECTION_PROBE_MODE_CUSTOM: _ClassVar[ReflectionProbeMode]
    REFLECTION_PROBE_MODE_REALTIME: _ClassVar[ReflectionProbeMode]

class ReflectionProbeClearFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFLECTION_PROBE_CLEAR_FLAGS_SKYBOX: _ClassVar[ReflectionProbeClearFlags]
    REFLECTION_PROBE_CLEAR_FLAGS_SOLID_COLOR: _ClassVar[ReflectionProbeClearFlags]

class ReflectionProbeRefreshMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFLECTION_PROBE_REFRESH_MODE_ON_AWAKE: _ClassVar[ReflectionProbeRefreshMode]
    REFLECTION_PROBE_REFRESH_MODE_EVERY_FRAME: _ClassVar[ReflectionProbeRefreshMode]
    REFLECTION_PROBE_REFRESH_MODE_VIA_SCRIPTING: _ClassVar[ReflectionProbeRefreshMode]

class ReflectionProbeTimeSlicingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFLECTION_PROBE_TIME_SLICING_MODE_ALL_FACES_AT_ONCE: _ClassVar[ReflectionProbeTimeSlicingMode]
    REFLECTION_PROBE_TIME_SLICING_MODE_INDIVIDUAL_FACES: _ClassVar[ReflectionProbeTimeSlicingMode]
    REFLECTION_PROBE_TIME_SLICING_MODE_NO_TIME_SLICING: _ClassVar[ReflectionProbeTimeSlicingMode]
REFLECTION_PROBE_MODE_BAKED: ReflectionProbeMode
REFLECTION_PROBE_MODE_CUSTOM: ReflectionProbeMode
REFLECTION_PROBE_MODE_REALTIME: ReflectionProbeMode
REFLECTION_PROBE_CLEAR_FLAGS_SKYBOX: ReflectionProbeClearFlags
REFLECTION_PROBE_CLEAR_FLAGS_SOLID_COLOR: ReflectionProbeClearFlags
REFLECTION_PROBE_REFRESH_MODE_ON_AWAKE: ReflectionProbeRefreshMode
REFLECTION_PROBE_REFRESH_MODE_EVERY_FRAME: ReflectionProbeRefreshMode
REFLECTION_PROBE_REFRESH_MODE_VIA_SCRIPTING: ReflectionProbeRefreshMode
REFLECTION_PROBE_TIME_SLICING_MODE_ALL_FACES_AT_ONCE: ReflectionProbeTimeSlicingMode
REFLECTION_PROBE_TIME_SLICING_MODE_INDIVIDUAL_FACES: ReflectionProbeTimeSlicingMode
REFLECTION_PROBE_TIME_SLICING_MODE_NO_TIME_SLICING: ReflectionProbeTimeSlicingMode

class ReflectionProbeCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class ReflectionProbeDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class ReflectionProbeUpdate(_message.Message):
    __slots__ = ["id", "enabled", "mode", "refresh_mode", "time_slicing_mode", "clear_flags", "importance", "intensity", "near_clip_plane", "far_clip_plane", "render_dynamic_objects", "box_projection", "blend_distance", "bounds", "resolution", "hdr", "shadow_distance", "background_color", "culling_mask", "custom_baked_texture_id", "baked_texture_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_MODE_FIELD_NUMBER: _ClassVar[int]
    TIME_SLICING_MODE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FLAGS_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    NEAR_CLIP_PLANE_FIELD_NUMBER: _ClassVar[int]
    FAR_CLIP_PLANE_FIELD_NUMBER: _ClassVar[int]
    RENDER_DYNAMIC_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    BOX_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    BLEND_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    HDR_FIELD_NUMBER: _ClassVar[int]
    SHADOW_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    CULLING_MASK_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BAKED_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    BAKED_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    mode: ReflectionProbeMode
    refresh_mode: ReflectionProbeRefreshMode
    time_slicing_mode: ReflectionProbeTimeSlicingMode
    clear_flags: ReflectionProbeClearFlags
    importance: int
    intensity: float
    near_clip_plane: float
    far_clip_plane: float
    render_dynamic_objects: bool
    box_projection: bool
    blend_distance: float
    bounds: _bounds_pb2.Bounds
    resolution: int
    hdr: bool
    shadow_distance: float
    background_color: _color_pb2.Color
    culling_mask: int
    custom_baked_texture_id: _identifiers_pb2.AssetIdentifier
    baked_texture_id: _identifiers_pb2.AssetIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ..., mode: _Optional[_Union[ReflectionProbeMode, str]] = ..., refresh_mode: _Optional[_Union[ReflectionProbeRefreshMode, str]] = ..., time_slicing_mode: _Optional[_Union[ReflectionProbeTimeSlicingMode, str]] = ..., clear_flags: _Optional[_Union[ReflectionProbeClearFlags, str]] = ..., importance: _Optional[int] = ..., intensity: _Optional[float] = ..., near_clip_plane: _Optional[float] = ..., far_clip_plane: _Optional[float] = ..., render_dynamic_objects: bool = ..., box_projection: bool = ..., blend_distance: _Optional[float] = ..., bounds: _Optional[_Union[_bounds_pb2.Bounds, _Mapping]] = ..., resolution: _Optional[int] = ..., hdr: bool = ..., shadow_distance: _Optional[float] = ..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., culling_mask: _Optional[int] = ..., custom_baked_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., baked_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...
