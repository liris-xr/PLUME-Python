from plume.sample.common import vector4_pb2 as _vector4_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SphericalHarmonicsL1(_message.Message):
    __slots__ = ("sh_ar", "sh_ag", "sh_ab")
    SH_AR_FIELD_NUMBER: _ClassVar[int]
    SH_AG_FIELD_NUMBER: _ClassVar[int]
    SH_AB_FIELD_NUMBER: _ClassVar[int]
    sh_ar: _vector4_pb2.Vector4
    sh_ag: _vector4_pb2.Vector4
    sh_ab: _vector4_pb2.Vector4
    def __init__(
        self,
        sh_ar: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...,
        sh_ag: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...,
        sh_ab: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ...,
    ) -> None: ...
