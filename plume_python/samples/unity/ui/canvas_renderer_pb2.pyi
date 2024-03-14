from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CanvasRendererCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasRendererDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class CanvasRendererUpdate(_message.Message):
    __slots__ = ["id", "cull_transparent_mesh"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CULL_TRANSPARENT_MESH_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    cull_transparent_mesh: bool
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., cull_transparent_mesh: bool = ...) -> None: ...
