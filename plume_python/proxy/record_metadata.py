from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class RecorderVersion:
    name: str
    major: int
    minor: int
    patch: int

    def __str__(self):
        return f"{self.name} {self.major}.{self.minor}.{self.patch}"

@dataclass(frozen=True)
class RecordMetadata:
    recorder_version: RecorderVersion
    start_timestamp: datetime
    name: str
    extra_metadata: str

    def __str__(self):
        return f"Record: {self.name} ({self.recorder_version})"