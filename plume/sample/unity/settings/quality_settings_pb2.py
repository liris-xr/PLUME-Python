# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plume/sample/unity/settings/quality_settings.proto
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
    'plume/sample/unity/settings/quality_settings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from plume.sample.unity import identifiers_pb2 as plume_dot_sample_dot_unity_dot_identifiers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2plume/sample/unity/settings/quality_settings.proto\x12\x1bplume.sample.unity.settings\x1a$plume/sample/unity/identifiers.proto\"\xa3\x01\n\x15QualitySettingsUpdate\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\\\n\x15render_pipeline_asset\x18\x02 \x01(\x0b\x32#.plume.sample.unity.AssetIdentifierH\x00R\x13renderPipelineAsset\x88\x01\x01\x42\x18\n\x16_render_pipeline_assetB\x1e\xaa\x02\x1bPLUME.Sample.Unity.Settingsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plume.sample.unity.settings.quality_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\033PLUME.Sample.Unity.Settings'
  _globals['_QUALITYSETTINGSUPDATE']._serialized_start=122
  _globals['_QUALITYSETTINGSUPDATE']._serialized_end=285
# @@protoc_insertion_point(module_scope)
