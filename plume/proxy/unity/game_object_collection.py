from __future__ import annotations

from typing import List, Union, Optional, Type, Dict, Sequence
from plume.proxy.unity.game_object import GameObject
from plume.proxy.unity.component import Component
from plume.proxy.collection import Collection

from uuid import UUID


class GameObjectCollection(Collection[GameObject]):
    _guid_to_game_object: Dict[UUID, GameObject]
    _name_to_game_objects: Dict[str, List[GameObject]]

    def __post_init__(self):
        self._guid_to_game_object = {
            game_object.guid: game_object for game_object in self
        }
        self._name_to_game_objects = {}
        for game_object in self:
            self._name_to_game_objects.setdefault(game_object.name, []).append(
                game_object
            )

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        game_object = self.with_guid(guid)

        if not super()._remove(game_object):
            return False

        if game_object.name in self._name_to_game_objects:
            self._name_to_game_objects[game_object.name].remove(game_object)

        del self._guid_to_game_object[game_object.guid]
        return True

    def _add(self, game_object: GameObject) -> bool:
        if game_object.guid in self._guid_to_game_object:
            return False
        if not super()._add(game_object):
            return False
        self._guid_to_game_object[game_object.guid] = game_object
        if game_object.name in self._name_to_game_objects:
            self._name_to_game_objects[game_object.name].append(game_object)
        else:
            self._name_to_game_objects[game_object.name] = [game_object]
        return True

    def roots(self) -> GameObjectCollection:
        return GameObjectCollection(
            {
                game_object
                for game_object in self
                if game_object.transform.parent is None
            }
        )

    def with_guids(
        self, guids: Sequence[Union[str, UUID]]
    ) -> GameObjectCollection:
        # Ensure unique guids
        if not isinstance(guids, set):
            guids = set(guids)

        return GameObjectCollection(
            {self._guid_to_game_object.get(UUID(guid), None) for guid in guids}
        )

    def with_guid(self, guid: Union[str, UUID]) -> GameObject:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_game_object.get(guid, None)

    def first_with_name(self, name: str) -> Optional[GameObject]:
        gameobjects = self._name_to_game_objects.get(name, [])
        if len(gameobjects) == 0:
            return None
        return gameobjects[0]

    def with_names(self, names: Sequence[str]) -> GameObjectCollection:
        # Ensure unique names
        if not isinstance(names, set):
            names = set(names)

        return GameObjectCollection(
            {
                game_object
                for name in names
                for game_object in self._name_to_game_objects.get(name, [])
            }
        )

    def with_name(self, name: str) -> GameObjectCollection:
        """
        Retrieve one or more game objects with the specified name.

        Args:
            name (str): The name of the game objects to retrieve.

        Returns:
            GameObjectCollection: A collection of game objects that match the specified name.
        """
        return GameObjectCollection(self._name_to_game_objects.get(name, []))

    def with_tag(self, tag: str) -> GameObjectCollection:
        """
        Retrieve one or more game objects with the specified tag.

        Args:
            tag (str): The tag of the game objects to retrieve.

        Returns:
            GameObjectCollection: A collection of game objects that match the specified tag.
        """
        return GameObjectCollection(
            {game_object for game_object in self if game_object.tag == tag}
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
            {game_object for game_object in self if game_object.layer == layer}
        )

    def with_component_type(
        self, component_type: Type[Component]
    ) -> GameObjectCollection:
        """
        Retrieve one or more game objects that have at least one component of the specified type.

        Args:
            component_type (type): The type of component that the game objects must have.

        Returns:
            GameObjectCollection: A collection of game objects that have the specified component type.
        """
        return GameObjectCollection(
            {
                game_object
                for game_object in self
                if len(game_object.components.with_type(component_type)) > 0
            }
        )
