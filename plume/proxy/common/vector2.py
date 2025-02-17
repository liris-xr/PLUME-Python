from __future__ import annotations
import numpy as np

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2:
    x: float = 0.0
    y: float = 0.0

    def numpy(self) -> np.ndarray:
        return np.array([self._x, self._y], dtype=np.float32)

    def __array__(self) -> np.ndarray:
        return self.numpy()
