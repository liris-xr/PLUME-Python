from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameObjectCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.GameObjectIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.GameObjectIdentifier, _Mapping]] = ...) -> None: ...

class GameObjectDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.GameObjectIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.GameObjectIdentifier, _Mapping]] = ...) -> None: ...

class GameObjectUpdate(_message.Message):
    __slots__ = ["id", "name", "active", "tag", "layer", "scene_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.GameObjectIdentifier
    name: str
    active: bool
    tag: str
    layer: int
    scene_id: int
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.GameObjectIdentifier, _Mapping]] = ..., name: _Optional[str] = ..., active: bool = ..., tag: _Optional[str] = ..., layer: _Optional[int] = ..., scene_id: _Optional[int] = ...) -> None: ...
