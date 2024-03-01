from google.protobuf.message_factory import GetMessageClass
from google.protobuf.message import Message
from google.protobuf.any_pb2 import Any
from google.protobuf import descriptor_pool
from delimited_protobuf import read as _read_delimited

from warnings import warn
from typing import BinaryIO, TypeVar, Any

from plume.samples import packed_sample_pb2, record_pb2
from plume.samples.common import marker_pb2
from plume.samples.lsl import stream_sample_pb2
from plume.samples.unity import frame_pb2
from plume.record import Record, Sample, Frame
from plume.filtering import filter_samples
from plume import file_reader

# Required to add all DESCRIPTORS into the default descriptor pool
from plume.samples import *
__default_descriptor_pool = descriptor_pool.Default()

T = TypeVar('T', bound=Message)

def unpack_any(any: Any, descriptor_pool: descriptor_pool.DescriptorPool) -> Message:
    """Unpacks an Any message into its original type using the provided descriptor pool."""
    descriptor = descriptor_pool.FindMessageTypeByName(any.TypeName())
    unpacked = GetMessageClass(descriptor)()

    try:
        success = any.Unpack(unpacked)
    except:
        warn(f"Failed to unpack payload with type name {any.TypeName()} and at timestamp {any.timestamp}")
        success = False

    if not success:
        return None

    return unpacked

def unpack_frame(packed_sample: Sample[frame_pb2.Frame], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> Frame:
    """Unpacks a sample containing a payload of type Frame into an unpacked frame."""
    packed_frame: frame_pb2.Frame = packed_sample.payload
    unpacked_frame_data: list[Message] = []

    for data in packed_frame.data:
        unpacked_data: Message = unpack_any(data, descriptor_pool)
        if unpacked_data is None:
            warn(f"Failed to unpack frame data with type name {data.type_url}")
            continue
        unpacked_frame_data.append(Sample(timestamp=packed_sample.timestamp, payload=unpacked_data))
    return Frame(timestamp=packed_sample.timestamp, frame_number=packed_frame.frame_number, data=unpacked_frame_data)

def unpack_frames(packed_samples: list[Sample[frame_pb2.Frame]], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> list[Frame]:
    """Unpacks a list of samples containing a payload of type Frame into a list of unpacked frames."""
    frames: list[Frame] = []
    for packed_sample in packed_samples:
        unpacked_frame = unpack_frame(packed_sample, descriptor_pool)
        if unpacked_frame is not None:
            frames.append(unpacked_frame)
    return frames

def unpack_sample(packed_sample: packed_sample_pb2.PackedSample, descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> Sample:
    """Unpacks the payload of a packed sample using the provided descriptor pool and returns an unpacked sample."""
    unpacked_payload = unpack_any(packed_sample.payload, descriptor_pool)
    if unpacked_payload is None:
        warn(f"Failed to unpack payload with type name {packed_sample.payload.type_url}")
    timestamp = packed_sample.timestamp if packed_sample.HasField("timestamp") else None
    return Sample(timestamp=timestamp, payload=unpacked_payload)

def unpack_samples(packed_samples: list[packed_sample_pb2.PackedSample], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> list[Sample]:
    """Unpacks the payload of each packed samples in the list using the provided descriptor pool and returns a list of unpacked samples."""
    samples: list[Sample] = []
    for packed_sample in packed_samples:
        unpacked_sample = unpack_sample(packed_sample, descriptor_pool)
        if unpacked_sample is not None:
            samples.append(unpacked_sample)
    return samples

def parse_record_from_stream(data_stream: BinaryIO) -> Record:
    """Parses a record from a binary stream and returns a record object."""
    packed_samples = parse_packed_samples_from_stream(data_stream)
    samples = unpack_samples(packed_samples)
    metadata = filter_samples(samples, record_pb2.RecordMetadata)

    if len(metadata) == 0 or metadata is None:
        warn("No metadata found in the record")
        metadata = None

    packed_frames = filter_samples(samples, frame_pb2.Frame)
    packed_markers = filter_samples(samples, marker_pb2.Marker)
    packed_lsl_samples = filter_samples(samples, stream_sample_pb2.StreamSample)
    frames = unpack_frames(packed_frames)
    return Record(metadata=metadata, samples=samples, frames=frames, lsl_samples=packed_lsl_samples, markers=packed_markers)

def parse_record_from_file(filepath: str) -> Record:
    """Parses a record from a file and returns a record object."""
    data_stream = file_reader.read_file(filepath)
    return parse_record_from_stream(data_stream)

def parse_packed_samples_from_stream(data_stream: BinaryIO) -> list[packed_sample_pb2.PackedSample]:
    """Parses packed samples from a binary stream and returns a list of packed samples."""
    unpacked_samples = []

    while data_stream.tell() < len(data_stream.getbuffer()):
        packed_sample = _read_delimited(data_stream, packed_sample_pb2.PackedSample)

        if packed_sample is not None:
            unpacked_samples.append(packed_sample)

    return unpacked_samples

def parse_packed_samples_from_file(filepath: str) -> list[packed_sample_pb2.PackedSample]:
    """Parses packed samples from a file and returns a list of packed samples."""
    data_stream = file_reader.read_file(filepath)
    return parse_packed_samples_from_stream(data_stream)