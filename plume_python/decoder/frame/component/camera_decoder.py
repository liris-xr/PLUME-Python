from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.camera_pb2 import (
    CameraCreate,
    CameraUpdate,
    CameraDestroy,
)

from plume_python.proxy.common.rect import Rect
from plume_python.proxy.common.color import Color
from plume_python.proxy.common.vector2 import Vector2
from plume_python.proxy.common.vector3 import Vector3
from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component.camera import (
    Camera,
    CameraGateFitMode,
    CameraStereoTargetEyeMask,
)
from plume_python.decoder.frame.frame_decoder import (
    get_or_create_component,
    get_or_create_asset,
    destroy_component,
)


@register_frame_data_decoder(CameraCreate)
class CameraCreateDecoder(FrameDataDecoder[CameraCreate]):
    def decode(self, frame: Frame, data: CameraCreate) -> Frame:
        get_or_create_component(frame, data.component, Camera)


@register_frame_data_decoder(CameraUpdate)
class CameraUpdateDecoder(FrameDataDecoder[CameraUpdate]):
    def decode(self, frame: Frame, data: CameraUpdate):
        camera = get_or_create_component(frame, data.component, Camera)

        if data.HasField("near_clip_plane"):
            camera._near_clip_plane = data.near_clip_plane
        if data.HasField("far_clip_plane"):
            camera._far_clip_plane = data.far_clip_plane
        if data.HasField("field_of_view"):
            camera._field_of_view = data.field_of_view
        if data.HasField("rendering_path"):
            camera._rendering_path = data.rendering_path
        if data.HasField("allow_hdr"):
            camera._allow_hdr = data.allow_hdr
        if data.HasField("allow_msaa"):
            camera._allow_msaa = data.allow_msaa
        if data.HasField("allow_dynamic_resolution"):
            camera._allow_dynamic_resolution = data.allow_dynamic_resolution
        if data.HasField("force_into_render_texture"):
            camera._force_into_render_texture = data.force_into_render_texture
        if data.HasField("orthographic_size"):
            camera._orthographic_size = data.orthographic_size
        if data.HasField("orthographic"):
            camera._orthographic = data.orthographic
        if data.HasField("opaque_sort_mode"):
            camera._opaque_sort_mode = data.opaque_sort_mode
        if data.HasField("transparency_sort_mode"):
            camera._transparency_sort_mode = data.transparency_sort_mode
        if data.HasField("transparency_sort_axis"):
            camera._transparency_sort_axis = Vector3(
                x=data.transparency_sort_axis.x,
                y=data.transparency_sort_axis.y,
                z=data.transparency_sort_axis.z,
            )
        if data.HasField("depth"):
            camera._depth = data.depth
        if data.HasField("aspect"):
            camera._aspect = data.aspect
        if data.HasField("culling_mask"):
            camera._culling_mask = data.culling_mask
        if data.HasField("event_mask"):
            camera._event_mask = data.event_mask
        if data.HasField("layer_cull_spherical"):
            camera._layer_cull_spherical = data.layer_cull_spherical
        if data.HasField("camera_type"):
            camera._camera_type = data.camera_type
        if data.HasField("layer_cull_distances"):
            camera._layer_cull_distances = data.layer_cull_distances.distances
        if data.HasField("use_occlusion_culling"):
            camera._use_occlusion_culling = data.use_occlusion_culling
        if data.HasField("culling_matrix"):
            # Assuming Matrix4x4 has similar structure as the original
            camera._culling_matrix = data.culling_matrix
        if data.HasField("background_color"):
            camera._background_color = Color(
                r=data.background_color.r,
                g=data.background_color.g,
                b=data.background_color.b,
                a=data.background_color.a,
            )
        if data.HasField("clear_flags"):
            camera._clear_flags = data.clear_flags
        if data.HasField("depth_texture_mode"):
            camera._depth_texture_mode = data.depth_texture_mode
        if data.HasField("clear_stencil_after_lighting_pass"):
            camera._clear_stencil_after_lighting_pass = (
                data.clear_stencil_after_lighting_pass
            )
        if data.HasField("use_physical_properties"):
            camera._use_physical_properties = data.use_physical_properties
        if data.HasField("sensor_size"):
            camera._sensor_size = Vector2(
                x=data.sensor_size.x,
                y=data.sensor_size.y,
            )
        if data.HasField("lens_shift"):
            camera._lens_shift = Vector2(
                x=data.lens_shift.x,
                y=data.lens_shift.y,
            )
        if data.HasField("focal_length"):
            camera._focal_length = data.focal_length
        if data.HasField("gate_fit"):
            camera._gate_fit = CameraGateFitMode.from_message(data.gate_fit)
        if data.HasField("rect"):
            camera._rect = Rect(
                x=data.rect.x,
                y=data.rect.y,
                width=data.rect.width,
                height=data.rect.height,
            )
        if data.HasField("pixel_rect"):
            camera._pixel_rect = Rect(
                x=data.pixel_rect.x,
                y=data.pixel_rect.y,
                width=data.pixel_rect.width,
                height=data.pixel_rect.height,
            )
        if data.HasField("target_texture"):
            camera._target_texture = get_or_create_asset(frame, data.target_texture)
        if data.HasField("target_display"):
            camera._target_display = data.target_display
        if data.HasField("world_to_camera_matrix"):
            camera._world_to_camera_matrix = data.world_to_camera_matrix
        if data.HasField("projection_matrix"):
            camera._projection_matrix = data.projection_matrix
        if data.HasField("non_jittered_projection_matrix"):
            camera._non_jittered_projection_matrix = data.non_jittered_projection_matrix
        if data.HasField("use_jittered_projection_matrix_for_transparent_rendering"):
            camera._use_jittered_projection_matrix_for_transparent_rendering = (
                data.use_jittered_projection_matrix_for_transparent_rendering
            )
        if data.HasField("stereo_separation"):
            camera._stereo_separation = data.stereo_separation
        if data.HasField("stereo_convergence"):
            camera._stereo_convergence = data.stereo_convergence
        if data.HasField("stereo_target_eye"):
            camera._stereo_target_eye = CameraStereoTargetEyeMask.from_message(
                data.stereo_target_eye
            )


@register_frame_data_decoder(CameraDestroy)
class CameraDestroyDecoder(FrameDataDecoder[CameraDestroy]):
    def decode(self, frame: Frame, data: CameraDestroy):
        destroy_component(frame, data.component)
