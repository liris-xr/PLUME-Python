from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LoadSceneMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOAD_SCENE_MODE_SINGLE: _ClassVar[LoadSceneMode]
    LOAD_SCENE_MODE_ADDITIVE: _ClassVar[LoadSceneMode]

LOAD_SCENE_MODE_SINGLE: LoadSceneMode
LOAD_SCENE_MODE_ADDITIVE: LoadSceneMode

class LoadScene(_message.Message):
    __slots__ = ("scene", "mode")
    SCENE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    scene: _identifiers_pb2.SceneIdentifier
    mode: LoadSceneMode
    def __init__(
        self,
        scene: _Optional[
            _Union[_identifiers_pb2.SceneIdentifier, _Mapping]
        ] = ...,
        mode: _Optional[_Union[LoadSceneMode, str]] = ...,
    ) -> None: ...

class UnloadScene(_message.Message):
    __slots__ = ("scene",)
    SCENE_FIELD_NUMBER: _ClassVar[int]
    scene: _identifiers_pb2.SceneIdentifier
    def __init__(
        self,
        scene: _Optional[
            _Union[_identifiers_pb2.SceneIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...

class ChangeActiveScene(_message.Message):
    __slots__ = ("scene",)
    SCENE_FIELD_NUMBER: _ClassVar[int]
    scene: _identifiers_pb2.SceneIdentifier
    def __init__(
        self,
        scene: _Optional[
            _Union[_identifiers_pb2.SceneIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...
