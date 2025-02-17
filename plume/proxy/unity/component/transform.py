from __future__ import annotations

from plume.proxy.unity.component import Component
from plume.proxy.common.vector3 import Vector3
from plume.proxy.common.quaternion import Quaternion

from typing import Union, Optional, TYPE_CHECKING, List
from uuid import UUID
import numpy as np
import functools

if TYPE_CHECKING:
    from plume.proxy.unity.game_object import GameObject


class Transform(Component):
    _parent: Optional[Transform]
    _children: List[Transform]
    _sibling_index: int
    _local_position: Vector3
    _local_rotation: Quaternion
    _local_scale: Vector3

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        parent: Optional[Transform] = None,
        children: Optional[List[Transform]] = None,
        sibling_index: int = 0,
        local_position: Optional[Vector3] = None,
        local_rotation: Optional[Quaternion] = None,
        local_scale: Optional[Vector3] = None,
    ):
        super().__init__(guid, game_object)
        self._parent = parent
        self._children = children if children else []
        self._sibling_index = sibling_index
        self._local_position = (
            local_position if local_position else Vector3(0, 0, 0)
        )
        self._local_rotation = (
            local_rotation if local_rotation else Quaternion(0, 0, 0, 1)
        )
        self._local_scale = local_scale if local_scale else Vector3(1, 1, 1)

    def _invalidate_cached_world_matrix(self):
        self.__dict__.pop("world_matrix", None)
        for child in self._children:
            child._invalidate_cached_world_matrix()

    @functools.cached_property
    def world_matrix(self) -> np.ndarray:
        T = np.eye(4, dtype=np.float32)
        T[:3, 3] = self._local_position.numpy()

        R = np.eye(4, dtype=np.float32)
        R[:3, :3] = self._local_rotation.as_matrix()

        S = np.eye(4, dtype=np.float32)
        S[:3, :3] *= self._local_scale.numpy()

        local_matrix = T @ R @ S

        if self._parent:
            return self._parent.world_matrix @ local_matrix

        return local_matrix

    @property
    def world_position(self) -> Vector3:
        x = self.world_matrix[0, 3]
        y = self.world_matrix[1, 3]
        z = self.world_matrix[2, 3]
        return Vector3(x, y, z)

    @property
    def world_rotation(self) -> Quaternion:
        return Quaternion.from_matrix(self.world_matrix[:3, :3])

    @property
    def world_scale(self) -> Vector3:
        scale_x = np.linalg.norm(self.world_matrix[:3, 0])
        scale_y = np.linalg.norm(self.world_matrix[:3, 1])
        scale_z = np.linalg.norm(self.world_matrix[:3, 2])
        return Vector3(scale_x, scale_y, scale_z)

    @property
    def parent(self) -> Optional[Transform]:
        return self._parent

    @property
    def children(self) -> List[Transform]:
        return self._children.copy()

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
