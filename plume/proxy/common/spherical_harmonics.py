from __future__ import annotations

from dataclasses import dataclass

from plume.proxy.common.vector4 import Vector4

@dataclass(frozen=True)
class SphericalHarmonicsL1:
    sh_ar: Vector4 = Vector4()
    sh_ag: Vector4 = Vector4()
    sh_ab: Vector4 = Vector4()
    
@dataclass(frozen=True)
class SphericalHarmonicsL2:
    shr0: float = 0.0
    shr1: float = 0.0
    shr2: float = 0.0
    shr3: float = 0.0
    shr4: float = 0.0
    shr5: float = 0.0
    shr6: float = 0.0
    shr7: float = 0.0
    shr8: float = 0.0
    shg0: float = 0.0
    shg1: float = 0.0
    shg2: float = 0.0
    shg3: float = 0.0
    shg4: float = 0.0
    shg5: float = 0.0
    shg6: float = 0.0
    shg7: float = 0.0
    shg8: float = 0.0
    shb0: float = 0.0
    shb1: float = 0.0
    shb2: float = 0.0
    shb3: float = 0.0
    shb4: float = 0.0
    shb5: float = 0.0
    shb6: float = 0.0
    shb7: float = 0.0
    shb8: float = 0.0
