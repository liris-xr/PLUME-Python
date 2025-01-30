from __future__ import annotations

from typing import (
    Union,
    TYPE_CHECKING,
    Optional,
)
from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.component import ComponentCollection
from plume_python.proxy.unity.component.transform import Transform

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
    def transform(self) -> Transform:
        return self.components.first_with_type(Transform)

    @property
    def components(self) -> ComponentCollection[Component]:
        return self._components

    def __hash__(self):
        return hash(self._guid)

    def __eq__(self, other):
        if not isinstance(other, GameObject):
            return False
        return self._guid == other._guid

    def __repr__(self):
        return f"GameObject(guid={self._guid}, scene={self._scene.name}, name={self._name}, active={self._active}, tag={self._tag}, layer={self._layer}, components=[{', '.join([str(type(component).__name__) for component in self._components])}])"
