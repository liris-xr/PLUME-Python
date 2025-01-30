from __future__ import annotations

from abc import ABC, abstractmethod
from typing import (
    Union,
    List,
    Iterable,
    Iterator,
    TypeVar,
    Type,
    TYPE_CHECKING,
    Optional,
    Generic,
)
from uuid import UUID

if TYPE_CHECKING:
    from plume_python.proxy.unity.game_object import GameObject

TU = TypeVar("TU", bound="Component")
TV = TypeVar("TV", bound="Component")


class Component(ABC):
    _guid: UUID
    _game_object: GameObject

    def __init__(self, guid: Union[str, UUID], game_object: GameObject):
        self._guid = UUID(guid) if isinstance(guid, str) else guid
        self._game_object = game_object

    @property
    def guid(self) -> UUID:
        return self._guid

    @property
    def game_object(self) -> GameObject:
        return self._game_object
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(guid={self.guid}, game_object={self.game_object.name})"


class ComponentCollection(Iterable[Component], Generic[TU]):
    _components: List[Component]
    _guid_to_component: dict[UUID, Component]
    _type_to_components: dict[Type, List[Component]]

    def __init__(self, components: List[Component] = []):
        self._components = components.copy()

        self._guid_to_component = {
            component.guid: component for component in self._components
        }

        self._type_to_components = {}
        for component in self._components:
            self._type_to_components.setdefault(type(component), []).append(component)

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, index: int) -> TU:
        return self._components[index]

    def __iter__(self) -> Iterator[TU]:
        return iter(self._components)

    def __contains__(self, component: Component) -> bool:
        return component in self._components

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return False
        component = self._guid_to_component.get(guid, None)
        if component is None:
            return False
        self._components.remove(component)
        self._type_to_components[type(component)].remove(component)
        del self._guid_to_component[component.guid]
        return True

    def _add(self, component: Component):
        self._components.append(component)
        self._guid_to_component[component.guid] = component
        self._type_to_components.setdefault(type(component), []).append(component)

    def with_guid(self, guid: Union[str, UUID]) -> Component:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_component.get(guid, None)
    
    def first_with_type(self, component_type: Type[TV]) -> Optional[TV]:
        components = self._type_to_components.get(component_type, [])
        if len(components) == 0:
            return None
        return components[0]

    def with_type(self, component_type: Type[TV]) -> ComponentCollection[TV]:
        return ComponentCollection[TV](
            self._type_to_components.get(component_type, [])
        )
    
    def with_game_object(self, game_object: GameObject) -> ComponentCollection[TU]:
        game_object_guid = game_object.guid
        return ComponentCollection(
            [
                component
                for component in self._components
                if component.game_object.guid == game_object_guid
            ]
        )
