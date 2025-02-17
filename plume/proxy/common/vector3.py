from __future__ import annotations
import numpy as np

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z], dtype=np.float32)

    def __array__(self) -> np.ndarray:
        return self.numpy()
