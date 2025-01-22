from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from plume_python.proxy.unity.gameobject import GameObject
from dataclasses import field

@dataclass(frozen=True)
class Component(ABC):
    uuid: str
    gameobject: GameObject

    def __post_init__(self):
        if not self.uuid:
            raise ValueError("uuid must not be None")
        if not self.gameobject:
            raise ValueError("gameobject must not be None")