from __future__ import annotations
import numpy as np

from dataclasses import dataclass

@dataclass(frozen=True)
class Vector2:
    x: float = 0.0
    y: float = 0.0

    def to_numpy(self) -> np.ndarray:
        return np.array([self._x, self._y], dtype=np.float32)
