from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecorderVersion(_message.Message):
    __slots__ = ["name", "major", "minor", "patch"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    major: str
    minor: str
    patch: str
    def __init__(self, name: _Optional[str] = ..., major: _Optional[str] = ..., minor: _Optional[str] = ..., patch: _Optional[str] = ...) -> None: ...

class RecordMetadata(_message.Message):
    __slots__ = ["recorder_version", "start_time", "name", "extra_metadata"]
    RECORDER_VERSION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_METADATA_FIELD_NUMBER: _ClassVar[int]
    recorder_version: RecorderVersion
    start_time: _timestamp_pb2.Timestamp
    name: str
    extra_metadata: str
    def __init__(self, recorder_version: _Optional[_Union[RecorderVersion, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., extra_metadata: _Optional[str] = ...) -> None: ...

class RecordMetrics(_message.Message):
    __slots__ = ["is_sequential", "duration", "n_samples"]
    IS_SEQUENTIAL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    N_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    is_sequential: bool
    duration: int
    n_samples: int
    def __init__(self, is_sequential: bool = ..., duration: _Optional[int] = ..., n_samples: _Optional[int] = ...) -> None: ...
