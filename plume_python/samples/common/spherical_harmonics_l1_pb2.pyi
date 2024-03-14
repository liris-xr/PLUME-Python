from common import vector4_pb2 as _vector4_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SphericalHarmonicsL1(_message.Message):
    __slots__ = ["shAr", "shAg", "shAb"]
    SHAR_FIELD_NUMBER: _ClassVar[int]
    SHAG_FIELD_NUMBER: _ClassVar[int]
    SHAB_FIELD_NUMBER: _ClassVar[int]
    shAr: _vector4_pb2.Vector4
    shAg: _vector4_pb2.Vector4
    shAb: _vector4_pb2.Vector4
    def __init__(self, shAr: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., shAg: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., shAb: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...) -> None: ...
