# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/light.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2
from common import matrix4x4_pb2 as common_dot_matrix4x4__pb2
from common import vector4_pb2 as common_dot_vector4__pb2
from common import color_pb2 as common_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11unity/light.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x16\x63ommon/matrix4x4.proto\x1a\x14\x63ommon/vector4.proto\x1a\x12\x63ommon/color.proto\"B\n\x0bLightCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"C\n\x0cLightDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"\xd7\x0f\n\x0bLightUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x14\n\x07\x65nabled\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x30\n\x04type\x18\x03 \x01(\x0e\x32\x1d.plume.sample.unity.LightTypeH\x01\x88\x01\x01\x12\x32\n\x05shape\x18\x04 \x01(\x0e\x32\x1e.plume.sample.unity.LightShapeH\x02\x88\x01\x01\x12\x16\n\tintensity\x18\x05 \x01(\x02H\x03\x88\x01\x01\x12\x1d\n\x10\x62ounce_intensity\x18\x06 \x01(\x02H\x04\x88\x01\x01\x12\x12\n\x05range\x18\x07 \x01(\x02H\x05\x88\x01\x01\x12.\n\x05\x63olor\x18\x08 \x01(\x0b\x32\x1a.plume.sample.common.ColorH\x06\x88\x01\x01\x12\x1e\n\x11\x63olor_temperature\x18\t \x01(\x02H\x07\x88\x01\x01\x12\"\n\x15use_color_temperature\x18\n \x01(\x08H\x08\x88\x01\x01\x12\x17\n\nspot_angle\x18\x0b \x01(\x02H\t\x88\x01\x01\x12\x1d\n\x10inner_spot_angle\x18\x0c \x01(\x02H\n\x88\x01\x01\x12\x36\n\x07shadows\x18\r \x01(\x0e\x32 .plume.sample.unity.LightShadowsH\x0b\x88\x01\x01\x12\x1c\n\x0fshadow_strength\x18\x0e \x01(\x02H\x0c\x88\x01\x01\x12I\n\x11shadow_resolution\x18\x0f \x01(\x0e\x32).plume.sample.unity.LightShadowResolutionH\r\x88\x01\x01\x12\x43\n\x16shadow_matrix_override\x18\x10 \x01(\x0b\x32\x1e.plume.sample.common.Matrix4x4H\x0e\x88\x01\x01\x12\'\n\x1ause_shadow_matrix_override\x18\x11 \x01(\x08H\x0f\x88\x01\x01\x12\x18\n\x0bshadow_bias\x18\x12 \x01(\x02H\x10\x88\x01\x01\x12\x1f\n\x12shadow_normal_bias\x18\x13 \x01(\x02H\x11\x88\x01\x01\x12\x1e\n\x11shadow_near_plane\x18\x14 \x01(\x02H\x12\x88\x01\x01\x12\x34\n\'use_view_frustum_for_shadow_caster_cull\x18\x15 \x01(\x08H\x13\x88\x01\x01\x12V\n\x1blayer_shadow_cull_distances\x18\x16 \x01(\x0b\x32,.plume.sample.unity.LayerShadowCullDistancesH\x14\x88\x01\x01\x12%\n\x18shadow_custom_resolution\x18\x17 \x01(\x05H\x15\x88\x01\x01\x12P\n\x18light_shadow_caster_mode\x18\x18 \x01(\x0e\x32).plume.sample.unity.LightShadowCasterModeH\x16\x88\x01\x01\x12!\n\x14rendering_layer_mask\x18\x19 \x01(\x05H\x17\x88\x01\x01\x12\x19\n\x0c\x63ulling_mask\x18\x1a \x01(\x05H\x18\x88\x01\x01\x12\x43\n\x18\x62ounding_sphere_override\x18\x1b \x01(\x0b\x32\x1c.plume.sample.common.Vector4H\x19\x88\x01\x01\x12)\n\x1cuse_bounding_sphere_override\x18\x1c \x01(\x08H\x1a\x88\x01\x01\x12;\n\tcookie_id\x18\x1d \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x1b\x88\x01\x01\x12\x18\n\x0b\x63ookie_size\x18\x1e \x01(\x02H\x1c\x88\x01\x01\x12:\n\x08\x66lare_id\x18\x1f \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x1d\x88\x01\x01\x42\n\n\x08_enabledB\x07\n\x05_typeB\x08\n\x06_shapeB\x0c\n\n_intensityB\x13\n\x11_bounce_intensityB\x08\n\x06_rangeB\x08\n\x06_colorB\x14\n\x12_color_temperatureB\x18\n\x16_use_color_temperatureB\r\n\x0b_spot_angleB\x13\n\x11_inner_spot_angleB\n\n\x08_shadowsB\x12\n\x10_shadow_strengthB\x14\n\x12_shadow_resolutionB\x19\n\x17_shadow_matrix_overrideB\x1d\n\x1b_use_shadow_matrix_overrideB\x0e\n\x0c_shadow_biasB\x15\n\x13_shadow_normal_biasB\x14\n\x12_shadow_near_planeB*\n(_use_view_frustum_for_shadow_caster_cullB\x1e\n\x1c_layer_shadow_cull_distancesB\x1b\n\x19_shadow_custom_resolutionB\x1b\n\x19_light_shadow_caster_modeB\x17\n\x15_rendering_layer_maskB\x0f\n\r_culling_maskB\x1b\n\x19_bounding_sphere_overrideB\x1f\n\x1d_use_bounding_sphere_overrideB\x0c\n\n_cookie_idB\x0e\n\x0c_cookie_sizeB\x0b\n\t_flare_id\"-\n\x18LayerShadowCullDistances\x12\x11\n\tdistances\x18\x01 \x03(\x02*\x96\x01\n\tLightType\x12\x13\n\x0fLIGHT_TYPE_SPOT\x10\x00\x12\x1a\n\x16LIGHT_TYPE_DIRECTIONAL\x10\x01\x12\x14\n\x10LIGHT_TYPE_POINT\x10\x02\x12\x13\n\x0fLIGHT_TYPE_AREA\x10\x03\x12\x18\n\x14LIGHT_TYPE_RECTANGLE\x10\x04\x12\x13\n\x0fLIGHT_TYPE_DISC\x10\x05*P\n\nLightShape\x12\x14\n\x10LIGHT_SHAPE_CONE\x10\x00\x12\x17\n\x13LIGHT_SHAPE_PYRAMID\x10\x01\x12\x13\n\x0fLIGHT_SHAPE_BOX\x10\x02*\x99\x01\n\x15LightShadowCasterMode\x12$\n LIGHT_SHADOW_CASTER_MODE_DEFAULT\x10\x00\x12\x31\n-LIGHT_SHADOW_CASTER_MODE_NON_LIGHTMAPPED_ONLY\x10\x01\x12\'\n#LIGHT_SHADOW_CASTER_MODE_EVERYTHING\x10\x02*\xd8\x01\n\x15LightShadowResolution\x12\x31\n-LIGHT_SHADOW_RESOLUTION_FROM_QUALITY_SETTINGS\x10\x00\x12\x1f\n\x1bLIGHT_SHADOW_RESOLUTION_LOW\x10\x01\x12\"\n\x1eLIGHT_SHADOW_RESOLUTION_MEDIUM\x10\x02\x12 \n\x1cLIGHT_SHADOW_RESOLUTION_HIGH\x10\x03\x12%\n!LIGHT_SHADOW_RESOLUTION_VERY_HIGH\x10\x04*V\n\x0cLightShadows\x12\x16\n\x12LIGHT_SHADOWS_NONE\x10\x00\x12\x16\n\x12LIGHT_SHADOWS_HARD\x10\x01\x12\x16\n\x12LIGHT_SHADOWS_SOFT\x10\x02\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.light_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_LIGHTTYPE']._serialized_start=2327
  _globals['_LIGHTTYPE']._serialized_end=2477
  _globals['_LIGHTSHAPE']._serialized_start=2479
  _globals['_LIGHTSHAPE']._serialized_end=2559
  _globals['_LIGHTSHADOWCASTERMODE']._serialized_start=2562
  _globals['_LIGHTSHADOWCASTERMODE']._serialized_end=2715
  _globals['_LIGHTSHADOWRESOLUTION']._serialized_start=2718
  _globals['_LIGHTSHADOWRESOLUTION']._serialized_end=2934
  _globals['_LIGHTSHADOWS']._serialized_start=2936
  _globals['_LIGHTSHADOWS']._serialized_end=3022
  _globals['_LIGHTCREATE']._serialized_start=132
  _globals['_LIGHTCREATE']._serialized_end=198
  _globals['_LIGHTDESTROY']._serialized_start=200
  _globals['_LIGHTDESTROY']._serialized_end=267
  _globals['_LIGHTUPDATE']._serialized_start=270
  _globals['_LIGHTUPDATE']._serialized_end=2277
  _globals['_LAYERSHADOWCULLDISTANCES']._serialized_start=2279
  _globals['_LAYERSHADOWCULLDISTANCES']._serialized_end=2324
# @@protoc_insertion_point(module_scope)
