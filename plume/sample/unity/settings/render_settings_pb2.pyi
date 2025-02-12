from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from plume.sample.common import color_pb2 as _color_pb2
from plume.sample.common import spherical_harmonics_l2_pb2 as _spherical_harmonics_l2_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FogMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOG_MODE_UNSPECIFIED: _ClassVar[FogMode]
    FOG_MODE_LINEAR: _ClassVar[FogMode]
    FOG_MODE_EXPONENTIAL: _ClassVar[FogMode]
    FOG_MODE_EXPONENTIAL_SQUARED: _ClassVar[FogMode]

class AmbientMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AMBIENT_MODE_UNSPECIFIED: _ClassVar[AmbientMode]
    AMBIENT_MODE_SKYBOX: _ClassVar[AmbientMode]
    AMBIENT_MODE_TRILIGHT: _ClassVar[AmbientMode]
    AMBIENT_MODE_FLAT: _ClassVar[AmbientMode]
    AMBIENT_MODE_CUSTOM: _ClassVar[AmbientMode]

class DefaultReflectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT_REFLECTION_MODE_UNSPECIFIED: _ClassVar[DefaultReflectionMode]
    DEFAULT_REFLECTION_MODE_SKYBOX: _ClassVar[DefaultReflectionMode]
    DEFAULT_REFLECTION_MODE_CUSTOM: _ClassVar[DefaultReflectionMode]
FOG_MODE_UNSPECIFIED: FogMode
FOG_MODE_LINEAR: FogMode
FOG_MODE_EXPONENTIAL: FogMode
FOG_MODE_EXPONENTIAL_SQUARED: FogMode
AMBIENT_MODE_UNSPECIFIED: AmbientMode
AMBIENT_MODE_SKYBOX: AmbientMode
AMBIENT_MODE_TRILIGHT: AmbientMode
AMBIENT_MODE_FLAT: AmbientMode
AMBIENT_MODE_CUSTOM: AmbientMode
DEFAULT_REFLECTION_MODE_UNSPECIFIED: DefaultReflectionMode
DEFAULT_REFLECTION_MODE_SKYBOX: DefaultReflectionMode
DEFAULT_REFLECTION_MODE_CUSTOM: DefaultReflectionMode

class RenderSettingsUpdate(_message.Message):
    __slots__ = ("skybox", "sun", "fog", "fog_mode", "fog_color", "fog_density", "fog_start_distance", "fog_end_distance", "ambient_light_color", "ambient_equator_color", "ambient_ground_color", "ambient_sky_color", "ambient_intensity", "ambient_mode", "ambient_probe", "custom_reflection_texture", "default_reflection_mode", "default_reflection_resolution", "reflection_bounces", "reflection_intensity", "halo_strength", "flare_strength", "flare_fade_speed", "subtractive_shadow_color")
    SKYBOX_FIELD_NUMBER: _ClassVar[int]
    SUN_FIELD_NUMBER: _ClassVar[int]
    FOG_FIELD_NUMBER: _ClassVar[int]
    FOG_MODE_FIELD_NUMBER: _ClassVar[int]
    FOG_COLOR_FIELD_NUMBER: _ClassVar[int]
    FOG_DENSITY_FIELD_NUMBER: _ClassVar[int]
    FOG_START_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    FOG_END_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_LIGHT_COLOR_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_EQUATOR_COLOR_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_GROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_SKY_COLOR_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_MODE_FIELD_NUMBER: _ClassVar[int]
    AMBIENT_PROBE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_REFLECTION_TEXTURE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REFLECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REFLECTION_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    REFLECTION_BOUNCES_FIELD_NUMBER: _ClassVar[int]
    REFLECTION_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    HALO_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    FLARE_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    FLARE_FADE_SPEED_FIELD_NUMBER: _ClassVar[int]
    SUBTRACTIVE_SHADOW_COLOR_FIELD_NUMBER: _ClassVar[int]
    skybox: _identifiers_pb2.AssetIdentifier
    sun: _identifiers_pb2.ComponentIdentifier
    fog: bool
    fog_mode: FogMode
    fog_color: _color_pb2.Color
    fog_density: float
    fog_start_distance: float
    fog_end_distance: float
    ambient_light_color: _color_pb2.Color
    ambient_equator_color: _color_pb2.Color
    ambient_ground_color: _color_pb2.Color
    ambient_sky_color: _color_pb2.Color
    ambient_intensity: float
    ambient_mode: AmbientMode
    ambient_probe: _spherical_harmonics_l2_pb2.SphericalHarmonicsL2
    custom_reflection_texture: _identifiers_pb2.AssetIdentifier
    default_reflection_mode: DefaultReflectionMode
    default_reflection_resolution: int
    reflection_bounces: int
    reflection_intensity: float
    halo_strength: float
    flare_strength: float
    flare_fade_speed: float
    subtractive_shadow_color: _color_pb2.Color
    def __init__(self, skybox: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., sun: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., fog: bool = ..., fog_mode: _Optional[_Union[FogMode, str]] = ..., fog_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., fog_density: _Optional[float] = ..., fog_start_distance: _Optional[float] = ..., fog_end_distance: _Optional[float] = ..., ambient_light_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., ambient_equator_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., ambient_ground_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., ambient_sky_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., ambient_intensity: _Optional[float] = ..., ambient_mode: _Optional[_Union[AmbientMode, str]] = ..., ambient_probe: _Optional[_Union[_spherical_harmonics_l2_pb2.SphericalHarmonicsL2, _Mapping]] = ..., custom_reflection_texture: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., default_reflection_mode: _Optional[_Union[DefaultReflectionMode, str]] = ..., default_reflection_resolution: _Optional[int] = ..., reflection_bounces: _Optional[int] = ..., reflection_intensity: _Optional[float] = ..., halo_strength: _Optional[float] = ..., flare_strength: _Optional[float] = ..., flare_fade_speed: _Optional[float] = ..., subtractive_shadow_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
