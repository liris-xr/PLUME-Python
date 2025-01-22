from dataclasses import dataclass
import numpy as np

@dataclass
class Quaternion:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0

    @property
    def to_numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z, self.w], dtype=np.float32)