from __future__ import annotations

from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.asset import Asset
from plume_python.proxy.common.bounds import Bounds
from plume_python.proxy.common.vector4 import Vector4

from typing import Union, Optional, List
from uuid import UUID

from abc import ABC, abstractmethod

class Renderer(Component, ABC):
    _enabled: bool
    _materials: List[Asset]
    _local_bounds: Bounds
    _lightmap_index: int
    _lightmap_scale_offset: Vector4
    _realtime_lightmap_index: int
    _realtime_lightmap_scale_offset: Vector4

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        enabled: bool = True,
        materials: Optional[List[Asset]] = None,
        local_bounds: Optional[Bounds] = None,
        lightmap_index: int = -1,
        lightmap_scale_offset: Optional[Vector4] = None,
        realtime_lightmap_index: int = -1,
        realtime_lightmap_scale_offset: Optional[Vector4] = None,
    ):
        super().__init__(guid, game_object)
        self._enabled = enabled
        self._materials = materials or []
        self._local_bounds = local_bounds or Bounds()
        self._lightmap_index = lightmap_index
        self._lightmap_scale_offset = lightmap_scale_offset or Vector4()
        self._realtime_lightmap_index = realtime_lightmap_index
        self._realtime_lightmap_scale_offset = realtime_lightmap_scale_offset or Vector4()

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @property
    def materials(self) -> List[Asset]:
        return self._materials.copy()

    @property
    def local_bounds(self) -> Bounds:
        return self._local_bounds

    @property
    def lightmap_index(self) -> int:
        return self._lightmap_index

    @property
    def lightmap_scale_offset(self) -> Vector4:
        return self._lightmap_scale_offset

    @property
    def realtime_lightmap_index(self) -> int:
        return self._realtime_lightmap_index

    @property
    def realtime_lightmap_scale_offset(self) -> Vector4:
        return self._realtime_lightmap_scale_offset
    
    def __repr__(self) -> str:
        return f"Renderer(guid={self.guid}, game_object={self.game_object.name}, enabled={self.enabled}, materials={self.materials}, local_bounds={self.local_bounds}, lightmap_index={self.lightmap_index}, lightmap_scale_offset={self.lightmap_scale_offset}, realtime_lightmap_index={self.realtime_lightmap_index}, realtime_lightmap_scale_offset={self.realtime_lightmap_scale_offset})"

    @abstractmethod
    def deepcopy(self) -> Renderer:
        raise NotImplementedError