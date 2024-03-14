from typing import TypeVar, cast, Type

import pandas as pd
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message

from plume_python.record import Sample, FrameDataSample, Record

T = TypeVar('T', bound=Message)


def samples_to_dataframe(samples: list[Sample[T]]) -> pd.DataFrame:
    if len(samples) == 0:
        return pd.DataFrame()

    sample_data = []

    if isinstance(samples[0], FrameDataSample):
        frame_samples = cast(list[FrameDataSample[T]], samples)
        for frame_sample in frame_samples:
            sample_payload_fields_value = MessageToDict(frame_sample.payload, including_default_value_fields=True)
            sample_data.append({"timestamp": frame_sample.timestamp,
                                "frame_number": frame_sample.frame_number} | sample_payload_fields_value)
    else:
        for sample in samples:
            sample_payload_fields_value = MessageToDict(sample.payload, including_default_value_fields=True)
            if sample.is_timestamped():
                sample_data.append({"timestamp": sample.timestamp} | sample_payload_fields_value)
            else:
                sample_data.append(sample_payload_fields_value)

    return pd.json_normalize(sample_data)


def record_to_dataframes(record: Record) -> dict[type, pd.DataFrame]:
    dataframes: dict[Type[T], pd.DataFrame] = {}

    for payload_type, samples in record.samples_by_type.items():
        dataframes[payload_type] = samples_to_dataframe(samples)

    return dataframes
