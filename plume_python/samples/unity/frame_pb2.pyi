from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Frame(_message.Message):
    __slots__ = ["frame_number", "data"]
    FRAME_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    frame_number: int
    data: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, frame_number: _Optional[int] = ..., data: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
