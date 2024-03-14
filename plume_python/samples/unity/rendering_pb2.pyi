from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ShadowCastingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SHADOW_CASTING_MODE_OFF: _ClassVar[ShadowCastingMode]
    SHADOW_CASTING_MODE_ON: _ClassVar[ShadowCastingMode]
    SHADOW_CASTING_MODE_TWO_SIDED: _ClassVar[ShadowCastingMode]
    SHADOW_CASTING_MODE_SHADOWS_ONLY: _ClassVar[ShadowCastingMode]

class ReflectionProbeUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFLECTION_PROBE_USAGE_OFF: _ClassVar[ReflectionProbeUsage]
    REFLECTION_PROBE_USAGE_BLEND_PROBES: _ClassVar[ReflectionProbeUsage]
    REFLECTION_PROBE_USAGE_BLEND_PROBES_AND_SKYBOX: _ClassVar[ReflectionProbeUsage]
    REFLECTION_PROBE_USAGE_SIMPLE: _ClassVar[ReflectionProbeUsage]

class RenderingPath(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RENDERING_PATH_USE_PLAYER_SETTINGS: _ClassVar[RenderingPath]
    RENDERING_PATH_VERTEX_LIT: _ClassVar[RenderingPath]
    RENDERING_PATH_FORWARD: _ClassVar[RenderingPath]
    RENDERING_PATH_DEFERRED_LIGHTING: _ClassVar[RenderingPath]
    RENDERING_PATH_DEFERRED_SHADING: _ClassVar[RenderingPath]

class OpaqueSortMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    OPAQUE_SORT_MODE_DEFAULT: _ClassVar[OpaqueSortMode]
    OPAQUE_SORT_MODE_FRONT_TO_BACK: _ClassVar[OpaqueSortMode]
    OPAQUE_SORT_MODE_NO_DISTANCE_SORT: _ClassVar[OpaqueSortMode]

class TransparencySortMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSPARENCY_SORT_MODE_DEFAULT: _ClassVar[TransparencySortMode]
    TRANSPARENCY_SORT_MODE_PERSPECTIVE: _ClassVar[TransparencySortMode]
    TRANSPARENCY_SORT_MODE_ORTHOGRAPHIC: _ClassVar[TransparencySortMode]
    TRANSPARENCY_SORT_MODE_CUSTOM_AXIS: _ClassVar[TransparencySortMode]
SHADOW_CASTING_MODE_OFF: ShadowCastingMode
SHADOW_CASTING_MODE_ON: ShadowCastingMode
SHADOW_CASTING_MODE_TWO_SIDED: ShadowCastingMode
SHADOW_CASTING_MODE_SHADOWS_ONLY: ShadowCastingMode
REFLECTION_PROBE_USAGE_OFF: ReflectionProbeUsage
REFLECTION_PROBE_USAGE_BLEND_PROBES: ReflectionProbeUsage
REFLECTION_PROBE_USAGE_BLEND_PROBES_AND_SKYBOX: ReflectionProbeUsage
REFLECTION_PROBE_USAGE_SIMPLE: ReflectionProbeUsage
RENDERING_PATH_USE_PLAYER_SETTINGS: RenderingPath
RENDERING_PATH_VERTEX_LIT: RenderingPath
RENDERING_PATH_FORWARD: RenderingPath
RENDERING_PATH_DEFERRED_LIGHTING: RenderingPath
RENDERING_PATH_DEFERRED_SHADING: RenderingPath
OPAQUE_SORT_MODE_DEFAULT: OpaqueSortMode
OPAQUE_SORT_MODE_FRONT_TO_BACK: OpaqueSortMode
OPAQUE_SORT_MODE_NO_DISTANCE_SORT: OpaqueSortMode
TRANSPARENCY_SORT_MODE_DEFAULT: TransparencySortMode
TRANSPARENCY_SORT_MODE_PERSPECTIVE: TransparencySortMode
TRANSPARENCY_SORT_MODE_ORTHOGRAPHIC: TransparencySortMode
TRANSPARENCY_SORT_MODE_CUSTOM_AXIS: TransparencySortMode
