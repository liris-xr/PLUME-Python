from __future__ import annotations
import numpy as np
from dataclasses import dataclass

from typing import List

from enum import Enum

@dataclass(frozen=True)
class Color:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0

    def to_numpy(self) -> np.ndarray:
        return np.array([self.r, self.g, self.b, self.a], dtype=np.float32)
    
    def to_hex(self) -> str:
        return f"#{int(self.r * 255):02x}{int(self.g * 255):02x}{int(self.b * 255):02x}{int(self.a * 255):02x}"

    def deepcopy(self) -> Color:
        return Color(r=self.r, g=self.g, b=self.b)

class ColorSpace(Enum):
    UNSPECIFIED = 0
    GAMMA = 1
    LINEAR = 2

class GradientMode(Enum):
    UNSPECIFIED = 0
    BLEND = 1
    FIXED = 2
    PERCEPTUAL_BLEND = 3

@dataclass(frozen=True)
class ColorGradient:
    color_space: ColorSpace
    gradient_mode: GradientMode
    color_keys: List[Color]
    alpha_keys: List[float]

    def __post_init__(self):
        if len(self.color_keys) != len(self.alpha_keys):
            raise ValueError("Color keys and alpha keys must have the same length")