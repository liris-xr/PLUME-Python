from typing import BinaryIO, Any, Optional, TypeVar, cast, Type
from warnings import warn

from delimited_protobuf import read as _read_delimited
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf.message import Message
from google.protobuf.message_factory import GetMessageClass

from . import file_reader
from .record import Record, Sample, FrameDataSample, FrameInfo
from .samples import packed_sample_pb2, default_descriptor_pool
from .samples.unity import frame_pb2

T = TypeVar('T', bound=Message)


def unpack_any(any_payload: Any, descriptor_pool: _descriptor_pool.DescriptorPool) -> Optional[Message]:
    """Unpacks an Any message into its original type using the provided descriptor pool."""
    try:
        descriptor = descriptor_pool.FindMessageTypeByName(any_payload.TypeName())
        unpacked = GetMessageClass(descriptor)()
        success = any_payload.Unpack(unpacked)
        if not success:
            warn(f"Failed to unpack payload with type name {any_payload.TypeName()}")
            return None
        return unpacked
    except KeyError:
        return None


def parse_record_from_stream(data_stream: BinaryIO) -> Record:
    """Parses a record from a binary stream and returns a record object."""
    packed_samples = parse_packed_samples_from_stream(data_stream)

    samples_by_type: dict[Type[T], list[Sample[T]]] = {}
    frames_info: list[FrameInfo] = []
    first_timestamp: Optional[int] = None
    last_timestamp: Optional[int] = None

    for packed_sample in packed_samples:

        unpacked_payload = unpack_any(packed_sample.payload, default_descriptor_pool)
        if unpacked_payload is None:
            continue
        timestamp = packed_sample.timestamp if packed_sample.HasField("timestamp") else None

        if timestamp is not None:
            last_timestamp = timestamp if last_timestamp is None else max(last_timestamp, timestamp)
            if first_timestamp is None:
                first_timestamp = timestamp

        if isinstance(unpacked_payload, frame_pb2.Frame):
            frame = cast(frame_pb2.Frame, unpacked_payload)
            frames_info.append(FrameInfo(frame_number=frame.frame_number, timestamp=timestamp))

            for packed_frame_data in frame.data:
                unpacked_frame_data = unpack_any(packed_frame_data, default_descriptor_pool)
                if unpacked_frame_data is None:
                    continue
                frame_data_sample = FrameDataSample(timestamp=timestamp,
                                                    frame_number=frame.frame_number,
                                                    payload=unpacked_frame_data)
                payload_type = type(unpacked_frame_data)
                samples_by_type.setdefault(payload_type, list[FrameDataSample[T]]()).append(frame_data_sample)
        else:
            sample = Sample(timestamp=timestamp, payload=unpacked_payload)
            payload_type = type(unpacked_payload)
            samples_by_type.setdefault(payload_type, list[Sample[T]]()).append(sample)

    return Record(samples_by_type=samples_by_type, frames_info=frames_info,
                  first_timestamp=first_timestamp, last_timestamp=last_timestamp)


def parse_record_from_file(filepath: str) -> Record:
    """Parses a record from a file and returns a record object."""
    data_stream = file_reader.read_file(filepath)
    return parse_record_from_stream(data_stream)


def parse_packed_samples_from_stream(data_stream: BinaryIO) -> list[packed_sample_pb2.PackedSample]:
    """Parses packed samples from a binary stream and returns a list of packed samples."""
    packed_samples = []

    while data_stream.tell() < len(data_stream.getbuffer()):
        packed_sample = _read_delimited(data_stream, packed_sample_pb2.PackedSample)

        if packed_sample is not None:
            packed_samples.append(packed_sample)

    return packed_samples


def parse_packed_samples_from_file(filepath: str) -> list[packed_sample_pb2.PackedSample]:
    """Parses packed samples from a file and returns a list of packed samples."""
    data_stream = file_reader.read_file(filepath)
    return parse_packed_samples_from_stream(data_stream)
