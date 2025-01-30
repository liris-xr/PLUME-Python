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
)
from uuid import UUID

if TYPE_CHECKING:
    from plume_python.proxy.unity.game_object import GameObject

TU = TypeVar("TU", bound="Component")


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

    @abstractmethod
    def deepcopy(self) -> Component:
        raise NotImplementedError


class ComponentCollection(Iterable[Component]):
    _components: List[Component]
    _guid_to_component: dict[UUID, Component]
    _type_to_components: dict[Type[TU], List[Component]]

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

    def __getitem__(self, index: int) -> Component:
        return self._components[index]

    def __iter__(self) -> Iterator[Component]:
        return iter(self._components)

    def __contains__(self, component: Component) -> bool:
        return component.guid in self._guid_to_component

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

    def get_by_guid(self, guid: Union[str, UUID]) -> Optional[Component]:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_component.get(guid, None)

    def get_by_type(self, component_type: Type[TU]) -> List[TU]:
        return self._type_to_components.get(component_type, [])
    
    def get_first_by_type(self, component_type: Type[TU]) -> Optional[TU]:
        if component_type not in self._type_to_components:
            return None
        else:
            return self._type_to_components[component_type][0]

    def deepcopy(self) -> ComponentCollection:
        return ComponentCollection(
            [component.deepcopy() for component in self._components]
        )
