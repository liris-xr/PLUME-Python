from plume.samples.record_pb2 import RecordMetadata
from plume.samples.unity.frame_pb2 import Frame
from plume.samples.lsl.stream_sample_pb2 import StreamSample
from plume.samples.lsl.stream_close_pb2 import StreamClose
from plume.samples.lsl.stream_open_pb2 import StreamOpen
from plume.samples.common.marker_pb2 import Marker
from typing import TypeVar, Generic, Optional
from google.protobuf.message import Message

from dataclasses import dataclass

T = TypeVar('T', bound=Message)

@dataclass(frozen=True)
class Sample(Generic[T]):
    timestamp: Optional[int]
    payload: T
    
    def is_timestamped(self):
        return self.timestamp is not None

@dataclass(frozen=True)
class Frame():
    timestamp: int
    frame_number: int
    data: list[Sample]

@dataclass(frozen=True)
class Record():
    metadata: RecordMetadata
    frames: list[Frame]
    lsl_samples: list[Sample[StreamOpen | StreamClose | StreamSample]]
    markers: list[Sample[Marker]]
    samples: list[Sample]