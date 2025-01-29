from __future__ import annotations
import numpy as np


class Quaternion:
    _x: float
    _y: float
    _z: float
    _w: float

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

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
    def w(self) -> float:
        return self._w

    @property
    def to_numpy(self) -> np.ndarray:
        return np.array([self._x, self._y, self._z, self._w], dtype=np.float32)

    def __repr__(self) -> str:
        return f"Quaternion(x={self._x}, y={self._y}, z={self._z}, w={self._w})"

    def deepcopy(self) -> Quaternion:
        return Quaternion(self._x, self._y, self._z, self._w)
