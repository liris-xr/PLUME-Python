from __future__ import annotations

from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.asset import Asset

from typing import Union, Optional, List
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

    @mesh.setter
    def mesh(self, value: Optional[Asset]):
        self._mesh = value

    def __repr__(self):
        return f"MeshFilter(guid={self.guid}, mesh={self._mesh})"

    def deepcopy(self) -> MeshFilter:
        return MeshFilter(
            guid=self.guid,
            game_object=self.game_object,
            mesh=self._mesh.deepcopy() if self._mesh else None,
        )
