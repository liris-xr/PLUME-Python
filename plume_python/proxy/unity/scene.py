from __future__ import annotations

from typing import List, Union, Optional, Iterable, Iterator
from plume_python.proxy.unity.game_object import GameObjectCollection
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
    
    def deepcopy(self) -> Scene:
        new_scene = Scene(
            guid=self._guid,
            name=self._name,
            asset_bundle_path=self._asset_bundle_path,
            game_objects=self._game_objects.deepcopy(),
        )
        for game_object in new_scene.game_objects:
            game_object._scene = new_scene
        return new_scene


class SceneCollection(Iterable[Scene]):
    _scenes: List[Scene]
    _guid_to_scene: dict[UUID, Scene]

    def __init__(self, scenes: List[Scene] = []):
        self._scenes = scenes.copy()
        self._guid_to_scene = {scene.guid: scene for scene in self._scenes}

    def __len__(self) -> int:
        return len(self._scenes)

    def __getitem__(self, index: int) -> Scene:
        return self._scenes[index]

    def __iter__(self) -> Iterator[Scene]:
        return iter(self._scenes)

    def __contains__(self, scene: Scene) -> bool:
        return scene in self._scenes

    def _remove(self, scene: Scene) -> bool:
        if scene is None or scene.guid not in self._guid_to_scene:
            return False
        self._scenes.remove(scene)
        del self._guid_to_scene[scene.guid]
        return True

    def _add(self, scene: Scene):
        self._scenes.append(scene)
        self._guid_to_scene[scene.guid] = scene

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        scene = self.get_by_guid(guid)
        return self._remove(scene)

    def with_guid(self, guid: Union[str, UUID]) -> Scene:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_scene.get(guid, None)

    def first_with_name(self, name: str) -> Optional[Scene]:
        for scene in self._scenes:
            if scene.name == name:
                return scene
        return None

    def with_name(self, name: str) -> SceneCollection:
        return SceneCollection(
            [scene for scene in self._scenes if scene.name == name]
        )

    def __repr__(self) -> str:
        return f"SceneCollection(scenes={[scene.name for scene in self._scenes]})"

    def deepcopy(self) -> SceneCollection:
        return SceneCollection([scene.deepcopy() for scene in self._scenes])
