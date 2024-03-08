import pandas as pd
from google.protobuf.json_format import MessageToDict
from google.protobuf import descriptor_pool

from plume.record import Sample, Record, FrameSample, RawSample, MarkerSample
from plume.samples.common.marker_pb2 import Marker

# Required to add all DESCRIPTORS into the default descriptor pool
from plume.samples import *
__default_descriptor_pool = descriptor_pool.Default()

def markers_to_dataframe(markers: list[MarkerSample]) -> pd.DataFrame:
    sample_data = []
    for marker in markers:
        sample_data.append({"timestamp": marker.timestamp, "marker_label": marker.label})
    return pd.json_normalize(sample_data)

def frames_to_dataframe(frames: list[FrameSample], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> dict[type, pd.DataFrame]:
    """Converts a list of frames into a dictionary of dataframes. The keys are the types of the payloads and the values are the dataframes."""
    # Aggregate data from all frames in a single list
    samples = [data for frame in frames for data in frame.data]
    return samples_to_dataframes(samples, descriptor_pool)

def samples_to_dataframes(samples: list[Sample], descriptor_pool: descriptor_pool.DescriptorPool = __default_descriptor_pool) -> dict[type, pd.DataFrame]:

    dataframes: dict[type, pd.DataFrame] = {}

    # Group samples by payload type
    groups: dict[type, list[Sample]] = {}
    for s in samples:
        if type(s.payload) not in groups:
            groups[type(s.payload)] = []
        groups[type(s.payload)].append(s)

    for (group_key, group_samples) in groups.items():
        sample_data = []

        for sample in group_samples:
            sample_payload_fields_value = MessageToDict(sample.payload, including_default_value_fields=True, descriptor_pool=descriptor_pool)
            sample_data.append({"timestamp": sample.timestamp} | sample_payload_fields_value)

        dataframes[group_key] = pd.json_normalize(sample_data)

    return dataframes