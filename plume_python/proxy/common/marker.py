from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Marker:
    label: str
    time_ns: int

    @property
    def time_s(self) -> float:
        return self.time_ns / 1e9

    def deepcopy(self) -> Marker:
        return Marker(label=self.label, time_ns=self.time_ns)