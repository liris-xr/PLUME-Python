from __future__ import annotations

from plume_python.proxy.collection import Collection
from plume_python.proxy.unity.scene import Scene
from typing import Union, Optional
from uuid import UUID

class SceneCollection(Collection[Scene]):
    _guid_to_scene: dict[UUID, Scene]

    def __post_init__(self):
        self._guid_to_scene = {scene.guid: scene for scene in self}

    def _remove(self, scene: Scene) -> bool:
        if scene is None or scene.guid not in self._guid_to_scene:
            return False
        if not super()._remove(scene):
            return False
        del self._guid_to_scene[scene.guid]
        return True

    def _add(self, scene: Scene) -> bool:
        if scene.guid in self._guid_to_scene:
            return False
        if not super()._add(scene):
            return False
        self._guid_to_scene[scene.guid] = scene
        return True

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        scene = self.with_guid(guid)

        if not super()._remove(scene):
            return False
        
        del self._guid_to_scene[scene.guid]
        return True

    def with_guid(self, guid: Union[str, UUID]) -> Scene:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_scene.get(guid, None)

    def first_with_name(self, name: str) -> Optional[Scene]:
        for scene in self:
            if scene.name == name:
                return scene
        return None

    def with_name(self, name: str) -> SceneCollection:
        return SceneCollection(
            [scene for scene in self if scene.name == name]
        )