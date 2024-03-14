from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamOpen(_message.Message):
    __slots__ = ["stream_id", "xml_header"]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    XML_HEADER_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    xml_header: str
    def __init__(self, stream_id: _Optional[str] = ..., xml_header: _Optional[str] = ...) -> None: ...

class StreamClose(_message.Message):
    __slots__ = ["stream_id"]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    def __init__(self, stream_id: _Optional[str] = ...) -> None: ...

class StreamSample(_message.Message):
    __slots__ = ["stream_id", "float_values", "double_values", "string_values", "int8_values", "int16_values", "int32_values", "int64_values"]
    class RepeatedFloat(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...
    class RepeatedDouble(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...
    class RepeatedString(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, value: _Optional[_Iterable[str]] = ...) -> None: ...
    class RepeatedInt8(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...
    class RepeatedInt16(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...
    class RepeatedInt32(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...
    class RepeatedInt64(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, value: _Optional[_Iterable[int]] = ...) -> None: ...
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT8_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT16_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUES_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    float_values: StreamSample.RepeatedFloat
    double_values: StreamSample.RepeatedDouble
    string_values: StreamSample.RepeatedString
    int8_values: StreamSample.RepeatedInt8
    int16_values: StreamSample.RepeatedInt16
    int32_values: StreamSample.RepeatedInt32
    int64_values: StreamSample.RepeatedInt64
    def __init__(self, stream_id: _Optional[str] = ..., float_values: _Optional[_Union[StreamSample.RepeatedFloat, _Mapping]] = ..., double_values: _Optional[_Union[StreamSample.RepeatedDouble, _Mapping]] = ..., string_values: _Optional[_Union[StreamSample.RepeatedString, _Mapping]] = ..., int8_values: _Optional[_Union[StreamSample.RepeatedInt8, _Mapping]] = ..., int16_values: _Optional[_Union[StreamSample.RepeatedInt16, _Mapping]] = ..., int32_values: _Optional[_Union[StreamSample.RepeatedInt32, _Mapping]] = ..., int64_values: _Optional[_Union[StreamSample.RepeatedInt64, _Mapping]] = ...) -> None: ...
