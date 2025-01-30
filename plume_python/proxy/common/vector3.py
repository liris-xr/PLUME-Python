from __future__ import annotations
import numpy as np


class Vector3:
    _x: float
    _y: float
    _z: float

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    @property
    def to_numpy(self) -> np.ndarray:
        return np.array([self._x, self._y, self._z], dtype=np.float32)

    def __repr__(self):
        return f"Vector3(x={self._x:.2f}, y={self._y:.2f}, z={self._z:.2f})"

    def deepcopy(self) -> Vector3:
        return Vector3(self._x, self._y, self._z)
