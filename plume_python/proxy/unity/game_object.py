from __future__ import annotations

from typing import List, Union, Iterable, Iterator, TYPE_CHECKING, Optional
from plume_python.proxy.unity.component import ComponentCollection

from uuid import UUID

if TYPE_CHECKING:
    from plume_python.proxy.unity.scene import Scene


class GameObject:
    _guid: UUID
    _scene: Scene

    _name: str
    _active: bool
    _tag: str
    _layer: int
    _components: ComponentCollection

    def __init__(
        self,
        guid: Union[str, UUID],
        scene: Scene,
        name: str = "GameObject",
        active: bool = True,
        tag: str = "",
        layer: int = 0,
        components: Optional[ComponentCollection] = None,
    ):
        self._guid = UUID(guid) if isinstance(guid, str) else guid
        self._scene = scene
        self._name = name
        self._active = active
        self._tag = tag
        self._layer = layer
        self._components = components if components else ComponentCollection()

    @property
    def guid(self) -> UUID:
        return self._guid

    @property
    def scene(self) -> Scene:
        return self._scene

    @property
    def name(self) -> str:
        return self._name

    @property
    def active(self) -> bool:
        return self._active

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def layer(self) -> int:
        return self._layer

    @property
    def components(self) -> ComponentCollection:
        return self._components

    def __repr__(self):
        return f"GameObject(guid={self._guid}, scene={self._scene.name}, name={self._name}, active={self._active}, tag={self._tag}, layer={self._layer}, components=[{', '.join([str(type(component).__name__) for component in self._components])}])"

    def deepcopy(self) -> GameObject:
        new_game_object = GameObject(
            guid=self._guid,
            scene=self._scene,
            name=self._name,
            active=self._active,
            tag=self._tag,
            layer=self._layer,
            components=self._components.deepcopy(),
        )
        for component in new_game_object.components:
            component._game_object = new_game_object
        return new_game_object


class GameObjectCollection(Iterable[GameObject]):
    _game_objects: List[GameObject]
    _guid_to_game_object: dict[UUID, GameObject]

    def __init__(self, game_objects: List[GameObject] = []):
        self._game_objects = game_objects.copy()
        self._guid_to_game_object = {
            game_object.guid: game_object for game_object in self._game_objects
        }

    def __len__(self) -> int:
        return len(self._game_objects)

    def __getitem__(self, index: int) -> GameObject:
        return self._game_objects[index]

    def __iter__(self) -> Iterator[GameObject]:
        return iter(self._game_objects)

    def __contains__(self, game_object: GameObject) -> bool:
        return game_object.guid in self._guid_to_game_object

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return False
        game_object = self._guid_to_game_object.get(guid, None)
        if game_object is None:
            return False
        self._game_objects.remove(game_object)
        del self._guid_to_game_object[game_object.guid]
        return True

    def _add(self, game_object: GameObject):
        self._game_objects.append(game_object)
        self._guid_to_game_object[game_object.guid] = game_object

    def get_by_guid(self, guid: Union[str, UUID]) -> GameObject:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_game_object.get(guid, None)

    def get_by_name(self, name: str) -> GameObject:
        for game_object in self._game_objects:
            if game_object.name == name:
                return game_object
        raise KeyError(f"No game object with name '{name}' found")

    def deepcopy(self) -> GameObjectCollection:
        return GameObjectCollection(
            [game_object.deepcopy() for game_object in self._game_objects]
        )
