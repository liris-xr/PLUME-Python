from __future__ import annotations

from typing import List, TYPE_CHECKING

from dataclasses import dataclass

from plume_python.proxy.unity.component import Component

if TYPE_CHECKING:
    from plume_python.proxy.unity.scene import Scene

@dataclass(frozen=True)
class GameObject:
    uuid: str
    name: str = "Unknown"
    active: bool = True
    layer: int = 0

    components: List[Component] = []
    scene: Scene

    def __post_init__(self):
        if not self.uuid:
            raise ValueError("uuid must not be None")
        if not self.scene:
            raise ValueError("scene must not be None")