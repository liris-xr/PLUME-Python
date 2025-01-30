from __future__ import annotations

from dataclasses import dataclass

from plume_python.proxy.common.vector3 import Vector3

@dataclass(frozen=True)
class Bounds:
    center: Vector3 = Vector3()
    size: Vector3 = Vector3()

    def deepcopy(self) -> Bounds:
        return Bounds(
            center=self.center.deepcopy(),
            size=self.size.deepcopy(),
        )