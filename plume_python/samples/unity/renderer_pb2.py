# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/renderer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2
from common import bounds_pb2 as common_dot_bounds__pb2
from common import vector4_pb2 as common_dot_vector4__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14unity/renderer.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\x1a\x13\x63ommon/bounds.proto\x1a\x14\x63ommon/vector4.proto\"\xff\x04\n\x0eRendererUpdate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\x12\x14\n\x07\x65nabled\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x44\n\tmaterials\x18\x03 \x01(\x0b\x32,.plume.sample.unity.RendererUpdate.MaterialsH\x01\x88\x01\x01\x12\x36\n\x0clocal_bounds\x18\x04 \x01(\x0b\x32\x1b.plume.sample.common.BoundsH\x02\x88\x01\x01\x12\x1b\n\x0elightmap_index\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12@\n\x15lightmap_scale_offset\x18\x06 \x01(\x0b\x32\x1c.plume.sample.common.Vector4H\x04\x88\x01\x01\x12$\n\x17realtime_lightmap_index\x18\x07 \x01(\x05H\x05\x88\x01\x01\x12I\n\x1erealtime_lightmap_scale_offset\x18\x08 \x01(\x0b\x32\x1c.plume.sample.common.Vector4H\x06\x88\x01\x01\x1a=\n\tMaterials\x12\x30\n\x03ids\x18\x01 \x03(\x0b\x32#.plume.sample.unity.AssetIdentifierB\n\n\x08_enabledB\x0c\n\n_materialsB\x0f\n\r_local_boundsB\x11\n\x0f_lightmap_indexB\x18\n\x16_lightmap_scale_offsetB\x1a\n\x18_realtime_lightmap_indexB!\n\x1f_realtime_lightmap_scale_offsetB\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.renderer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_RENDERERUPDATE']._serialized_start=113
  _globals['_RENDERERUPDATE']._serialized_end=752
  _globals['_RENDERERUPDATE_MATERIALS']._serialized_start=540
  _globals['_RENDERERUPDATE_MATERIALS']._serialized_end=601
# @@protoc_insertion_point(module_scope)
