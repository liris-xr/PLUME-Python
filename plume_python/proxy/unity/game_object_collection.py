from __future__ import annotations

from typing import List, Union, Iterable, Iterator, Optional, Type, Callable, Dict, Sequence
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.component import Component

from uuid import UUID

class GameObjectCollection(Iterable[GameObject]):
    _game_objects: List[GameObject]
    _guid_to_game_object: Dict[UUID, GameObject]
    _name_to_game_objects: Dict[str, List[GameObject]]

    def __init__(self, game_objects: Optional[Sequence[GameObject]] = None):
        self._game_objects = list(game_objects) if game_objects else []
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

    def _add(self, game_object: GameObject) -> bool:
        if game_object.guid in self._guid_to_game_object:
            return False
        self._game_objects.append(game_object)
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
                for game_object in self._game_objects
                if game_object.transform.parent is None
            }
        )
    
    def with_guids(self, guids: Sequence[Union[str, UUID]]) -> GameObjectCollection:

        # Ensure unique guids
        if not isinstance(guids, set):
            guids = set(guids)

        return GameObjectCollection(
            {
                self._guid_to_game_object.get(UUID(guid), None)
                for guid in guids
            }
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
        return gameobjects

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
            {
                game_object
                for game_object in self._game_objects
                if game_object.tag == tag
            }
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
            {
                game_object
                for game_object in self._game_objects
                if game_object.layer == layer
            }
        )
    
    def with_component_type(self, component_type: Type[Component]) -> GameObjectCollection:
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
                for game_object in self._game_objects
                if len(game_object.components.with_type(component_type)) > 0
            }
        )

    def where(self, predicate: Callable[[GameObject], bool]) -> GameObjectCollection:
        return GameObjectCollection({game_object for game_object in self._game_objects if predicate(game_object)})

    def first_or_default(self, predicate: Optional[Callable[[GameObject], bool]] = None, default: Optional[GameObject] = None) -> Optional[GameObject]:
        for game_object in self._game_objects:
            if predicate is None or predicate(game_object):
                return game_object
        return default

    def last_or_default(self, predicate: Optional[Callable[[GameObject], bool]] = None, default: Optional[GameObject] = None) -> Optional[GameObject]:
        for game_object in reversed(self._game_objects):
            if predicate is None or predicate(game_object):
                return game_object
        return default

    def first(self, predicate: Optional[Callable[[GameObject], bool]] = None) -> Optional[GameObject]:
        for game_object in self._game_objects:
            if predicate is None or predicate(game_object):
                return game_object
        raise ValueError("Sequence contains no matching element")
    
    def last(self, predicate: Optional[Callable[[GameObject], bool]]) -> Optional[GameObject]:
        for game_object in reversed(self._game_objects):
            if predicate is None or predicate(game_object):
                return game_object
        raise ValueError("Sequence contains no matching element")

    def sort_by(self, key: Callable[[GameObject], int], reverse: bool = False) -> GameObjectCollection:
        return GameObjectCollection(sorted(self._game_objects, key=key, reverse=reverse))

    def group_by(self, key: Callable[[GameObject], Type[Component]]) -> Dict[Type[Component], GameObjectCollection]:
        groups: Dict[Type[Component], GameObjectCollection] = {}
        for game_object in self._game_objects:
            key = key(game_object)
            if key in groups:
                groups[key]._add(game_object)
            else:
                groups[key] = GameObjectCollection([game_object])
        return groups
    
    def except_with(self, predicate: Callable[[GameObject], bool]) -> GameObjectCollection:
        return GameObjectCollection({game_object for game_object in self._game_objects if not predicate(game_object)})

    def __or__(self, value):
        if isinstance(value, GameObject):
            return GameObjectCollection(set(self._game_objects) + {value})
        if isinstance(value, GameObjectCollection):
            return GameObjectCollection(set(self._game_objects) + set(value._game_objects))
        if isinstance(value, (list, set, tuple)):
            return GameObjectCollection(set(self._game_objects) + set(value))
        raise TypeError(f"Unsupported operand type(s) for |: {type(self)} and {type(value)}")
    
    def __and__(self, value):
        if isinstance(value, GameObject):
            return GameObjectCollection(set(self._game_objects) & {value})
        if isinstance(value, GameObjectCollection):
            return GameObjectCollection(set(self._game_objects) & set(value._game_objects))
        if isinstance(value, (list, set, tuple)):
            return GameObjectCollection(set(self._game_objects) & set(value))
        raise TypeError(f"Unsupported operand type(s) for &: {type(self)} and {type(value)}")
    
    def __sub__(self, value):
        if isinstance(value, GameObject):
            return GameObjectCollection(set(self._game_objects) - {value})
        if isinstance(value, GameObjectCollection):
            return GameObjectCollection(set(self._game_objects) - set(value._game_objects))
        if isinstance(value, (list, set, tuple)):
            return GameObjectCollection(set(self._game_objects) - set(value))
        raise TypeError(f"Unsupported operand type(s) for -: {type(self)} and {type(value)}")
    
    def __xor__(self, value):
        if isinstance(value, GameObject):
            return GameObjectCollection(set(self._game_objects) ^ {value})
        if isinstance(value, GameObjectCollection):
            return GameObjectCollection(set(self._game_objects) ^ set(value._game_objects))
        if isinstance(value, (list, set, tuple)):
            return GameObjectCollection(set(self._game_objects) ^ set(value))
        raise TypeError(f"Unsupported operand type(s) for ^: {type(self)} and {type(value)}")
    
    def __eq__(self, value):
        if isinstance(value, GameObject):
            return len(self._game_objects) == 1 and self._game_objects[0] == value
        if isinstance(value, GameObjectCollection):
            return self._game_objects == value._game_objects
        if isinstance(value, (list, set, tuple)):
            return self._game_objects == value
        return False
    
    def __repr__(self):
        return "[" + ",".join([game_object.name for game_object in self._game_objects]) + "]"