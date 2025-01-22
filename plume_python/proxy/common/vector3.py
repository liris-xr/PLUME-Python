from dataclasses import dataclass
import numpy as np

@dataclass
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @property
    def to_numpy(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z], dtype=np.float32)