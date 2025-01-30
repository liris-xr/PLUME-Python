from __future__ import annotations
from plume_python.proxy.unity.scene import SceneCollection
from plume_python.proxy.unity.asset import AssetCollection
from plume_python.proxy.unity.xritk_interaction import XRITKInteractionCollection
from typing import Optional, List


class Frame:
    _time_ns: int
    _frame_number: int
    _scenes: SceneCollection
    _assets: AssetCollection
    _xritk_interactions: XRITKInteractionCollection

    def __init__(
        self,
        time_ns: int = 0,
        frame_number: int = 0,
        scenes: Optional[SceneCollection] = None,
        assets: Optional[AssetCollection] = None,
        xritk_interactions: Optional[XRITKInteractionCollection] = None,
    ):
        self._time_ns = time_ns
        self._frame_number = frame_number
        self._scenes = scenes if scenes else SceneCollection()
        self._assets = assets if assets else AssetCollection()
        self._xritk_interactions = xritk_interactions if xritk_interactions else []

    def deepcopy(self) -> Frame:
        copy = Frame(
            time_ns=self._time_ns,
            frame_number=self._frame_number,
            scenes=self._scenes.deepcopy(),
            assets=self._assets.deepcopy(),
            xritk_interactions=[interaction.deepcopy() for interaction in self._xritk_interactions]
        )
        return copy

    @property
    def frame_number(self) -> int:
        return self._frame_number

    @property
    def frame_number(self) -> int:
        return self._frame_number

    @property
    def scenes(self) -> SceneCollection:
        return self._scenes
    
    @property
    def assets(self) -> AssetCollection:
        return self._assets
    
    @property
    def xritk_interactions(self) -> XRITKInteractionCollection:
        return self._xritk_interactions

    @property
    def time_ns(self) -> int:
        return self._time_ns

    @property
    def time_s(self) -> float:
        return self._time_ns / 1e9

    def __repr__(self):
        return f"Frame(frame_number={self._frame_number}, scenes={[scene.name for scene in self._scenes]}, time_ns={self._time_ns})"