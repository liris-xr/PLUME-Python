from __future__ import annotations

from plume.proxy.unity.component import Component
from plume.proxy.unity.game_object import GameObject

from typing import Union
from uuid import UUID


class XRBaseInteractable(Component):
    _enabled: bool = True

    def __init__(
        self,
        guid: Union[str, UUID],
        game_object: GameObject,
        enabled: bool = True,
    ):
        super().__init__(guid, game_object)
        self._enabled = enabled
