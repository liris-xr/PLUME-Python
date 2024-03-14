from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FitMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FIT_MODE_UNCONSTRAINED: _ClassVar[FitMode]
    FIT_MODE_MIN_SIZE: _ClassVar[FitMode]
    FIT_MODE_PREF_SIZE: _ClassVar[FitMode]
FIT_MODE_UNCONSTRAINED: FitMode
FIT_MODE_MIN_SIZE: FitMode
FIT_MODE_PREF_SIZE: FitMode

class ContentSizeFitterCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class ContentSizeFitterDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class ContentSizeFitterUpdate(_message.Message):
    __slots__ = ["id", "horizontal_fit", "vertical_fit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_FIT_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_FIT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    horizontal_fit: FitMode
    vertical_fit: FitMode
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., horizontal_fit: _Optional[_Union[FitMode, str]] = ..., vertical_fit: _Optional[_Union[FitMode, str]] = ...) -> None: ...
