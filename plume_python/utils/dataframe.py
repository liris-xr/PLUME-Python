from typing import TypeVar, cast, Type

from tqdm import tqdm
import pandas as pd
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message
from .transform import TimestampedTransform

from plume_python.record import Sample, FrameDataSample, Record

T = TypeVar("T", bound=Message)


def world_transforms_to_dataframe(
    world_transforms: list[TimestampedTransform],
) -> pd.DataFrame:
    if len(world_transforms) == 0:
        return pd.DataFrame()

    world_transform_data = []

    for world_transform in tqdm(world_transforms, desc="Creating dataframe"):
        world_position = world_transform.get_world_position()
        world_rotation = world_transform.get_world_rotation()
        world_scale = world_transform.get_world_scale()
        world_transform_data.append(
            {
                "timestamp": world_transform.timestamp,
                "position_x": world_position[0],
                "position_y": world_position[1],
                "position_z": world_position[2],
                "rotation_x": world_rotation.x,
                "rotation_y": world_rotation.y,
                "rotation_z": world_rotation.z,
                "rotation_w": world_rotation.w,
                "scale_x": world_scale[0],
                "scale_y": world_scale[1],
                "scale_z": world_scale[2],
            }
        )

    return pd.json_normalize(world_transform_data)


def samples_to_dataframe(samples: list[Sample[T]]) -> pd.DataFrame:
    if len(samples) == 0:
        return pd.DataFrame()

    sample_data = []

    if isinstance(samples[0], FrameDataSample):
        frame_samples = cast(list[FrameDataSample[T]], samples)
        for frame_sample in frame_samples:
            sample_payload_fields_value = MessageToDict(
                frame_sample.payload, True
            )
            sample_data.append(
                {
                    "timestamp": frame_sample.timestamp,
                    "frame_number": frame_sample.frame_number,
                }
                | sample_payload_fields_value
            )
    else:
        for sample in samples:
            sample_payload_fields_value = MessageToDict(sample.payload, True)
            if sample.is_timestamped():
                sample_data.append(
                    {"timestamp": sample.timestamp}
                    | sample_payload_fields_value
                )
            else:
                sample_data.append(sample_payload_fields_value)

    return pd.json_normalize(sample_data)


def record_to_dataframes(record: Record) -> dict[Type[T], pd.DataFrame]:
    dataframes: dict[Type[T], pd.DataFrame] = {}

    for payload_type, samples in record.samples_by_type.items():
        dataframes[payload_type] = samples_to_dataframe(samples)

    return dataframes
