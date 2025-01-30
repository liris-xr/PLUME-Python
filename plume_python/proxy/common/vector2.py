from __future__ import annotations
import numpy as np


class Vector2:
    _x: float
    _y: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def to_numpy(self) -> np.ndarray:
        return np.array([self._x, self._y], dtype=np.float32)

    def __repr__(self):
        return f"Vector3(x={self._x:.2f}, y={self._y:.2f})"

    def deepcopy(self) -> Vector2:
        return Vector2(self._x, self._y)
