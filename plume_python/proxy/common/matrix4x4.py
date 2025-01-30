from __future__ import annotations
import numpy as np

from dataclasses import dataclass

@dataclass(frozen=True)
class Matrix4x4:
    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m03: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m13: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0
    m23: float = 0.0
    m30: float = 0.0
    m31: float = 0.0
    m32: float = 0.0
    m33: float = 0.0

    def to_numpy(self) -> np.ndarray:
        return np.array(
            [
                [self.m00, self.m01, self.m02, self.m03],
                [self.m10, self.m11, self.m12, self.m13],
                [self.m20, self.m21, self.m22, self.m23],
                [self.m30, self.m31, self.m32, self.m33],
            ],
            dtype=np.float32,
        )
    
    def __repr__(self) -> str:
        return f"Matrix4x4([[{self.m00:.2f}, {self.m01:.2f}, {self.m02:.2f}, {self.m03:.2f}], [{self.m10:.2f}, {self.m11:.2f}, {self.m12:.2f}, {self.m13:.2f}], [{self.m20:.2f}, {self.m21:.2f}, {self.m22:.2f}, {self.m23:.2f}], [{self.m30:.2f}, {self.m31:.2f}, {self.m32:.2f}, {self.m33:.2f}])"
    
    def deepcopy(self) -> Matrix4x4:
        return Matrix4x4(
            self.m00,
            self.m01,
            self.m02,
            self.m03,
            self.m10,
            self.m11,
            self.m12,
            self.m13,
            self.m20,
            self.m21,
            self.m22,
            self.m23,
            self.m30,
            self.m31,
            self.m32,
            self.m33,
        )