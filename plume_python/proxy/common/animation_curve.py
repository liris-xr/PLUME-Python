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
    
@dataclass(frozen=True)
class AnimationCurve:
    key_frames: List[KeyFrame]