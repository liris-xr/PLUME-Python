from __future__ import annotations

from typing import List, Union, Iterable, Iterator, TYPE_CHECKING, Optional, Type, TypeVar
from plume_python.proxy.unity.component import ComponentCollection, Component
from plume_python.proxy.unity.component.transform import Transform

from uuid import UUID

if TYPE_CHECKING:
    from plume_python.proxy.unity.scene import Scene

TC = TypeVar("TC", bound="Component")

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
    def transform(self) -> Transform:
        return self.components.get_first_by_type(Transform)

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
    _name_to_game_objects: dict[str, List[GameObject]]

    def __init__(self, game_objects: List[GameObject] = []):
        self._game_objects = game_objects.copy()
        self._guid_to_game_object = {
            game_object.guid: game_object for game_object in self._game_objects
        }
        self._name_to_game_objects = {}
        for game_object in self._game_objects:
            self._name_to_game_objects.setdefault(game_object.name, []).append(
                game_object
            )

    def __len__(self) -> int:
        return len(self._game_objects)

    def __getitem__(self, index: int) -> GameObject:
        return self._game_objects[index]

    def __iter__(self) -> Iterator[GameObject]:
        return iter(self._game_objects)

    def __contains__(self, game_object: GameObject) -> bool:
        return game_object in self._game_objects

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return False
        game_object = self._guid_to_game_object.get(guid, None)
        if game_object is None:
            return False
        self._game_objects.remove(game_object)

        if game_object.name in self._name_to_game_objects:
            self._name_to_game_objects[game_object.name].remove(game_object)

        del self._guid_to_game_object[game_object.guid]
        return True

    def _add(self, game_object: GameObject):
        self._game_objects.append(game_object)
        self._guid_to_game_object[game_object.guid] = game_object
        if game_object.name in self._name_to_game_objects:
            self._name_to_game_objects[game_object.name].append(game_object)
        else:
            self._name_to_game_objects[game_object.name] = [game_object]

    def with_guid(self, guid: Union[str, UUID]) -> GameObject:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_game_object.get(guid, None)

    def first_with_name(self, name: str) -> Optional[GameObject]:
        return self._name_to_game_objects.get(name, [None])[0]

    def with_name(self, name: str) -> GameObjectCollection:
        """
        Retrieve one or more game objects with the specified name.

        Args:
            name (str): The name of the game objects to retrieve.

        Returns:
            GameObjectCollection: A collection of game objects that match the specified name.
        """
        return GameObjectCollection(
            self._name_to_game_objects.get(name, [])
        )
    
    def with_tag(self, tag: str) -> GameObjectCollection:
        """
        Retrieve one or more game objects with the specified tag.

        Args:
            tag (str): The tag of the game objects to retrieve.

        Returns:
            GameObjectCollection: A collection of game objects that match the specified tag.
        """
        return GameObjectCollection(
            [
                game_object
                for game_object in self._game_objects
                if game_object.tag == tag
            ]
        )
    
    def with_layer(self, layer: int) -> GameObjectCollection:
        """
        Retrieve one or more game objects with the specified layer.

        Args:
            layer (int): The layer of the game objects to retrieve.

        Returns:
            GameObjectCollection: A collection of game objects that match the specified layer.
        """
        return GameObjectCollection(
            [
                game_object
                for game_object in self._game_objects
                if game_object.layer == layer
            ]
        )
    
    def with_component_type(self, component_type: Type[TC]) -> GameObjectCollection:
        """
        Retrieve one or more game objects that have at least one component of the specified type.

        Args:
            component_type (type): The type of component that the game objects must have.

        Returns:
            GameObjectCollection: A collection of game objects that have the specified component type.
        """
        return GameObjectCollection(
            [
                game_object
                for game_object in self._game_objects
                if len(game_object.components.with_type(component_type)) > 0
            ]
        )

    def deepcopy(self) -> GameObjectCollection:
        return GameObjectCollection(
            [game_object.deepcopy() for game_object in self._game_objects]
        )
