from __future__ import annotations
import numpy as np

from plume.proxy.common.vector3 import Vector3
from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Quaternion:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0

    def numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z, self.w], dtype=np.float32)

    @staticmethod
    def from_matrix(matrix: np.ndarray) -> Quaternion:
        if matrix.shape != (3, 3):
            raise ValueError(f"Invalid rotation matrix shape {matrix.shape}")

        m00, m01, m02 = matrix[0]
        m10, m11, m12 = matrix[1]
        m20, m21, m22 = matrix[2]

        q_abs = np.sqrt(
            np.maximum(
                0,
                np.array(
                    [
                        1.0 + m00 + m11 + m22,
                        1.0 + m00 - m11 - m22,
                        1.0 - m00 + m11 - m22,
                        1.0 - m00 - m11 + m22,
                    ]
                ),
            )
        )

        quat_by_rijk = np.array(
            [
                [q_abs[0] ** 2, m21 - m12, m02 - m20, m10 - m01],
                [m21 - m12, q_abs[1] ** 2, m10 + m01, m02 + m20],
                [m02 - m20, m10 + m01, q_abs[2] ** 2, m12 + m21],
                [m10 - m01, m20 + m02, m21 + m12, q_abs[3] ** 2],
            ]
        )

        flr = 0.1
        q_abs_max = np.maximum(q_abs[:, None], flr)
        quat_candidates = quat_by_rijk / (2.0 * q_abs_max)

        max_idx = q_abs.argmax()
        out = quat_candidates[max_idx]

        # Standardize quaternion
        norm = np.linalg.norm(out)
        if out[0] < 0:
            out = -out
        out = out / norm

        return Quaternion(out[1], out[2], out[3], out[0])

    def normalize(self) -> Quaternion:
        norm = sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
        return Quaternion(self.x / norm, self.y / norm, self.z / norm, self.w / norm)

    def to_euler(self) -> Vector3:
        q0, q1, q2, q3 = self.w, self.x, self.y, self.z
        roll = np.arctan2(2 * (q0 * q1 + q2 * q3), q0**2 - q1**2 - q2**2 + q3**2)
        pitch = np.arcsin(2 * (q0 * q2 - q3 * q1))
        yaw = np.arctan2(2 * (q0 * q3 + q1 * q2), q0**2 + q1**2 - q2**2 - q3**2)
        return Vector3(roll, pitch, yaw)

    def as_matrix(self) -> np.ndarray:
        r, i, j, k = self.w, self.x, self.y, self.z

        m00 = r**2 + i**2 - j**2 - k**2
        m01 = 2 * (i * j - r * k)
        m02 = 2 * (i * k + r * j)

        m10 = 2 * (i * j + r * k)
        m11 = r**2 - i**2 + j**2 - k**2
        m12 = 2 * (j * k - r * i)

        m20 = 2 * (i * k - r * j)
        m21 = 2 * (j * k + r * i)
        m22 = r**2 - i**2 - j**2 + k**2

        return np.array(
            [[m00, m01, m02], [m10, m11, m12], [m20, m21, m22]], dtype=np.float32
        )
