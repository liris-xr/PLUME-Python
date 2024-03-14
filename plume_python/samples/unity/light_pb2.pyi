from unity import identifiers_pb2 as _identifiers_pb2
from common import matrix4x4_pb2 as _matrix4x4_pb2
from common import vector4_pb2 as _vector4_pb2
from common import color_pb2 as _color_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LightType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHT_TYPE_SPOT: _ClassVar[LightType]
    LIGHT_TYPE_DIRECTIONAL: _ClassVar[LightType]
    LIGHT_TYPE_POINT: _ClassVar[LightType]
    LIGHT_TYPE_AREA: _ClassVar[LightType]
    LIGHT_TYPE_RECTANGLE: _ClassVar[LightType]
    LIGHT_TYPE_DISC: _ClassVar[LightType]

class LightShape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHT_SHAPE_CONE: _ClassVar[LightShape]
    LIGHT_SHAPE_PYRAMID: _ClassVar[LightShape]
    LIGHT_SHAPE_BOX: _ClassVar[LightShape]

class LightShadowCasterMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHT_SHADOW_CASTER_MODE_DEFAULT: _ClassVar[LightShadowCasterMode]
    LIGHT_SHADOW_CASTER_MODE_NON_LIGHTMAPPED_ONLY: _ClassVar[LightShadowCasterMode]
    LIGHT_SHADOW_CASTER_MODE_EVERYTHING: _ClassVar[LightShadowCasterMode]

class LightShadowResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHT_SHADOW_RESOLUTION_FROM_QUALITY_SETTINGS: _ClassVar[LightShadowResolution]
    LIGHT_SHADOW_RESOLUTION_LOW: _ClassVar[LightShadowResolution]
    LIGHT_SHADOW_RESOLUTION_MEDIUM: _ClassVar[LightShadowResolution]
    LIGHT_SHADOW_RESOLUTION_HIGH: _ClassVar[LightShadowResolution]
    LIGHT_SHADOW_RESOLUTION_VERY_HIGH: _ClassVar[LightShadowResolution]

