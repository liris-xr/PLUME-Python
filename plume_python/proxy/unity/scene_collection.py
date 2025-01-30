from __future__ import annotations

from plume_python.proxy.unity.scene import Scene
from typing import List, Union, Optional, Iterable, Iterator
from uuid import UUID

class SceneCollection(Iterable[Scene]):
    _scenes: List[Scene]
    _guid_to_scene: dict[UUID, Scene]

    def __init__(self, scenes: List[Scene] = []):
        self._scenes = scenes.copy()
        self._guid_to_scene = {scene.guid: scene for scene in self._scenes}

    def __len__(self) -> int:
        return len(self._scenes)

    def __getitem__(self, index: int) -> Scene:
        return self._scenes[index]

    def __iter__(self) -> Iterator[Scene]:
        return iter(self._scenes)

    def __contains__(self, scene: Scene) -> bool:
        return scene in self._scenes

    def _remove(self, scene: Scene) -> bool:
        if scene is None or scene.guid not in self._guid_to_scene:
            return False
        self._scenes.remove(scene)
        del self._guid_to_scene[scene.guid]
        return True

    def _add(self, scene: Scene):
        self._scenes.append(scene)
        self._guid_to_scene[scene.guid] = scene

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        scene = self.get_by_guid(guid)
        return self._remove(scene)
    
    def __hash__(self) -> int:
        return hash(self._scenes)

    def with_guid(self, guid: Union[str, UUID]) -> Scene:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_scene.get(guid, None)

    def first_with_name(self, name: str) -> Optional[Scene]:
        for scene in self._scenes:
            if scene.name == name:
                return scene
        return None

    def with_name(self, name: str) -> SceneCollection:
        return SceneCollection(
            [scene for scene in self._scenes if scene.name == name]
        )

    def __repr__(self) -> str:
        return f"SceneCollection(scenes={[scene.name for scene in self._scenes]})"
