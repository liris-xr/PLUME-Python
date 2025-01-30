from __future__ import annotations

from dataclasses import dataclass

from plume_python.proxy.common.vector4 import Vector4

@dataclass(frozen=True)
class SphericalHarmonicsL1:
    sh_ar: Vector4 = Vector4()
    sh_ag: Vector4 = Vector4()
    sh_ab: Vector4 = Vector4()

    def deepcopy(self) -> SphericalHarmonicsL1:
        return SphericalHarmonicsL1(
            sh_ar=self.sh_ar.deepcopy(),
            sh_ag=self.sh_ag.deepcopy(),
            sh_ab=self.sh_ab.deepcopy(),
        )
    
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

    def deepcopy(self) -> SphericalHarmonicsL2:
        return SphericalHarmonicsL2(
            shr0=self.shr0,
            shr1=self.shr1,
            shr2=self.shr2,
            shr3=self.shr3,
            shr4=self.shr4,
            shr5=self.shr5,
            shr6=self.shr6,
            shr7=self.shr7,
            shr8=self.shr8,
            shg0=self.shg0,
            shg1=self.shg1,
            shg2=self.shg2,
            shg3=self.shg3,
            shg4=self.shg4,
            shg5=self.shg5,
            shg6=self.shg6,
            shg7=self.shg7,
            shg8=self.shg8,
            shb0=self.shb0,
            shb1=self.shb1,
            shb2=self.shb2,
            shb3=self.shb3,
            shb4=self.shb4,
            shb5=self.shb5,
            shb6=self.shb6,
            shb7=self.shb7,
            shb8=self.shb8,
        )