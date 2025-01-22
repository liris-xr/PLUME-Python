from typing import List
from plume_python.proxy.unity.gameobject import GameObject
from enum import Enum

class SceneLoadMode(Enum):
    SINGLE = 0
    ADDITIVE = 1

class Scene:
    _uuid: str
    _runtime_idx: int
    _build_idx: int
    _name: str
    _path: str
    _mode: SceneLoadMode

    _game_objects: List[GameObject]

    def __init__(self, uuid: str, runtime_idx: int, build_idx: int, name: str, path: str, mode: SceneLoadMode):
        self._uuid = uuid
        self._runtime_idx = runtime_idx
        self._build_idx = build_idx
        self._name = name
        self._path = path
        self._mode = mode
        self._game_objects = []

    def _add_game_object(self, game_object: GameObject):
        if game_object in self._game_objects:
            raise ValueError('GameObject already belongs to this Scene')
        if game_object._scene is not None and game_object._scene != self:
            raise ValueError('GameObject already belongs to another Scene')
        game_object._scene = self
        self._game_objects.append(game_object)

    def _remove_game_object(self, game_object: GameObject):
        if game_object._scene != self:
            raise ValueError('GameObject does not belong to this Scene')
        if game_object not in self._game_objects:
            raise ValueError('GameObject does not belong to this Scene')
        game_object._scene = None
        self._game_objects.remove(game_object)

    def __hash__(self):
        return hash(self._uuid)

    @property
    def uuid(self) -> str:
        return self._uuid
    
    @property
    def runtime_idx(self) -> int:
        return self._runtime_idx
    
    @property
    def build_idx(self) -> int:
        return self._build_idx
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def path(self) -> str:
        return self._path
    
    @property
    def mode(self) -> SceneLoadMode:
        return self._mode
    
    @property
    def game_objects(self) -> List[GameObject]:
        return self._game_objects.copy()
