from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadSceneMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LOAD_SCENE_MODE_SINGLE: _ClassVar[LoadSceneMode]
    LOAD_SCENE_MODE_ADDITIVE: _ClassVar[LoadSceneMode]
LOAD_SCENE_MODE_SINGLE: LoadSceneMode
LOAD_SCENE_MODE_ADDITIVE: LoadSceneMode

class GameObjectIdentifier(_message.Message):
    __slots__ = ["game_object_id", "transform_id"]
    GAME_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ID_FIELD_NUMBER: _ClassVar[int]
    game_object_id: str
    transform_id: str
    def __init__(self, game_object_id: _Optional[str] = ..., transform_id: _Optional[str] = ...) -> None: ...

class ComponentIdentifier(_message.Message):
    __slots__ = ["component_id", "parent_id"]
    COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    component_id: str
    parent_id: GameObjectIdentifier
    def __init__(self, component_id: _Optional[str] = ..., parent_id: _Optional[_Union[GameObjectIdentifier, _Mapping]] = ...) -> None: ...

class AssetIdentifier(_message.Message):
    __slots__ = ["id", "path"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class SceneIdentifier(_message.Message):
    __slots__ = ["id", "runtime_index", "name", "path", "build_index", "mode"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BUILD_INDEX_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    runtime_index: str
    name: str
    path: str
    build_index: int
    mode: LoadSceneMode
    def __init__(self, id: _Optional[str] = ..., runtime_index: _Optional[str] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., build_index: _Optional[int] = ..., mode: _Optional[_Union[LoadSceneMode, str]] = ...) -> None: ...
