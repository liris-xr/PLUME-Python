from __future__ import annotations

from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.asset import Asset
from plume_python.proxy.unity.component.renderer import Renderer

from plume_python.proxy.common.bounds import Bounds
from plume_python.proxy.common.vector4 import Vector4

from typing import Union, Optional, List
from uuid import UUID


class MeshRenderer(Renderer):

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
        super().__init__(
            guid,
            game_object,
            enabled,
            materials,
            local_bounds,
            lightmap_index,
            lightmap_scale_offset,
            realtime_lightmap_index,
            realtime_lightmap_scale_offset,
        )
