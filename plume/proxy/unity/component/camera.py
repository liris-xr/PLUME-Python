from __future__ import annotations

from plume.sample.unity.camera_pb2 import (
    CameraGateFitMode as CameraGateFitModeSample,
    CameraStereoTargetEyeMask as CameraStereoTargetEyeMaskSample,
)

from plume.proxy.unity.component import Component
from plume.proxy.unity.game_object import GameObject
from plume.proxy.common.vector2 import Vector2
from plume.proxy.common.vector3 import Vector3
from plume.proxy.common.matrix4x4 import Matrix4x4
from plume.proxy.common.color import Color
from plume.proxy.common.rect import Rect
from plume.proxy.unity.asset import Asset

from typing import Union, Optional, List
from uuid import UUID

from enum import Enum


class CameraGateFitMode(Enum):
    UNSPECIFIED = 0
    NONE = 1
    VERTICAL = 2
    HORIZONTAL = 3
    FILL = 4
    OVERSCAN = 5

    @staticmethod
    def from_message(gate_fit: CameraGateFitModeSample):
        if gate_fit == CameraGateFitModeSample.CAMERA_GATE_FIT_MODE_NONE:
            return CameraGateFitMode.NONE
        elif gate_fit == CameraGateFitModeSample.CAMERA_GATE_FIT_MODE_VERTICAL:
            return CameraGateFitMode.VERTICAL
        elif (
            gate_fit == CameraGateFitModeSample.CAMERA_GATE_FIT_MODE_HORIZONTAL
        ):
            return CameraGateFitMode.HORIZONTAL
        elif gate_fit == CameraGateFitModeSample.CAMERA_GATE_FIT_MODE_FILL:
            return CameraGateFitMode.FILL
        elif gate_fit == CameraGateFitModeSample.CAMERA_GATE_FIT_MODE_OVERSCAN:
            return CameraGateFitMode.OVERSCAN
        else:
            return CameraGateFitMode.UNSPECIFIED


class CameraStereoTargetEyeMask(Enum):
    UNSPECIFIED = 0
    NONE = 1
    LEFT = 2
    RIGHT = 3
    BOTH = 4

    @staticmethod
    def from_message(stereo_target_eye_mask: CameraStereoTargetEyeMaskSample):
        if (
            stereo_target_eye_mask
            == CameraStereoTargetEyeMaskSample.CAMERA_STEREO_TARGET_EYE_MASK_NONE
        ):
            return CameraStereoTargetEyeMask.NONE
        elif (
            stereo_target_eye_mask
            == CameraStereoTargetEyeMaskSample.CAMERA_STEREO_TARGET_EYE_MASK_LEFT
        ):
            return CameraStereoTargetEyeMask.LEFT
        elif (
            stereo_target_eye_mask
            == CameraStereoTargetEyeMaskSample.CAMERA_STEREO_TARGET_EYE_MASK_RIGHT
        ):
            return CameraStereoTargetEyeMask.RIGHT
        elif (
            stereo_target_eye_mask
            == CameraStereoTargetEyeMaskSample.CAMERA_STEREO_TARGET_EYE_MASK_BOTH
        ):
            return CameraStereoTargetEyeMask.BOTH
        else:
            return CameraStereoTargetEyeMask.UNSPECIFIED


