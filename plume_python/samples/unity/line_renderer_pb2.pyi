from unity import identifiers_pb2 as _identifiers_pb2
from common import color_pb2 as _color_pb2
from common import vector2_pb2 as _vector2_pb2
from common import vector3_pb2 as _vector3_pb2
from common import animation_curve_pb2 as _animation_curve_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ALIGNMENT_VIEW: _ClassVar[Alignment]
    ALIGNMENT_TRANSFORM_Z: _ClassVar[Alignment]

class TextureMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TEXTURE_MODE_STRETCH: _ClassVar[TextureMode]
    TEXTURE_MODE_TILE: _ClassVar[TextureMode]
    TEXTURE_MODE_DISTRIBUTE_PER_SEGMENT: _ClassVar[TextureMode]
    TEXTURE_MODE_REPEAT_PER_SEGMENT: _ClassVar[TextureMode]
    TEXTURE_MODE_STATIC: _ClassVar[TextureMode]

class MaskInteraction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MASK_INTERACTION_NONE: _ClassVar[MaskInteraction]
    MASK_INTERACTION_VISIBLE_INSIDE: _ClassVar[MaskInteraction]
    MASK_INTERACTION_VISIBLE_OUTSIDE: _ClassVar[MaskInteraction]
ALIGNMENT_VIEW: Alignment
ALIGNMENT_TRANSFORM_Z: Alignment
TEXTURE_MODE_STRETCH: TextureMode
TEXTURE_MODE_TILE: TextureMode
TEXTURE_MODE_DISTRIBUTE_PER_SEGMENT: TextureMode
TEXTURE_MODE_REPEAT_PER_SEGMENT: TextureMode
TEXTURE_MODE_STATIC: TextureMode
MASK_INTERACTION_NONE: MaskInteraction
MASK_INTERACTION_VISIBLE_INSIDE: MaskInteraction
MASK_INTERACTION_VISIBLE_OUTSIDE: MaskInteraction

class LineRendererCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class LineRendererDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class LineRendererUpdate(_message.Message):
    __slots__ = ["id", "loop", "width_curve", "width_multiplier", "positions", "color", "corner_vertices", "end_cap_vertices", "alignment", "texture_mode", "texture_scale", "shadow_bias", "generate_lighting_data", "use_world_space", "mask_interaction"]
    class Positions(_message.Message):
        __slots__ = ["positions"]
        POSITIONS_FIELD_NUMBER: _ClassVar[int]
        positions: _containers.RepeatedCompositeFieldContainer[_vector3_pb2.Vector3]
        def __init__(self, positions: _Optional[_Iterable[_Union[_vector3_pb2.Vector3, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    WIDTH_CURVE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CORNER_VERTICES_FIELD_NUMBER: _ClassVar[int]
    END_CAP_VERTICES_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    TEXTURE_MODE_FIELD_NUMBER: _ClassVar[int]
    TEXTURE_SCALE_FIELD_NUMBER: _ClassVar[int]
    SHADOW_BIAS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_LIGHTING_DATA_FIELD_NUMBER: _ClassVar[int]
    USE_WORLD_SPACE_FIELD_NUMBER: _ClassVar[int]
    MASK_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    loop: bool
    width_curve: _animation_curve_pb2.AnimationCurve
    width_multiplier: float
    positions: LineRendererUpdate.Positions
    color: _color_pb2.ColorGradient
    corner_vertices: int
    end_cap_vertices: int
    alignment: Alignment
    texture_mode: TextureMode
    texture_scale: _vector2_pb2.Vector2
    shadow_bias: float
    generate_lighting_data: bool
    use_world_space: bool
    mask_interaction: MaskInteraction
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., loop: bool = ..., width_curve: _Optional[_Union[_animation_curve_pb2.AnimationCurve, _Mapping]] = ..., width_multiplier: _Optional[float] = ..., positions: _Optional[_Union[LineRendererUpdate.Positions, _Mapping]] = ..., color: _Optional[_Union[_color_pb2.ColorGradient, _Mapping]] = ..., corner_vertices: _Optional[int] = ..., end_cap_vertices: _Optional[int] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., texture_mode: _Optional[_Union[TextureMode, str]] = ..., texture_scale: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., shadow_bias: _Optional[float] = ..., generate_lighting_data: bool = ..., use_world_space: bool = ..., mask_interaction: _Optional[_Union[MaskInteraction, str]] = ...) -> None: ...
