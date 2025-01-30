from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Rect:
    x: float = 0.0
    y: float = 0.0
    width: float = 0.0
    height: float = 0.0

    def deepcopy(self) -> Rect:
        return Rect(
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height,
        )