from unity import identifiers_pb2 as _identifiers_pb2
from unity import rendering_pb2 as _rendering_pb2
from common import vector2_pb2 as _vector2_pb2
from common import vector3_pb2 as _vector3_pb2
from common import matrix4x4_pb2 as _matrix4x4_pb2
from common import color_pb2 as _color_pb2
from common import rect_pb2 as _rect_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraGateFitMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CAMERA_GATE_FIT_MODE_NONE: _ClassVar[CameraGateFitMode]
    CAMERA_GATE_FIT_MODE_VERTICAL: _ClassVar[CameraGateFitMode]
    CAMERA_GATE_FIT_MODE_HORIZONTAL: _ClassVar[CameraGateFitMode]
    CAMERA_GATE_FIT_MODE_FILL: _ClassVar[CameraGateFitMode]
    CAMERA_GATE_FIT_MODE_OVERSCAN: _ClassVar[CameraGateFitMode]

class CameraStereoTargetEyeMask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CAMERA_STEREO_TARGET_EYE_MASK_NONE: _ClassVar[CameraStereoTargetEyeMask]
    CAMERA_STEREO_TARGET_EYE_MASK_LEFT: _ClassVar[CameraStereoTargetEyeMask]
    CAMERA_STEREO_TARGET_EYE_MASK_RIGHT: _ClassVar[CameraStereoTargetEyeMask]
    CAMERA_STEREO_TARGET_EYE_MASK_BOTH: _ClassVar[CameraStereoTargetEyeMask]
CAMERA_GATE_FIT_MODE_NONE: CameraGateFitMode
CAMERA_GATE_FIT_MODE_VERTICAL: CameraGateFitMode
CAMERA_GATE_FIT_MODE_HORIZONTAL: CameraGateFitMode
CAMERA_GATE_FIT_MODE_FILL: CameraGateFitMode
CAMERA_GATE_FIT_MODE_OVERSCAN: CameraGateFitMode
CAMERA_STEREO_TARGET_EYE_MASK_NONE: CameraStereoTargetEyeMask
CAMERA_STEREO_TARGET_EYE_MASK_LEFT: CameraStereoTargetEyeMask
CAMERA_STEREO_TARGET_EYE_MASK_RIGHT: CameraStereoTargetEyeMask
CAMERA_STEREO_TARGET_EYE_MASK_BOTH: CameraStereoTargetEyeMask

class CameraCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CameraDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CameraUpdate(_message.Message):
    __slots__ = ["id", "near_clip_plane", "far_clip_plane", "field_of_view", "rendering_path", "allow_hdr", "allow_msaa", "allow_dynamic_resolution", "force_into_render_texture", "orthographic_size", "orthographic", "opaque_sort_mode", "transparency_sort_mode", "transparency_sort_axis", "depth", "aspect", "culling_mask", "event_mask", "layer_cull_spherical", "camera_type", "layer_cull_distances", "use_occlusion_culling", "culling_matrix", "background_color", "clear_flags", "depth_texture_mode", "clear_stencil_after_lighting_pass", "use_physical_properties", "sensor_size", "lens_shift", "focal_length", "gate_fit", "rect", "pixel_rect", "target_texture_id", "target_display", "world_to_camera_matrix", "projection_matrix", "non_jittered_projection_matrix", "use_jittered_projection_matrix_for_transparent_rendering", "stereo_separation", "stereo_convergence", "stereo_target_eye"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NEAR_CLIP_PLANE_FIELD_NUMBER: _ClassVar[int]
    FAR_CLIP_PLANE_FIELD_NUMBER: _ClassVar[int]
    FIELD_OF_VIEW_FIELD_NUMBER: _ClassVar[int]
    RENDERING_PATH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_HDR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MSAA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DYNAMIC_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FORCE_INTO_RENDER_TEXTURE_FIELD_NUMBER: _ClassVar[int]
    ORTHOGRAPHIC_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORTHOGRAPHIC_FIELD_NUMBER: _ClassVar[int]
    OPAQUE_SORT_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENCY_SORT_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENCY_SORT_AXIS_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    ASPECT_FIELD_NUMBER: _ClassVar[int]
    CULLING_MASK_FIELD_NUMBER: _ClassVar[int]
    EVENT_MASK_FIELD_NUMBER: _ClassVar[int]
    LAYER_CULL_SPHERICAL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAYER_CULL_DISTANCES_FIELD_NUMBER: _ClassVar[int]
    USE_OCCLUSION_CULLING_FIELD_NUMBER: _ClassVar[int]
    CULLING_MATRIX_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DEPTH_TEXTURE_MODE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_STENCIL_AFTER_LIGHTING_PASS_FIELD_NUMBER: _ClassVar[int]
    USE_PHYSICAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SENSOR_SIZE_FIELD_NUMBER: _ClassVar[int]
    LENS_SHIFT_FIELD_NUMBER: _ClassVar[int]
    FOCAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GATE_FIT_FIELD_NUMBER: _ClassVar[int]
    RECT_FIELD_NUMBER: _ClassVar[int]
    PIXEL_RECT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEXTURE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    WORLD_TO_CAMERA_MATRIX_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    NON_JITTERED_PROJECTION_MATRIX_FIELD_NUMBER: _ClassVar[int]
    USE_JITTERED_PROJECTION_MATRIX_FOR_TRANSPARENT_RENDERING_FIELD_NUMBER: _ClassVar[int]
    STEREO_SEPARATION_FIELD_NUMBER: _ClassVar[int]
    STEREO_CONVERGENCE_FIELD_NUMBER: _ClassVar[int]
    STEREO_TARGET_EYE_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    near_clip_plane: float
    far_clip_plane: float
    field_of_view: float
    rendering_path: _rendering_pb2.RenderingPath
    allow_hdr: bool
    allow_msaa: bool
    allow_dynamic_resolution: bool
    force_into_render_texture: bool
    orthographic_size: float
    orthographic: bool
    opaque_sort_mode: _rendering_pb2.OpaqueSortMode
    transparency_sort_mode: _rendering_pb2.TransparencySortMode
    transparency_sort_axis: _vector3_pb2.Vector3
    depth: float
    aspect: float
    culling_mask: int
    event_mask: int
    layer_cull_spherical: bool
    camera_type: int
    layer_cull_distances: CameraLayerCullDistances
    use_occlusion_culling: bool
    culling_matrix: _matrix4x4_pb2.Matrix4x4
    background_color: _color_pb2.Color
    clear_flags: int
    depth_texture_mode: int
    clear_stencil_after_lighting_pass: bool
    use_physical_properties: bool
    sensor_size: _vector2_pb2.Vector2
    lens_shift: _vector2_pb2.Vector2
    focal_length: float
    gate_fit: CameraGateFitMode
    rect: _rect_pb2.Rect
    pixel_rect: _rect_pb2.Rect
    target_texture_id: _identifiers_pb2.AssetIdentifier
    target_display: int
    world_to_camera_matrix: _matrix4x4_pb2.Matrix4x4
    projection_matrix: _matrix4x4_pb2.Matrix4x4
    non_jittered_projection_matrix: _matrix4x4_pb2.Matrix4x4
    use_jittered_projection_matrix_for_transparent_rendering: bool
    stereo_separation: float
    stereo_convergence: float
    stereo_target_eye: CameraStereoTargetEyeMask
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., near_clip_plane: _Optional[float] = ..., far_clip_plane: _Optional[float] = ..., field_of_view: _Optional[float] = ..., rendering_path: _Optional[_Union[_rendering_pb2.RenderingPath, str]] = ..., allow_hdr: bool = ..., allow_msaa: bool = ..., allow_dynamic_resolution: bool = ..., force_into_render_texture: bool = ..., orthographic_size: _Optional[float] = ..., orthographic: bool = ..., opaque_sort_mode: _Optional[_Union[_rendering_pb2.OpaqueSortMode, str]] = ..., transparency_sort_mode: _Optional[_Union[_rendering_pb2.TransparencySortMode, str]] = ..., transparency_sort_axis: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., depth: _Optional[float] = ..., aspect: _Optional[float] = ..., culling_mask: _Optional[int] = ..., event_mask: _Optional[int] = ..., layer_cull_spherical: bool = ..., camera_type: _Optional[int] = ..., layer_cull_distances: _Optional[_Union[CameraLayerCullDistances, _Mapping]] = ..., use_occlusion_culling: bool = ..., culling_matrix: _Optional[_Union[_matrix4x4_pb2.Matrix4x4, _Mapping]] = ..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., clear_flags: _Optional[int] = ..., depth_texture_mode: _Optional[int] = ..., clear_stencil_after_lighting_pass: bool = ..., use_physical_properties: bool = ..., sensor_size: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., lens_shift: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., focal_length: _Optional[float] = ..., gate_fit: _Optional[_Union[CameraGateFitMode, str]] = ..., rect: _Optional[_Union[_rect_pb2.Rect, _Mapping]] = ..., pixel_rect: _Optional[_Union[_rect_pb2.Rect, _Mapping]] = ..., target_texture_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., target_display: _Optional[int] = ..., world_to_camera_matrix: _Optional[_Union[_matrix4x4_pb2.Matrix4x4, _Mapping]] = ..., projection_matrix: _Optional[_Union[_matrix4x4_pb2.Matrix4x4, _Mapping]] = ..., non_jittered_projection_matrix: _Optional[_Union[_matrix4x4_pb2.Matrix4x4, _Mapping]] = ..., use_jittered_projection_matrix_for_transparent_rendering: bool = ..., stereo_separation: _Optional[float] = ..., stereo_convergence: _Optional[float] = ..., stereo_target_eye: _Optional[_Union[CameraStereoTargetEyeMask, str]] = ...) -> None: ...

class CameraLayerCullDistances(_message.Message):
    __slots__ = ["distances"]
    DISTANCES_FIELD_NUMBER: _ClassVar[int]
    distances: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, distances: _Optional[_Iterable[float]] = ...) -> None: ...
