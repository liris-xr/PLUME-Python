from google.protobuf.message_factory import GetMessageClass
from google.protobuf.message import Message
from google.protobuf.any_pb2 import Any
from google.protobuf import descriptor_pool
from delimited_protobuf import read as _read_delimited

from warnings import warn
from typing import BinaryIO, TypeVar, Any

from plume.samples import packed_sample_pb2, record_pb2
from plume.samples.common import marker_pb2
from plume.samples.lsl import stream_sample_pb2, stream_close_pb2, stream_open_pb2, stream_info_pb2
from plume.samples.unity import frame_pb2
from plume.record import Record, FrameSample, MarkerSample, RawSample, LslSample, RecordMetadata, RecorderVersion
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

def parse_raw_marker_sample(raw_marker_sample: RawSample[marker_pb2.Marker]) -> MarkerSample:
    """Unpacks a sample containing a payload of type Marker into a MarkerSample."""
    unpacked_marker = marker_pb2.Marker()
    raw_marker_sample.payload.Unpack(unpacked_marker)
    if unpacked_marker is None:
        warn(f"Failed to unpack marker")
        return None
    return MarkerSample(timestamp=raw_marker_sample.timestamp, label=unpacked_marker.label)

def parse_raw_marker_samples(raw_marker_samples: list[RawSample[marker_pb2.Marker]]) -> list[MarkerSample]:
    """Unpacks a list of markers into a list of MarkerSamples."""
    marker_samples: list[MarkerSample] = []
    for packed_sample in raw_marker_samples:
        marker_sample = parse_raw_marker_sample(packed_sample)
        if marker_sample is not None:
            marker_samples.append(marker_sample)
    return marker_samples

def parse_raw_lsl_sample(raw_lsl_sample: RawSample[stream_sample_pb2.StreamSample]) -> LslSample:
    """Unpacks a sample containing a payload of type StreamSample into an LslSample."""
    stream_info = raw_lsl_sample.payload.stream_info
    values: list[float | int | str] = []
    value_case = raw_lsl_sample.payload.WhichOneof("values")
    if value_case == "string_value":
        values = raw_lsl_sample.payload.string_value.value
    elif value_case == "float_value":
        values = raw_lsl_sample.payload.float_value.value
    elif value_case == "double_value":
        values = raw_lsl_sample.payload.double_value.value
    elif value_case == "int8_value":
        values = raw_lsl_sample.payload.int8_value.value
    elif value_case == "int16_value":
        values = raw_lsl_sample.payload.int16_value.value
    elif value_case == "int32_value":
        values = raw_lsl_sample.payload.int32_value.value
    elif value_case == "int64_value":
        values = raw_lsl_sample.payload.int64_value.value
    else:
        warn(f"Failed to parse raw lsl sample with value type {value_case}")
        return None
    return LslSample(timestamp=raw_lsl_sample.timestamp, stream_info=stream_info, channel_values=values)

def parse_raw_lsl_samples(raw_lsl_samples: list[RawSample[stream_sample_pb2.StreamSample]]) -> list[LslSample]:
    """Unpacks a list of lsl samples into a list of LslSamples."""
    lsl_samples: list[LslSample] = []
    for packed_sample in raw_lsl_samples:
        lsl_sample = parse_raw_lsl_sample(packed_sample)
        if lsl_sample is not None:
            lsl_samples.append(lsl_sample)
    return lsl_samples
    