class LightShadows(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LIGHT_SHADOWS_NONE: _ClassVar[LightShadows]
    LIGHT_SHADOWS_HARD: _ClassVar[LightShadows]
    LIGHT_SHADOWS_SOFT: _ClassVar[LightShadows]
LIGHT_TYPE_SPOT: LightType
LIGHT_TYPE_DIRECTIONAL: LightType
LIGHT_TYPE_POINT: LightType
LIGHT_TYPE_AREA: LightType
LIGHT_TYPE_RECTANGLE: LightType
LIGHT_TYPE_DISC: LightType
LIGHT_SHAPE_CONE: LightShape
LIGHT_SHAPE_PYRAMID: LightShape
LIGHT_SHAPE_BOX: LightShape
LIGHT_SHADOW_CASTER_MODE_DEFAULT: LightShadowCasterMode
LIGHT_SHADOW_CASTER_MODE_NON_LIGHTMAPPED_ONLY: LightShadowCasterMode
LIGHT_SHADOW_CASTER_MODE_EVERYTHING: LightShadowCasterMode
LIGHT_SHADOW_RESOLUTION_FROM_QUALITY_SETTINGS: LightShadowResolution
LIGHT_SHADOW_RESOLUTION_LOW: LightShadowResolution
LIGHT_SHADOW_RESOLUTION_MEDIUM: LightShadowResolution
LIGHT_SHADOW_RESOLUTION_HIGH: LightShadowResolution
LIGHT_SHADOW_RESOLUTION_VERY_HIGH: LightShadowResolution
LIGHT_SHADOWS_NONE: LightShadows
LIGHT_SHADOWS_HARD: LightShadows
LIGHT_SHADOWS_SOFT: LightShadows

class LightCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class LightDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class LightUpdate(_message.Message):
    __slots__ = ["id", "enabled", "type", "shape", "intensity", "bounce_intensity", "range", "color", "color_temperature", "use_color_temperature", "spot_angle", "inner_spot_angle", "shadows", "shadow_strength", "shadow_resolution", "shadow_matrix_override", "use_shadow_matrix_override", "shadow_bias", "shadow_normal_bias", "shadow_near_plane", "use_view_frustum_for_shadow_caster_cull", "layer_shadow_cull_distances", "shadow_custom_resolution", "light_shadow_caster_mode", "rendering_layer_mask", "culling_mask", "bounding_sphere_override", "use_bounding_sphere_override", "cookie_id", "cookie_size", "flare_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    BOUNCE_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    COLOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    USE_COLOR_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SPOT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    INNER_SPOT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    SHADOWS_FIELD_NUMBER: _ClassVar[int]
    SHADOW_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    SHADOW_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SHADOW_MATRIX_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    USE_SHADOW_MATRIX_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SHADOW_BIAS_FIELD_NUMBER: _ClassVar[int]
    SHADOW_NORMAL_BIAS_FIELD_NUMBER: _ClassVar[int]
    SHADOW_NEAR_PLANE_FIELD_NUMBER: _ClassVar[int]
    USE_VIEW_FRUSTUM_FOR_SHADOW_CASTER_CULL_FIELD_NUMBER: _ClassVar[int]
    LAYER_SHADOW_CULL_DISTANCES_FIELD_NUMBER: _ClassVar[int]
    SHADOW_CUSTOM_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SHADOW_CASTER_MODE_FIELD_NUMBER: _ClassVar[int]
    RENDERING_LAYER_MASK_FIELD_NUMBER: _ClassVar[int]
    CULLING_MASK_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_SPHERE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    USE_BOUNDING_SPHERE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    COOKIE_ID_FIELD_NUMBER: _ClassVar[int]
    COOKIE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FLARE_ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    type: LightType
    shape: LightShape
    intensity: float
    bounce_intensity: float
    range: float
    color: _color_pb2.Color
    color_temperature: float
    use_color_temperature: bool
    spot_angle: float
    inner_spot_angle: float
    shadows: LightShadows
    shadow_strength: float
    shadow_resolution: LightShadowResolution
    shadow_matrix_override: _matrix4x4_pb2.Matrix4x4
    use_shadow_matrix_override: bool
    shadow_bias: float
    shadow_normal_bias: float
    shadow_near_plane: float
    use_view_frustum_for_shadow_caster_cull: bool
    layer_shadow_cull_distances: LayerShadowCullDistances
    shadow_custom_resolution: int
    light_shadow_caster_mode: LightShadowCasterMode
    rendering_layer_mask: int
    culling_mask: int
    bounding_sphere_override: _vector4_pb2.Vector4
    use_bounding_sphere_override: bool
    cookie_id: _identifiers_pb2.AssetIdentifier
    cookie_size: float
    flare_id: _identifiers_pb2.AssetIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ..., type: _Optional[_Union[LightType, str]] = ..., shape: _Optional[_Union[LightShape, str]] = ..., intensity: _Optional[float] = ..., bounce_intensity: _Optional[float] = ..., range: _Optional[float] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., color_temperature: _Optional[float] = ..., use_color_temperature: bool = ..., spot_angle: _Optional[float] = ..., inner_spot_angle: _Optional[float] = ..., shadows: _Optional[_Union[LightShadows, str]] = ..., shadow_strength: _Optional[float] = ..., shadow_resolution: _Optional[_Union[LightShadowResolution, str]] = ..., shadow_matrix_override: _Optional[_Union[_matrix4x4_pb2.Matrix4x4, _Mapping]] = ..., use_shadow_matrix_override: bool = ..., shadow_bias: _Optional[float] = ..., shadow_normal_bias: _Optional[float] = ..., shadow_near_plane: _Optional[float] = ..., use_view_frustum_for_shadow_caster_cull: bool = ..., layer_shadow_cull_distances: _Optional[_Union[LayerShadowCullDistances, _Mapping]] = ..., shadow_custom_resolution: _Optional[int] = ..., light_shadow_caster_mode: _Optional[_Union[LightShadowCasterMode, str]] = ..., rendering_layer_mask: _Optional[int] = ..., culling_mask: _Optional[int] = ..., bounding_sphere_override: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., use_bounding_sphere_override: bool = ..., cookie_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., cookie_size: _Optional[float] = ..., flare_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...

class LayerShadowCullDistances(_message.Message):
    __slots__ = ["distances"]
    DISTANCES_FIELD_NUMBER: _ClassVar[int]
    distances: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, distances: _Optional[_Iterable[float]] = ...) -> None: ...
