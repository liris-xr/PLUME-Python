# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plume/sample/unity/rendering.proto
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
    'plume/sample/unity/rendering.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"plume/sample/unity/rendering.proto\x12\x12plume.sample.unity*\x95\x01\n\x11ShadowCastingMode\x12\x1b\n\x17SHADOW_CASTING_MODE_OFF\x10\x00\x12\x1a\n\x16SHADOW_CASTING_MODE_ON\x10\x01\x12!\n\x1dSHADOW_CASTING_MODE_TWO_SIDED\x10\x02\x12$\n SHADOW_CASTING_MODE_SHADOWS_ONLY\x10\x03*\xb6\x01\n\x14ReflectionProbeUsage\x12\x1e\n\x1aREFLECTION_PROBE_USAGE_OFF\x10\x00\x12\'\n#REFLECTION_PROBE_USAGE_BLEND_PROBES\x10\x01\x12\x32\n.REFLECTION_PROBE_USAGE_BLEND_PROBES_AND_SKYBOX\x10\x02\x12!\n\x1dREFLECTION_PROBE_USAGE_SIMPLE\x10\x03*\xbd\x01\n\rRenderingPath\x12&\n\"RENDERING_PATH_USE_PLAYER_SETTINGS\x10\x00\x12\x1d\n\x19RENDERING_PATH_VERTEX_LIT\x10\x01\x12\x1a\n\x16RENDERING_PATH_FORWARD\x10\x02\x12$\n RENDERING_PATH_DEFERRED_LIGHTING\x10\x03\x12#\n\x1fRENDERING_PATH_DEFERRED_SHADING\x10\x04*y\n\x0eOpaqueSortMode\x12\x1c\n\x18OPAQUE_SORT_MODE_DEFAULT\x10\x00\x12\"\n\x1eOPAQUE_SORT_MODE_FRONT_TO_BACK\x10\x01\x12%\n!OPAQUE_SORT_MODE_NO_DISTANCE_SORT\x10\x02*\xb3\x01\n\x14TransparencySortMode\x12\"\n\x1eTRANSPARENCY_SORT_MODE_DEFAULT\x10\x00\x12&\n\"TRANSPARENCY_SORT_MODE_PERSPECTIVE\x10\x01\x12\'\n#TRANSPARENCY_SORT_MODE_ORTHOGRAPHIC\x10\x02\x12&\n\"TRANSPARENCY_SORT_MODE_CUSTOM_AXIS\x10\x03\x42\x15\xaa\x02\x12PLUME.Sample.Unityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plume.sample.unity.rendering_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\022PLUME.Sample.Unity'
  _globals['_SHADOWCASTINGMODE']._serialized_start=59
  _globals['_SHADOWCASTINGMODE']._serialized_end=208
  _globals['_REFLECTIONPROBEUSAGE']._serialized_start=211
  _globals['_REFLECTIONPROBEUSAGE']._serialized_end=393
  _globals['_RENDERINGPATH']._serialized_start=396
  _globals['_RENDERINGPATH']._serialized_end=585
  _globals['_OPAQUESORTMODE']._serialized_start=587
  _globals['_OPAQUESORTMODE']._serialized_end=708
  _globals['_TRANSPARENCYSORTMODE']._serialized_start=711
  _globals['_TRANSPARENCYSORTMODE']._serialized_end=890
# @@protoc_insertion_point(module_scope)
