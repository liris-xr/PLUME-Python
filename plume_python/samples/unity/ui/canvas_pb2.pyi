from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RenderMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RENDER_MODE_SCREEN_SPACE_OVERLAY: _ClassVar[RenderMode]
    RENDER_MODE_SCREEN_SPACE_CAMERA: _ClassVar[RenderMode]
    RENDER_MODE_WORLD_SPACE: _ClassVar[RenderMode]

class StandaloneRenderResize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STANDALONE_RENDER_RESIZE_ENABLED: _ClassVar[StandaloneRenderResize]
    STANDALONE_RENDER_RESIZE_DISABLED: _ClassVar[StandaloneRenderResize]
RENDER_MODE_SCREEN_SPACE_OVERLAY: RenderMode
RENDER_MODE_SCREEN_SPACE_CAMERA: RenderMode
RENDER_MODE_WORLD_SPACE: RenderMode
STANDALONE_RENDER_RESIZE_ENABLED: StandaloneRenderResize
STANDALONE_RENDER_RESIZE_DISABLED: StandaloneRenderResize

class CanvasCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasUpdate(_message.Message):
    __slots__ = ["id", "render_mode", "scale_factor", "reference_pixels_per_unit", "override_pixel_perfect", "vertex_color_always_gamma_space", "pixel_perfect", "plane_distance", "override_sorting", "sorting_order", "target_display", "sorting_layer_id", "additional_shader_channels", "sorting_layer_name", "update_rect_transform_for_standalone", "world_camera", "normalized_sorting_grid_size"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_MODE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_PIXELS_PER_UNIT_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PIXEL_PERFECT_FIELD_NUMBER: _ClassVar[int]
    VERTEX_COLOR_ALWAYS_GAMMA_SPACE_FIELD_NUMBER: _ClassVar[int]
    PIXEL_PERFECT_FIELD_NUMBER: _ClassVar[int]
    PLANE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_SORTING_FIELD_NUMBER: _ClassVar[int]
    SORTING_ORDER_FIELD_NUMBER: _ClassVar[int]
    TARGET_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    SORTING_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_SHADER_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SORTING_LAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_RECT_TRANSFORM_FOR_STANDALONE_FIELD_NUMBER: _ClassVar[int]
    WORLD_CAMERA_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_SORTING_GRID_SIZE_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    render_mode: RenderMode
    scale_factor: float
    reference_pixels_per_unit: float
    override_pixel_perfect: bool
    vertex_color_always_gamma_space: bool
    pixel_perfect: bool
    plane_distance: float
    override_sorting: bool
    sorting_order: int
    target_display: int
    sorting_layer_id: int
    additional_shader_channels: int
    sorting_layer_name: str
    update_rect_transform_for_standalone: StandaloneRenderResize
    world_camera: _identifiers_pb2.ComponentIdentifier
    normalized_sorting_grid_size: float
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., render_mode: _Optional[_Union[RenderMode, str]] = ..., scale_factor: _Optional[float] = ..., reference_pixels_per_unit: _Optional[float] = ..., override_pixel_perfect: bool = ..., vertex_color_always_gamma_space: bool = ..., pixel_perfect: bool = ..., plane_distance: _Optional[float] = ..., override_sorting: bool = ..., sorting_order: _Optional[int] = ..., target_display: _Optional[int] = ..., sorting_layer_id: _Optional[int] = ..., additional_shader_channels: _Optional[int] = ..., sorting_layer_name: _Optional[str] = ..., update_rect_transform_for_standalone: _Optional[_Union[StandaloneRenderResize, str]] = ..., world_camera: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., normalized_sorting_grid_size: _Optional[float] = ...) -> None: ...
