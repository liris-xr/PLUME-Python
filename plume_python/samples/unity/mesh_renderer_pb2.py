# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unity/mesh_renderer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from unity import identifiers_pb2 as unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19unity/mesh_renderer.proto\x12\x12plume.sample.unity\x1a\x17unity/identifiers.proto\"I\n\x12MeshRendererCreate\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifier\"J\n\x13MeshRendererDestroy\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierB\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unity.mesh_renderer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_MESHRENDERERCREATE']._serialized_start=74
  _globals['_MESHRENDERERCREATE']._serialized_end=147
  _globals['_MESHRENDERERDESTROY']._serialized_start=149
  _globals['_MESHRENDERERDESTROY']._serialized_end=223
# @@protoc_insertion_point(module_scope)