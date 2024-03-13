from plume.samples import record_pb2
from plume.samples.unity import frame_pb2
from plume.samples.lsl import lsl_stream_pb2
from plume.samples.common.marker_pb2 import Marker
from typing import TypeVar, Generic, Optional
from google.protobuf.message import Message
from datetime import datetime

from dataclasses import dataclass
from abc import ABC

T = TypeVar('T', bound=Message)


@dataclass(frozen=True)
class Sample(ABC):
    # Timestamp in nanoseconds relative to the start of the record
    timestamp: Optional[int]
    
    def __new__(cls, *args, **kwargs):
        if cls == Sample: 
            raise TypeError("Cannot instantiate abstract sample.") 
        return super().__new__(cls)

    def is_timestamped(self):
        return self.timestamp is not None


@dataclass(frozen=True)
class RawSample(Sample, Generic[T]):
    payload: T


@dataclass(frozen=True)
class FrameSample(Sample):
    # This corresponds to the in-game frame number and *NOT* the index of the frame in the record
    frame_number: int
    data: list[RawSample]


@dataclass(frozen=True)
class MarkerSample(Sample):
    label: str


@dataclass(frozen=True)
class LslStreamInfo():
    # Stream unique identifier this data comes from
    stream_id: str
    # XML containing channel format, number of channels, metadata, etc
    xml_header: str


@dataclass(frozen=True)
class LslSample(Sample):
    stream_id: str
    channel_values: list[float | int | str]


@dataclass(frozen=True)
class LslOpenStream(Sample):
    stream_id: str
    xml_header: str


@dataclass(frozen=True)
class LslCloseStream(Sample):
    stream_id: str


@dataclass(frozen=True)
class RecorderVersion:
    name: str
    major: str
    minor: str
    patch: str


@dataclass(frozen=True)
class RecordMetadata():
    start_time: datetime
    name: str
    extra_metadata: str
    recorder_version: RecorderVersion


@dataclass(frozen=True)
class Record():
    metadata: RecordMetadata
    frames: list[FrameSample]
    lsl_samples: list[LslSample]
    lsl_open_streams: list[LslOpenStream]
    lsl_close_streams: list[LslCloseStream]
    markers: list[MarkerSample]
    raw_samples: list[RawSample]