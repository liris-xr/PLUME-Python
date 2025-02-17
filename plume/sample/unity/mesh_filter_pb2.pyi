from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class MeshFilterCreate(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...

class MeshFilterDestroy(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...

class MeshFilterUpdate(_message.Message):
    __slots__ = ("component", "mesh")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    MESH_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    mesh: _identifiers_pb2.AssetIdentifier
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
        mesh: _Optional[
            _Union[_identifiers_pb2.AssetIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...
