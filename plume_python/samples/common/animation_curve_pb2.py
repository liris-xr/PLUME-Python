# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/animation_curve.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63ommon/animation_curve.proto\x12\x13plume.sample.common\"P\n\x0e\x41nimationCurve\x12>\n\tkeyframes\x18\x01 \x03(\x0b\x32+.plume.sample.common.AnimationCurveKeyFrame\"\xbf\x01\n\x16\x41nimationCurveKeyFrame\x12\x0c\n\x04time\x18\x01 \x01(\x02\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x12\n\nin_tangent\x18\x03 \x01(\x02\x12\x13\n\x0bout_tangent\x18\x04 \x01(\x02\x12\x38\n\rweighted_mode\x18\x05 \x01(\x0e\x32!.plume.sample.common.WeightedMode\x12\x11\n\tin_weight\x18\x06 \x01(\x02\x12\x12\n\nout_weight\x18\x07 \x01(\x02*k\n\x0cWeightedMode\x12\x16\n\x12WEIGHTED_MODE_NONE\x10\x00\x12\x14\n\x10WEIGHTED_MODE_IN\x10\x01\x12\x15\n\x11WEIGHTED_MODE_OUT\x10\x02\x12\x16\n\x12WEIGHTED_MODE_BOTH\x10\x03\x42\x16\xaa\x02\x13PLUME.Sample.Commonb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.animation_curve_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\023PLUME.Sample.Common'
  _globals['_WEIGHTEDMODE']._serialized_start=329
  _globals['_WEIGHTEDMODE']._serialized_end=436
  _globals['_ANIMATIONCURVE']._serialized_start=53
  _globals['_ANIMATIONCURVE']._serialized_end=133
  _globals['_ANIMATIONCURVEKEYFRAME']._serialized_start=136
  _globals['_ANIMATIONCURVEKEYFRAME']._serialized_end=327
# @@protoc_insertion_point(module_scope)
