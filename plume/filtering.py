from typing import TypeVar
from google.protobuf.message import Message
from google.protobuf.any_pb2 import Any
from google.protobuf.descriptor_pool import DescriptorPool
from plume.samples.packed_sample_pb2 import PackedSample
from plume.record import Sample

def filter_packed_samples(samples: list[PackedSample], any_payload_types: list[type] = None, except_payload_types: list[type] = None) -> list[PackedSample]:
    
    if any_payload_types is not None and not isinstance(any_payload_types, list):
        any_payload_types = [any_payload_types]
    
    if except_payload_types is not None and not isinstance(except_payload_types, list):
        except_payload_types = [except_payload_types]
    
    if any_payload_types is None and except_payload_types is None:
        return samples.copy()
    
    filtered_packed_samples: list[PackedSample] = []
    
    for sample in samples:
        if any_payload_types is not None and not any(sample.payload.type_url.split("/")[-1] == payload_type.DESCRIPTOR.full_name for payload_type in any_payload_types):
            continue
        if except_payload_types is not None and any(sample.payload.type_url.split("/")[-1] == payload_type.DESCRIPTOR.full_name for payload_type in except_payload_types):
            continue
        filtered_packed_samples.append(sample)

    return filtered_packed_samples

def filter_samples(samples: list[Sample], any_payload_types: list[type] = None, except_payload_types: list[type] = None) -> list[Sample]:

    if any_payload_types is not None and not isinstance(any_payload_types, list):
        any_payload_types = [any_payload_types]
    
    if except_payload_types is not None and not isinstance(except_payload_types, list):
        except_payload_types = [except_payload_types]

    if any_payload_types is None and except_payload_types is None:
        return samples.copy()
    
    filtered_samples: list[Sample] = []
    
    for sample in samples:
        if any_payload_types is not None and not any(isinstance(sample.payload, payload_type) for payload_type in any_payload_types):
            continue
        if except_payload_types is not None and any(isinstance(sample.payload, payload_type) for payload_type in except_payload_types):
            continue
        filtered_samples.append(sample)

    return filtered_samples