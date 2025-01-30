from __future__ import annotations

from dataclasses import dataclass
from typing import List

from enum import Enum

class WeightedMode(Enum):
    UNSPECIFIED = 0
    IN = 1
    OUT = 2
    BOTH = 3

@dataclass(frozen=True)
class KeyFrame:
    time: float
    value: float
    in_tangent: float
    out_tangent: float
    weighted_mode: WeightedMode
    in_weight: float
    out_weight: float

    def deepcopy(self) -> KeyFrame:
        return KeyFrame(
            time=self.time,
            value=self.value,
            weighted_mode=self.weighted_mode,
            in_tangent=self.in_tangent,
            out_tangent=self.out_tangent,
            in_weight=self.in_weight,
            out_weight=self.out_weight,
        )
    
@dataclass(frozen=True)
class AnimationCurve:
    key_frames: List[KeyFrame]

    def deepcopy(self) -> AnimationCurve:
        return AnimationCurve(
            key_frames=[key_frame.deepcopy() for key_frame in self.key_frames],
        )