def parse_raw_frame_sample(raw_frame_sample: RawSample[frame_pb2.Frame], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> FrameSample:
    """Unpacks a sample containing a payload of type Frame into a list of unpacked frame data samples."""
    packed_frame: frame_pb2.Frame = raw_frame_sample.payload
    frame_data_samples: list[RawSample] = []

    for data in packed_frame.data:
        unpacked_data: Message = unpack_any(data, descriptor_pool)
        if unpacked_data is None:
            warn(f"Failed to unpack frame data with type name {data.type_url}")
            continue
        frame_data_samples.append(RawSample(timestamp=raw_frame_sample.timestamp, payload=unpacked_data))
    return FrameSample(timestamp=raw_frame_sample.timestamp, frame_number=packed_frame.frame_number, data=frame_data_samples)

def parse_raw_frame_samples(raw_frame_samples: list[RawSample[frame_pb2.Frame]], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> list[FrameSample]:
    """Unpacks a list of frames into a list of unpacked frame data samples."""
    frame_samples: list[FrameSample] = []
    for packed_sample in raw_frame_samples:
        frame_sample = parse_raw_frame_sample(packed_sample, descriptor_pool)
        if frame_sample is not None:
            frame_samples.append(frame_sample)
    return frame_samples

def unpack_sample(packed_sample: packed_sample_pb2.PackedSample, descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> RawSample:
    """Unpacks the payload of a packed sample using the provided descriptor pool and returns an unpacked sample."""
    unpacked_payload = unpack_any(packed_sample.payload, descriptor_pool)
    if unpacked_payload is None:
        warn(f"Failed to unpack payload with type name {packed_sample.payload.type_url}")
    timestamp = packed_sample.timestamp if packed_sample.HasField("timestamp") else None
    return RawSample(timestamp=timestamp, payload=unpacked_payload)

def unpack_samples(packed_samples: list[packed_sample_pb2.PackedSample], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> list[RawSample]:
    """Unpacks the payload of each packed samples in the list using the provided descriptor pool and returns a list of unpacked samples."""
    raw_samples: list[RawSample] = []
    for packed_sample in packed_samples:
        unpacked_sample = unpack_sample(packed_sample, descriptor_pool)
        if unpacked_sample is not None:
            raw_samples.append(unpacked_sample)
    return raw_samples

def parse_record_from_stream(data_stream: BinaryIO) -> Record:
    """Parses a record from a binary stream and returns a record object."""
    packed_samples = parse_packed_samples_from_stream(data_stream)
    raw_samples = unpack_samples(packed_samples)

    raw_frames: list[RawSample[frame_pb2.Frame]] = []
    raw_markers: list[RawSample[marker_pb2.Marker]] = []
    raw_lsl: list[RawSample[stream_sample_pb2.StreamOpen | stream_sample_pb2.StreamClose | stream_sample_pb2.StreamSample]] = []
    raw_metadata: RawSample[record_pb2.RecordMetadata] = None

    for sample in raw_samples:
        if isinstance(sample.payload, frame_pb2.Frame):
            raw_frames.append(sample)
        elif isinstance(sample.payload, marker_pb2.Marker):
            raw_markers.append(sample)
        elif isinstance(sample.payload, stream_sample_pb2.StreamSample):
            raw_lsl.append(sample)
        elif isinstance(sample.payload, record_pb2.RecordMetadata):
            raw_metadata = sample

    frames: list[FrameSample] = parse_raw_frame_samples(raw_frames)
    markers: list[MarkerSample] = parse_raw_marker_samples(raw_markers)
    lsl_stream_samples: list[LslSample] = parse_raw_lsl_samples(raw_lsl)

    if raw_metadata is None:
        warn("No metadata found in the record")
        metadata = None
    else:
        recorder_version = RecorderVersion(name=raw_metadata.payload.recorder_version.name,
                                           major=raw_metadata.payload.recorder_version.major,
                                           minor=raw_metadata.payload.recorder_version.minor,
                                           patch=raw_metadata.payload.recorder_version.patch)
        metadata = RecordMetadata(recorder_version=recorder_version,
                                  name=raw_metadata.payload.name,
                                  start_time=raw_metadata.payload.start_time.ToDatetime(),
                                  extra_metadata=raw_metadata.payload.extra_metadata)

    return Record(metadata=metadata,
                  frames=frames,
                  lsl=lsl_stream_samples,
                  markers=markers,
                  raw_samples=raw_samples)

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