from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Type
from .samples.record_pb2 import RecordMetadata

from google.protobuf.message import Message

T = TypeVar('T', bound=Message)


@dataclass(frozen=True, slots=True, kw_only=True)
class Sample(Generic[T]):
    # Timestamp in nanoseconds relative to the start of the record
    timestamp: Optional[int]
    payload: T

    def is_timestamped(self):
        return self.timestamp is not None


@dataclass(frozen=True, slots=True)
class FrameDataSample(Sample[T]):
    frame_number: int


@dataclass(frozen=True, slots=True)
class FrameInfo:
    frame_number: int
    timestamp: int


@dataclass(frozen=True)
class Record:
    samples_by_type: dict[Type[T], list[Sample[T]]]
    frames_info: list[FrameInfo]
    first_timestamp: Optional[int]
    last_timestamp: Optional[int]

    def __getitem__(self, item: Type[T]) -> list[Sample[T]]:
        return self.get_samples_by_type(item)

    def get_metadata(self) -> RecordMetadata:
        if RecordMetadata not in self.samples_by_type:
            raise ValueError("The record does not contain any metadata.")
        return self.samples_by_type[RecordMetadata][0].payload

    def get_frame_count(self) -> int:
        return len(self.frames_info)

    def get_samples_by_type(self, payload_type: Type[T]) -> list[Sample[T]]:
        return self.samples_by_type.get(payload_type, [])

    def get_samples_in_time_range(self, start: Optional[int], end: Optional[int]) -> dict[Type[T], list[Sample[T]]]:
        samples_in_time_range = {}
        for payload_type, samples in self.samples_by_type.items():
            samples_in_time_range[payload_type] = [sample for sample in samples if
                                                   (start is None or sample.timestamp >= start) and
                                                   (end is None or sample.timestamp <= end)]
        return samples_in_time_range

    def get_samples_by_type_in_time_range(self, start: Optional[int], end: Optional[int],
                                          payload_type: Type[T]) -> list[Sample[T]]:
        return [sample for sample in self.samples_by_type[payload_type] if
                (start is None or sample.timestamp >= start) and
                (end is None or sample.timestamp <= end)]

    def get_sample_timestamp_since_epoch(self, sample: Sample) -> int:
        """Returns the absolute timestamp of the sample since epoch in nanoseconds."""
        if RecordMetadata not in self.samples_by_type:
            raise ValueError("Unable to determine the absolute timestamp due to missing metadata sample in the record.")
        metadata = self.samples_by_type[RecordMetadata][0].payload
        return metadata.start_time.ToNanoseconds() + sample.timestamp
