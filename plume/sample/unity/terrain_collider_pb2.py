# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plume/sample/unity/terrain_collider.proto
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
    'plume/sample/unity/terrain_collider.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from plume.sample.unity import identifiers_pb2 as plume_dot_sample_dot_unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)plume/sample/unity/terrain_collider.proto\x12\x12plume.sample.unity\x1a$plume/sample/unity/identifiers.proto\"^\n\x15TerrainColliderCreate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"_\n\x16TerrainColliderDestroy\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\"\xba\x02\n\x15TerrainColliderUpdate\x12\x45\n\tcomponent\x18\x01 \x01(\x0b\x32\'.plume.sample.unity.ComponentIdentifierR\tcomponent\x12\x1d\n\x07\x65nabled\x18\x02 \x01(\x08H\x00R\x07\x65nabled\x88\x01\x01\x12K\n\x0cterrain_data\x18\x03 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x01R\x0bterrainData\x88\x01\x01\x12\x44\n\x08material\x18\x04 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x02R\x08material\x88\x01\x01\x42\n\n\x08_enabledB\x0f\n\r_terrain_dataB\x0b\n\t_materialB\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plume.sample.unity.terrain_collider_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_TERRAINCOLLIDERCREATE']._serialized_start=103
  _globals['_TERRAINCOLLIDERCREATE']._serialized_end=197
  _globals['_TERRAINCOLLIDERDESTROY']._serialized_start=199
  _globals['_TERRAINCOLLIDERDESTROY']._serialized_end=294
  _globals['_TERRAINCOLLIDERUPDATE']._serialized_start=297
  _globals['_TERRAINCOLLIDERUPDATE']._serialized_end=611
# @@protoc_insertion_point(module_scope)
