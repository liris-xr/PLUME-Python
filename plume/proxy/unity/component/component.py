from __future__ import annotations

from typing import Union, TYPE_CHECKING
from uuid import UUID
from abc import ABC

if TYPE_CHECKING:
    from plume.proxy.unity.game_object import GameObject


class Component(ABC):
    _guid: UUID
    _game_object: GameObject

    def __init__(self, guid: Union[str, UUID], game_object: GameObject):
        self._guid = UUID(guid) if isinstance(guid, str) else guid
        self._game_object = game_object

    @property
    def guid(self) -> UUID:
        return self._guid

    @property
    def game_object(self) -> GameObject:
        return self._game_object

    def __hash__(self) -> int:
        return hash(self.guid)

    def __str__(self) -> str:
        return f"{type(self).__name__} (guid={self.guid})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(guid={self.guid})"
