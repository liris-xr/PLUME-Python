from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Rect:
    x: float = 0.0
    y: float = 0.0
    width: float = 0.0
    height: float = 0.0
