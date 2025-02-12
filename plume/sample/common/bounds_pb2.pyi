from plume.sample.common import vector3_pb2 as _vector3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bounds(_message.Message):
    __slots__ = ("center", "size")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    center: _vector3_pb2.Vector3
    size: _vector3_pb2.Vector3
    def __init__(self, center: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., size: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ...) -> None: ...
