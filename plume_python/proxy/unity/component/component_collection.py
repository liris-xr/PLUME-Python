from __future__ import annotations

from plume_python.proxy.collection import Collection
from plume_python.proxy.unity.component import Component

from typing import (
    Union,
    List,
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

class ComponentCollection(Collection[TU], Generic[TU]):
    _guid_to_component: dict[UUID, Component]
    _type_to_components: dict[Type, List[Component]]

    def __post_init__(self):
        self._guid_to_component = {
            component.guid: component for component in self
        }

        self._type_to_components = {}
        for component in self:
            self._type_to_components.setdefault(type(component), []).append(component)

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return False
        component = self._guid_to_component.get(guid, None)
        if component is None:
            return False
        if not super()._remove(component):
            return False
        self._type_to_components[type(component)].remove(component)
        del self._guid_to_component[component.guid]
        return True

    def _add(self, component: TU) -> bool:
        if component.guid in self._guid_to_component:
            return False
        if not super()._add(component):
            return False
        self._guid_to_component[component.guid] = component
        self._type_to_components.setdefault(type(component), []).append(component)
        return True

    def with_guid(self, guid: Union[str, UUID]) -> TU:
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
                for component in self
                if component.game_object.guid == game_object_guid
            ]
        )
