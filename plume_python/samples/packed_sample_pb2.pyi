from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackedSample(_message.Message):
    __slots__ = ["timestamp", "payload"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    payload: _any_pb2.Any
    def __init__(self, timestamp: _Optional[int] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
