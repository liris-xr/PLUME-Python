from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class XRBaseInteractorCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class XRBaseInteractorDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class XRBaseInteractorUpdate(_message.Message):
    __slots__ = ["id", "enabled"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    enabled: bool
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class XRBaseInteractorHoverEnter(_message.Message):
    __slots__ = ["id", "interactable_current"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTABLE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    interactable_current: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., interactable_current: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class XRBaseInteractorHoverExit(_message.Message):
    __slots__ = ["id", "interactable_current"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTABLE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    interactable_current: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., interactable_current: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class XRBaseInteractorSelectEnter(_message.Message):
    __slots__ = ["id", "interactable_current"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTABLE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    interactable_current: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., interactable_current: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class XRBaseInteractorSelectExit(_message.Message):
    __slots__ = ["id", "interactable_current"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTABLE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    interactable_current: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., interactable_current: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...