class Camera(Component):
    _near_clip_plane: float
    _far_clip_plane: float
    _field_of_view: float
    _rendering_path: int
    _allow_hdr: bool
    _allow_msaa: bool
    _allow_dynamic_resolution: bool
    _force_into_render_texture: bool
    _orthographic_size: float
    _orthographic: bool
    _opaque_sort_mode: int
    _transparency_sort_mode: int
    _transparency_sort_axis: Vector3
    _depth: float
    _aspect: float
    _culling_mask: int
    _event_mask: int
    _layer_cull_spherical: bool
    _camera_type: int
    _layer_cull_distances: List[float]
    _use_occlusion_culling: bool
    _culling_matrix: Matrix4x4
    _background_color: Color
    _clear_flags: int
    _depth_texture_mode: int
    _clear_stencil_after_lighting_pass: bool
    _use_physical_properties: bool
    _sensor_size: Vector2
    _lens_shift: Vector2
    _focal_length: float
    _gate_fit: CameraGateFitMode
    _rect: Rect
    _pixel_rect: Rect
    _target_texture: Optional[Asset]
    _target_display: int
    _world_to_camera_matrix: Matrix4x4
    _projection_matrix: Matrix4x4
    _non_jittered_projection_matrix: Matrix4x4
    _use_jittered_projection_matrix_for_transparent_rendering: bool
    _stereo_separation: float
    _stereo_convergence: float
    _stereo_target_eye: CameraStereoTargetEyeMask

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        near_clip_plane: float = 0.3,
        far_clip_plane: float = 1000.0,
        field_of_view: float = 60.0,
        rendering_path: int = 0,
        allow_hdr: bool = True,
        allow_msaa: bool = True,
        allow_dynamic_resolution: bool = False,
        force_into_render_texture: bool = False,
        orthographic_size: float = 5.0,
        orthographic: bool = False,
        opaque_sort_mode: int = 0,
        transparency_sort_mode: int = 0,
        transparency_sort_axis: Optional[Vector3] = None,
        depth: float = 0.0,
        aspect: float = 16 / 9,
        culling_mask: int = -1,
        event_mask: int = -1,
        layer_cull_spherical: bool = False,
        camera_type: int = 0,
        layer_cull_distances: Optional[List[float]] = None,
        use_occlusion_culling: bool = True,
        culling_matrix: Optional[Matrix4x4] = None,
        background_color: Optional[Color] = None,
        clear_flags: int = 0,
        depth_texture_mode: int = 0,
        clear_stencil_after_lighting_pass: bool = True,
        use_physical_properties: bool = False,
        sensor_size: Optional[Vector2] = None,
        lens_shift: Optional[Vector2] = None,
        focal_length: float = 50.0,
        gate_fit: CameraGateFitMode = CameraGateFitMode.NONE,
        rect: Optional[Rect] = None,
        pixel_rect: Optional[Rect] = None,
        target_texture: Optional[Asset] = None,
        target_display: int = 0,
        world_to_camera_matrix: Optional[Matrix4x4] = None,
        projection_matrix: Optional[Matrix4x4] = None,
        non_jittered_projection_matrix: Optional[Matrix4x4] = None,
        use_jittered_projection_matrix_for_transparent_rendering: bool = True,
        stereo_separation: float = 0.064,
        stereo_convergence: float = 1.0,
        stereo_target_eye: int = CameraStereoTargetEyeMask.BOTH,
    ):
        super().__init__(guid, game_object)
        self._near_clip_plane = near_clip_plane
        self._far_clip_plane = far_clip_plane
        self._field_of_view = field_of_view
        self._rendering_path = rendering_path
        self._allow_hdr = allow_hdr
        self._allow_msaa = allow_msaa
        self._allow_dynamic_resolution = allow_dynamic_resolution
        self._force_into_render_texture = force_into_render_texture
        self._orthographic_size = orthographic_size
        self._orthographic = orthographic
        self._opaque_sort_mode = opaque_sort_mode
        self._transparency_sort_mode = transparency_sort_mode
        self._transparency_sort_axis = transparency_sort_axis
        self._depth = depth
        self._aspect = aspect
        self._culling_mask = culling_mask
        self._event_mask = event_mask
        self._layer_cull_spherical = layer_cull_spherical
        self._camera_type = camera_type
        self._layer_cull_distances = (
            layer_cull_distances if layer_cull_distances else []
        )
        self._use_occlusion_culling = use_occlusion_culling
        self._culling_matrix = culling_matrix
        self._background_color = (
            background_color
            if background_color
            else Color(0.1921569, 0.3019608, 0.4745098, 0)
        )
        self._clear_flags = clear_flags
        self._depth_texture_mode = depth_texture_mode
        self._clear_stencil_after_lighting_pass = (
            clear_stencil_after_lighting_pass
        )
        self._use_physical_properties = use_physical_properties
        self._sensor_size = sensor_size
        self._lens_shift = lens_shift
        self._focal_length = focal_length
        self._gate_fit = gate_fit
        self._rect = rect
        self._pixel_rect = pixel_rect
        self._target_texture = target_texture
        self._target_display = target_display
        self._world_to_camera_matrix = (
            world_to_camera_matrix if world_to_camera_matrix else Matrix4x4()
        )
        self._projection_matrix = (
            projection_matrix if projection_matrix else Matrix4x4()
        )
        self._non_jittered_projection_matrix = (
            non_jittered_projection_matrix
            if non_jittered_projection_matrix
            else Matrix4x4()
        )
        self._use_jittered_projection_matrix_for_transparent_rendering = (
            use_jittered_projection_matrix_for_transparent_rendering
        )
        self._stereo_separation = stereo_separation
        self._stereo_convergence = stereo_convergence
        self._stereo_target_eye = stereo_target_eye

    # Properties for all fields
    @property
    def near_clip_plane(self) -> float:
        return self._near_clip_plane

    @property
    def far_clip_plane(self) -> float:
        return self._far_clip_plane

    @property
    def field_of_view(self) -> float:
        return self._field_of_view

    @property
    def rendering_path(self) -> int:
        return self._rendering_path

    @property
    def allow_hdr(self) -> bool:
        return self._allow_hdr

    @property
    def allow_msaa(self) -> bool:
        return self._allow_msaa

    @property
    def allow_dynamic_resolution(self) -> bool:
        return self._allow_dynamic_resolution

    @property
    def force_into_render_texture(self) -> bool:
        return self._force_into_render_texture

    @property
    def orthographic_size(self) -> float:
        return self._orthographic_size

    @property
    def orthographic(self) -> bool:
        return self._orthographic

    @property
    def opaque_sort_mode(self) -> int:
        return self._opaque_sort_mode

    @property
    def transparency_sort_mode(self) -> int:
        return self._transparency_sort_mode

    @property
    def transparency_sort_axis(self) -> Vector3:
        return self._transparency_sort_axis

    @property
    def depth(self) -> float:
        return self._depth

    @property
    def aspect(self) -> float:
        return self._aspect

    @property
    def culling_mask(self) -> int:
        return self._culling_mask

    @property
    def event_mask(self) -> int:
        return self._event_mask

    @property
    def layer_cull_spherical(self) -> bool:
        return self._layer_cull_spherical

    @property
    def camera_type(self) -> int:
        return self._camera_type

    @property
    def layer_cull_distances(self) -> List[float]:
        return self._layer_cull_distances

    @property
    def use_occlusion_culling(self) -> bool:
        return self._use_occlusion_culling

    @property
    def culling_matrix(self) -> Matrix4x4:
        return self._culling_matrix

    @property
    def background_color(self) -> Color:
        return self._background_color

    @property
    def clear_flags(self) -> int:
        return self._clear_flags

    @property
    def depth_texture_mode(self) -> int:
        return self._depth_texture_mode

    @property
    def clear_stencil_after_lighting_pass(self) -> bool:
        return self._clear_stencil_after_lighting_pass

    @property
    def use_physical_properties(self) -> bool:
        return self._use_physical_properties

    @property
    def sensor_size(self) -> Vector2:
        return self._sensor_size

    @property
    def lens_shift(self) -> Vector2:
        return self._lens_shift

    @property
    def focal_length(self) -> float:
        return self._focal_length

    @property
    def gate_fit(self) -> CameraGateFitMode:
        return self._gate_fit

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def pixel_rect(self) -> Rect:
        return self._pixel_rect

    @property
    def target_texture(self) -> Optional[Asset]:
        return self._target_texture

    @property
    def target_display(self) -> int:
        return self._target_display

    @property
    def world_to_camera_matrix(self) -> Matrix4x4:
        return self._world_to_camera_matrix

    @property
    def projection_matrix(self) -> Matrix4x4:
        return self._projection_matrix

    @property
    def non_jittered_projection_matrix(self) -> Matrix4x4:
        return self._non_jittered_projection_matrix

    @property
    def use_jittered_projection_matrix_for_transparent_rendering(self) -> bool:
        return self._use_jittered_projection_matrix_for_transparent_rendering

    @property
    def stereo_separation(self) -> float:
        return self._stereo_separation

    @property
    def stereo_convergence(self) -> float:
        return self._stereo_convergence

    @property
    def stereo_target_eye(self) -> CameraStereoTargetEyeMask:
        return self._stereo_target_eye

    def __repr__(self):
        return (
            f"Camera(guid={self.guid}, "
            f"near_clip_plane={self._near_clip_plane}, "
            f"far_clip_plane={self._far_clip_plane}, "
            f"field_of_view={self._field_of_view}, "
            # Adding a few key properties for brevity
            f"orthographic={self._orthographic}, "
            f"depth={self._depth})"
        )
