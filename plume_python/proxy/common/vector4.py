from __future__ import annotations
import numpy as np

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector4:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0

    def numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z, self.w], dtype=np.float32)
