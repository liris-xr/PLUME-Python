from __future__ import annotations

class Marker:
    _label: str
    _time_ns: int

    def __init__(self, label: str, time_ns: int):
        self._label = label
        self._time_ns = time_ns

    @property
    def time_s(self) -> float:
        return self._time_ns / 1e9

    def __repr__(self) -> str:
        return f"Marker(label='{self._label}', time_ns={self._time_ns})"

    def deepcopy(self) -> Marker:
        return Marker(label=self._label, time_ns=self._time_ns)