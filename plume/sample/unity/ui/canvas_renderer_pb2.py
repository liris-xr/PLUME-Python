# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plume/sample/unity/ui/canvas_renderer.proto
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
    'plume/sample/unity/ui/canvas_renderer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from plume.sample.unity import identifiers_pb2 as plume_dot_sample_dot_unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+plume/sample/unity/ui/canvas_renderer.proto\x12\x15plume.sample.unity.ui\x1a$plume/sample/unity/identifiers.proto\"]\n\x14\x43\x61nvasRendererCreate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"^\n\x15\x43\x61nvasRendererDestroy\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"\xb0\x01\n\x14\x43\x61nvasRendererUpdate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\x12\x37\n\x15\x63ull_transparent_mesh\x18\x02 \x01(\x08H\x00R\x13\x63ullTransparentMesh\x88\x01\x01\x42\x18\n\x16_cull_transparent_meshB\x18\xaa\x02\x15PLUME.Sample.Unity.UIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plume.sample.unity.ui.canvas_renderer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025PLUME.Sample.Unity.UI'
  _globals['_CANVASRENDERERCREATE']._serialized_start=108
  _globals['_CANVASRENDERERCREATE']._serialized_end=201
  _globals['_CANVASRENDERERDESTROY']._serialized_start=203
  _globals['_CANVASRENDERERDESTROY']._serialized_end=297
  _globals['_CANVASRENDERERUPDATE']._serialized_start=300
  _globals['_CANVASRENDERERUPDATE']._serialized_end=476
# @@protoc_insertion_point(module_scope)
