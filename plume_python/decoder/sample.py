from dataclasses import dataclass
from typing import TypeVar, Generic, Optional
from google.protobuf.message import Message

T = TypeVar("T", bound=Message)

@dataclass(frozen=True, slots=True, kw_only=True)
class Sample(Generic[T]):
    # Timestamp in nanoseconds relative to the start of the record
    time_ns: Optional[int]
    payload: T

    @property
    def has_timestamp(self):
        return self.time_ns is not None