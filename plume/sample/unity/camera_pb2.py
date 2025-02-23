# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plume/sample/unity/camera.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'plume/sample/unity/camera.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from plume.sample.unity import identifiers_pb2 as plume_dot_sample_dot_unity_dot_identifiers__pb2
from plume.sample.unity import rendering_pb2 as plume_dot_sample_dot_unity_dot_rendering__pb2
from plume.sample.common import vector2_pb2 as plume_dot_sample_dot_common_dot_vector2__pb2
from plume.sample.common import vector3_pb2 as plume_dot_sample_dot_common_dot_vector3__pb2
from plume.sample.common import matrix4x4_pb2 as plume_dot_sample_dot_common_dot_matrix4x4__pb2
from plume.sample.common import color_pb2 as plume_dot_sample_dot_common_dot_color__pb2
from plume.sample.common import rect_pb2 as plume_dot_sample_dot_common_dot_rect__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fplume/sample/unity/camera.proto\x12\x12plume.sample.unity\x1a$plume/sample/unity/identifiers.proto\x1a\"plume/sample/unity/rendering.proto\x1a!plume/sample/common/vector2.proto\x1a!plume/sample/common/vector3.proto\x1a#plume/sample/common/matrix4x4.proto\x1a\x1fplume/sample/common/color.proto\x1a\x1eplume/sample/common/rect.proto\"U\n\x0c\x43\x61meraCreate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"V\n\rCameraDestroy\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"\x95\x1c\n\x0c\x43\x61meraUpdate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\x12+\n\x0fnear_clip_plane\x18\x02 \x01(\x02H\x00R\rnearClipPlane\x88\x01\x01\x12)\n\x0e\x66\x61r_clip_plane\x18\x03 \x01(\x02H\x01R\x0c\x66\x61rClipPlane\x88\x01\x01\x12\'\n\rfield_of_view\x18\x04 \x01(\x02H\x02R\x0b\x66ieldOfView\x88\x01\x01\x12M\n\x0erendering_path\x18\x05 \x01(\x0e\x32!.plume.sample.unity.RenderingPathH\x03R\rrenderingPath\x88\x01\x01\x12 \n\tallow_hdr\x18\x06 \x01(\x08H\x04R\x08\x61llowHdr\x88\x01\x01\x12\"\n\nallow_msaa\x18\x07 \x01(\x08H\x05R\tallowMsaa\x88\x01\x01\x12=\n\x18\x61llow_dynamic_resolution\x18\x08 \x01(\x08H\x06R\x16\x61llowDynamicResolution\x88\x01\x01\x12>\n\x19\x66orce_into_render_texture\x18\t \x01(\x08H\x07R\x16\x66orceIntoRenderTexture\x88\x01\x01\x12\x30\n\x11orthographic_size\x18\n \x01(\x02H\x08R\x10orthographicSize\x88\x01\x01\x12\'\n\x0corthographic\x18\x0b \x01(\x08H\tR\x0corthographic\x88\x01\x01\x12Q\n\x10opaque_sort_mode\x18\x0c \x01(\x0e\x32\".plume.sample.unity.OpaqueSortModeH\nR\x0eopaqueSortMode\x88\x01\x01\x12\x63\n\x16transparency_sort_mode\x18\r \x01(\x0e\x32(.plume.sample.unity.TransparencySortModeH\x0bR\x14transparencySortMode\x88\x01\x01\x12W\n\x16transparency_sort_axis\x18\x0e \x01(\x0b\x32\x1c.plume.sample.common.Vector3H\x0cR\x14transparencySortAxis\x88\x01\x01\x12\x19\n\x05\x64\x65pth\x18\x0f \x01(\x02H\rR\x05\x64\x65pth\x88\x01\x01\x12\x1b\n\x06\x61spect\x18\x10 \x01(\x02H\x0eR\x06\x61spect\x88\x01\x01\x12&\n\x0c\x63ulling_mask\x18\x11 \x01(\x05H\x0fR\x0b\x63ullingMask\x88\x01\x01\x12\"\n\nevent_mask\x18\x12 \x01(\x05H\x10R\teventMask\x88\x01\x01\x12\x35\n\x14layer_cull_spherical\x18\x13 \x01(\x08H\x11R\x12layerCullSpherical\x88\x01\x01\x12$\n\x0b\x63\x61mera_type\x18\x14 \x01(\rH\x12R\ncameraType\x88\x01\x01\x12\x63\n\x14layer_cull_distances\x18\x15 \x01(\x0b\x32,.plume.sample.unity.CameraLayerCullDistancesH\x13R\x12layerCullDistances\x88\x01\x01\x12\x37\n\x15use_occlusion_culling\x18\x16 \x01(\x08H\x14R\x13useOcclusionCulling\x88\x01\x01\x12J\n\x0e\x63ulling_matrix\x18\x17 \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H\x15R\rcullingMatrix\x88\x01\x01\x12J\n\x10\x62\x61\x63kground_color\x18\x18 \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x16R\x0f\x62\x61\x63kgroundColor\x88\x01\x01\x12$\n\x0b\x63lear_flags\x18\x19 \x01(\rH\x17R\nclearFlags\x88\x01\x01\x12\x31\n\x12\x64\x65pth_texture_mode\x18\x1a \x01(\rH\x18R\x10\x64\x65pthTextureMode\x88\x01\x01\x12M\n!clear_stencil_after_lighting_pass\x18\x1b \x01(\x08H\x19R\x1d\x63learStencilAfterLightingPass\x88\x01\x01\x12;\n\x17use_physical_properties\x18\x1c \x01(\x08H\x1aR\x15usePhysicalProperties\x88\x01\x01\x12\x42\n\x0bsensor_size\x18\x1d \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x1bR\nsensorSize\x88\x01\x01\x12@\n\nlens_shift\x18\x1e \x01(\x0b\x32\x1c.plume.sample.common.Vector2H\x1cR\tlensShift\x88\x01\x01\x12&\n\x0c\x66ocal_length\x18\x1f \x01(\x02H\x1dR\x0b\x66ocalLength\x88\x01\x01\x12\x45\n\x08gate_fit\x18  \x01(\x0e\x32%.plume.sample.unity.CameraGateFitModeH\x1eR\x07gateFit\x88\x01\x01\x12\x32\n\x04rect\x18! \x01(\x0b\x32\x19.plume.sample.common.RectH\x1fR\x04rect\x88\x01\x01\x12=\n\npixel_rect\x18\" \x01(\x0b\x32\x19.plume.sample.common.RectH R\tpixelRect\x88\x01\x01\x12O\n\x0etarget_texture\x18# \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH!R\rtargetTexture\x88\x01\x01\x12*\n\x0etarget_display\x18$ \x01(\x05H\"R\rtargetDisplay\x88\x01\x01\x12X\n\x16world_to_camera_matrix\x18% \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H#R\x13worldToCameraMatrix\x88\x01\x01\x12P\n\x11projection_matrix\x18& \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H$R\x10projectionMatrix\x88\x01\x01\x12h\n\x1enon_jittered_projection_matrix\x18\' \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H%R\x1bnonJitteredProjectionMatrix\x88\x01\x01\x12y\n8use_jittered_projection_matrix_for_transparent_rendering\x18( \x01(\x08H&R2useJitteredProjectionMatrixForTransparentRendering\x88\x01\x01\x12\x30\n\x11stereo_separation\x18) \x01(\x02H\'R\x10stereoSeparation\x88\x01\x01\x12\x32\n\x12stereo_convergence\x18* \x01(\x02H(R\x11stereoConvergence\x88\x01\x01\x12^\n\x11stereo_target_eye\x18+ \x01(\x0e\x32-.plume.sample.unity.CameraStereoTargetEyeMaskH)R\x0fstereoTargetEye\x88\x01\x01\x42\x12\n\x10_near_clip_planeB\x11\n\x0f_far_clip_planeB\x10\n\x0e_field_of_viewB\x11\n\x0f_rendering_pathB\x0c\n\n_allow_hdrB\r\n\x0b_allow_msaaB\x1b\n\x19_allow_dynamic_resolutionB\x1c\n\x1a_force_into_render_textureB\x14\n\x12_orthographic_sizeB\x0f\n\r_orthographicB\x13\n\x11_opaque_sort_modeB\x19\n\x17_transparency_sort_modeB\x19\n\x17_transparency_sort_axisB\x08\n\x06_depthB\t\n\x07_aspectB\x0f\n\r_culling_maskB\r\n\x0b_event_maskB\x17\n\x15_layer_cull_sphericalB\x0e\n\x0c_camera_typeB\x17\n\x15_layer_cull_distancesB\x18\n\x16_use_occlusion_cullingB\x11\n\x0f_culling_matrixB\x13\n\x11_background_colorB\x0e\n\x0c_clear_flagsB\x15\n\x13_depth_texture_modeB$\n\"_clear_stencil_after_lighting_passB\x1a\n\x18_use_physical_propertiesB\x0e\n\x0c_sensor_sizeB\r\n\x0b_lens_shiftB\x0f\n\r_focal_lengthB\x0b\n\t_gate_fitB\x07\n\x05_rectB\r\n\x0b_pixel_rectB\x11\n\x0f_target_textureB\x11\n\x0f_target_displayB\x19\n\x17_world_to_camera_matrixB\x14\n\x12_projection_matrixB!\n\x1f_non_jittered_projection_matrixB;\n9_use_jittered_projection_matrix_for_transparent_renderingB\x14\n\x12_stereo_separationB\x15\n\x13_stereo_convergenceB\x14\n\x12_stereo_target_eye\"8\n\x18\x43\x61meraLayerCullDistances\x12\x1c\n\tdistances\x18\x01 \x03(\x02R\tdistances*\xbc\x01\n\x11\x43\x61meraGateFitMode\x12\x1d\n\x19\x43\x41MERA_GATE_FIT_MODE_NONE\x10\x00\x12!\n\x1d\x43\x41MERA_GATE_FIT_MODE_VERTICAL\x10\x01\x12#\n\x1f\x43\x41MERA_GATE_FIT_MODE_HORIZONTAL\x10\x02\x12\x1d\n\x19\x43\x41MERA_GATE_FIT_MODE_FILL\x10\x03\x12!\n\x1d\x43\x41MERA_GATE_FIT_MODE_OVERSCAN\x10\x04*\xbc\x01\n\x19\x43\x61meraStereoTargetEyeMask\x12&\n\"CAMERA_STEREO_TARGET_EYE_MASK_NONE\x10\x00\x12&\n\"CAMERA_STEREO_TARGET_EYE_MASK_LEFT\x10\x01\x12\'\n#CAMERA_STEREO_TARGET_EYE_MASK_RIGHT\x10\x02\x12&\n\"CAMERA_STEREO_TARGET_EYE_MASK_BOTH\x10\x03\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plume.sample.unity.camera_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_CAMERAGATEFITMODE']._serialized_start=4143
  _globals['_CAMERAGATEFITMODE']._serialized_end=4331
  _globals['_CAMERASTEREOTARGETEYEMASK']._serialized_start=4334
  _globals['_CAMERASTEREOTARGETEYEMASK']._serialized_end=4522
  _globals['_CAMERACREATE']._serialized_start=301
  _globals['_CAMERACREATE']._serialized_end=386
  _globals['_CAMERADESTROY']._serialized_start=388
  _globals['_CAMERADESTROY']._serialized_end=474
  _globals['_CAMERAUPDATE']._serialized_start=477
  _globals['_CAMERAUPDATE']._serialized_end=4082
  _globals['_CAMERALAYERCULLDISTANCES']._serialized_start=4084
  _globals['_CAMERALAYERCULLDISTANCES']._serialized_end=4140
# @@protoc_insertion_point(module_scope)
