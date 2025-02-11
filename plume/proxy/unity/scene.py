from __future__ import annotations

from typing import Union, Optional
from plume.proxy.unity.game_object_collection import GameObjectCollection
from uuid import UUID


class Scene:
    _guid: UUID
    _name: str
    _asset_bundle_path: str
    _game_objects: GameObjectCollection

    def __init__(
        self,
        guid: Union[str, UUID],
        name: str,
        asset_bundle_path: str,
        game_objects: Optional[GameObjectCollection] = None,
    ):
        self._guid = UUID(guid) if isinstance(guid, str) else guid
        self._name = name
        self._asset_bundle_path = asset_bundle_path
        self._game_objects = game_objects if game_objects else GameObjectCollection()

    @property
    def guid(self) -> UUID:
        return self._guid

    @property
    def name(self) -> str:
        return self._name

    @property
    def asset_bundle_path(self) -> str:
        return self._asset_bundle_path

    @property
    def game_objects(self) -> GameObjectCollection:
        return self._game_objects

    def __repr__(self) -> str:
        return f"Scene(guid={self._guid}, name={self._name}, n_game_objects={len(self._game_objects)})"