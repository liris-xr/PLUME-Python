from __future__ import annotations

from plume.proxy.unity.component import Component
from plume.proxy.unity.game_object import GameObject
from plume.proxy.unity.asset import Asset

from typing import Union, Optional
from uuid import UUID


class MeshFilter(Component):
    _mesh: Optional[Asset]

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        mesh: Optional[Asset] = None,
    ):
        super().__init__(guid, game_object)
        self._mesh = mesh

    @property
    def mesh(self) -> Optional[Asset]:
        return self._mesh

    def __repr__(self):
        return f"MeshFilter(guid={self.guid}, mesh={self._mesh})"
