# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/lightmap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14unity/lightmap.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"\x86\x01\n\x0fLightmapsUpdate\x12\x39\n\x0elightmaps_mode\x18\x01 \x01(\x0e\x32!.plume.sample.unity.LightmapsMode\x12\x38\n\x0elightmaps_data\x18\x02 \x03(\x0b\x32 .plume.sample.unity.LightmapData\"\xd7\x02\n\x0cLightmapData\x12K\n\x19lightmap_color_texture_id\x18\x01 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x00\x88\x01\x01\x12I\n\x17lightmap_dir_texture_id\x18\x02 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01\x88\x01\x01\x12Q\n\x1flightmap_shadow_mask_texture_id\x18\x03 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x02\x88\x01\x01\x42\x1c\n\x1a_lightmap_color_texture_idB\x1a\n\x18_lightmap_dir_texture_idB\"\n _lightmap_shadow_mask_texture_id*\\\n\rLightmapsMode\x12\"\n\x1eLIGHTMAPS_MODE_NON_DIRECTIONAL\x10\x00\x12\'\n#LIGHTMAPS_MODE_COMBINED_DIRECTIONAL\x10\x01\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.lightmap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_LIGHTMAPSMODE']._serialized_start=552
  _globals['_LIGHTMAPSMODE']._serialized_end=644
  _globals['_LIGHTMAPSUPDATE']._serialized_start=70
  _globals['_LIGHTMAPSUPDATE']._serialized_end=204
  _globals['_LIGHTMAPDATA']._serialized_start=207
  _globals['_LIGHTMAPDATA']._serialized_end=550
# @@protoc_insertion_point(module_scope)