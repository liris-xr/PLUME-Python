from __future__ import annotations

from plume_python.proxy.unity.component import Component
from plume_python.proxy.common.vector3 import Vector3
from plume_python.proxy.common.quaternion import Quaternion

from typing import Union, Optional, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from plume_python.proxy.unity.game_object import GameObject

class Transform(Component):
    _sibling_index: int
    _local_position: Vector3
    _local_rotation: Quaternion
    _local_scale: Vector3

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        sibling_index: int = 0,
        local_position: Optional[Vector3] = None,
        local_rotation: Optional[Quaternion] = None,
        local_scale: Optional[Vector3] = None,
    ):
        super().__init__(guid, game_object)
        self._sibling_index = sibling_index
        self._local_position = local_position if local_position else Vector3(0, 0, 0)
        self._local_rotation = (
            local_rotation if local_rotation else Quaternion(0, 0, 0, 1)
        )
        self._local_scale = local_scale if local_scale else Vector3(1, 1, 1)

    @property
    def sibling_index(self) -> int:
        return self._sibling_index

    @property
    def local_position(self) -> Vector3:
        return self._local_position

    @property
    def local_rotation(self) -> Quaternion:
        return self._local_rotation

    @property
    def local_scale(self) -> Vector3:
        return self._local_scale

    def __repr__(self):
        return f"Transform(guid={self.guid}, sibling_index={self._sibling_index}, local_position={self._local_position}, local_rotation={self._local_rotation}, local_scale={self._local_scale})"
