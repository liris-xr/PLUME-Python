# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lsl/lsl_stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14lsl/lsl_stream.proto\x12\x10plume.sample.lsl\"3\n\nStreamOpen\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x12\n\nxml_header\x18\x02 \x01(\t\" \n\x0bStreamClose\x12\x11\n\tstream_id\x18\x01 \x01(\t\"\xf8\x05\n\x0cStreamSample\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x44\n\x0c\x66loat_values\x18\x02 \x01(\x0b\x32,.plume.sample.lsl.StreamSample.RepeatedFloatH\x00\x12\x46\n\rdouble_values\x18\x03 \x01(\x0b\x32-.plume.sample.lsl.StreamSample.RepeatedDoubleH\x00\x12\x46\n\rstring_values\x18\x04 \x01(\x0b\x32-.plume.sample.lsl.StreamSample.RepeatedStringH\x00\x12\x42\n\x0bint8_values\x18\x05 \x01(\x0b\x32+.plume.sample.lsl.StreamSample.RepeatedInt8H\x00\x12\x44\n\x0cint16_values\x18\x06 \x01(\x0b\x32,.plume.sample.lsl.StreamSample.RepeatedInt16H\x00\x12\x44\n\x0cint32_values\x18\x07 \x01(\x0b\x32,.plume.sample.lsl.StreamSample.RepeatedInt32H\x00\x12\x44\n\x0cint64_values\x18\x08 \x01(\x0b\x32,.plume.sample.lsl.StreamSample.RepeatedInt64H\x00\x1a\x1e\n\rRepeatedFloat\x12\r\n\x05value\x18\x01 \x03(\x02\x1a\x1f\n\x0eRepeatedDouble\x12\r\n\x05value\x18\x01 \x03(\x01\x1a\x1f\n\x0eRepeatedString\x12\r\n\x05value\x18\x01 \x03(\t\x1a\x1d\n\x0cRepeatedInt8\x12\r\n\x05value\x18\x01 \x03(\x05\x1a\x1e\n\rRepeatedInt16\x12\r\n\x05value\x18\x01 \x03(\x05\x1a\x1e\n\rRepeatedInt32\x12\r\n\x05value\x18\x01 \x03(\x05\x1a\x1e\n\rRepeatedInt64\x12\r\n\x05value\x18\x01 \x03(\x03\x42\x08\n\x06valuesB\x13\xaa\x02\x10PLUME.Sample.LSLb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lsl.lsl_stream_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\020PLUME.Sample.LSL'
  _globals['_STREAMOPEN']._serialized_start=42
  _globals['_STREAMOPEN']._serialized_end=93
  _globals['_STREAMCLOSE']._serialized_start=95
  _globals['_STREAMCLOSE']._serialized_end=127
  _globals['_STREAMSAMPLE']._serialized_start=130
  _globals['_STREAMSAMPLE']._serialized_end=890
  _globals['_STREAMSAMPLE_REPEATEDFLOAT']._serialized_start=657
  _globals['_STREAMSAMPLE_REPEATEDFLOAT']._serialized_end=687
  _globals['_STREAMSAMPLE_REPEATEDDOUBLE']._serialized_start=689
  _globals['_STREAMSAMPLE_REPEATEDDOUBLE']._serialized_end=720
  _globals['_STREAMSAMPLE_REPEATEDSTRING']._serialized_start=722
  _globals['_STREAMSAMPLE_REPEATEDSTRING']._serialized_end=753
  _globals['_STREAMSAMPLE_REPEATEDINT8']._serialized_start=755
  _globals['_STREAMSAMPLE_REPEATEDINT8']._serialized_end=784
  _globals['_STREAMSAMPLE_REPEATEDINT16']._serialized_start=786
  _globals['_STREAMSAMPLE_REPEATEDINT16']._serialized_end=816
  _globals['_STREAMSAMPLE_REPEATEDINT32']._serialized_start=818
  _globals['_STREAMSAMPLE_REPEATEDINT32']._serialized_end=848
  _globals['_STREAMSAMPLE_REPEATEDINT64']._serialized_start=850
  _globals['_STREAMSAMPLE_REPEATEDINT64']._serialized_end=880
# @@protoc_insertion_point(module_scope)
