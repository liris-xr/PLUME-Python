from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GameObjectIdentifier(_message.Message):
    __slots__ = ("guid", "transform_guid", "scene")
    GUID_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_GUID_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    guid: str
    transform_guid: str
    scene: SceneIdentifier
    def __init__(
        self,
        guid: _Optional[str] = ...,
        transform_guid: _Optional[str] = ...,
        scene: _Optional[_Union[SceneIdentifier, _Mapping]] = ...,
    ) -> None: ...

class ComponentIdentifier(_message.Message):
    __slots__ = ("guid", "game_object")
    GUID_FIELD_NUMBER: _ClassVar[int]
    GAME_OBJECT_FIELD_NUMBER: _ClassVar[int]
    guid: str
    game_object: GameObjectIdentifier
    def __init__(
        self,
        guid: _Optional[str] = ...,
        game_object: _Optional[_Union[GameObjectIdentifier, _Mapping]] = ...,
    ) -> None: ...

class AssetIdentifier(_message.Message):
    __slots__ = ("guid", "asset_bundle_path")
    GUID_FIELD_NUMBER: _ClassVar[int]
    ASSET_BUNDLE_PATH_FIELD_NUMBER: _ClassVar[int]
    guid: str
    asset_bundle_path: str
    def __init__(
        self,
        guid: _Optional[str] = ...,
        asset_bundle_path: _Optional[str] = ...,
    ) -> None: ...

class SceneIdentifier(_message.Message):
    __slots__ = ("guid", "name", "asset_bundle_path")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_BUNDLE_PATH_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    asset_bundle_path: str
    def __init__(
        self,
        guid: _Optional[str] = ...,
        name: _Optional[str] = ...,
        asset_bundle_path: _Optional[str] = ...,
    ) -> None: ...
