import os.path
from typing import cast

import pytest

from plume_python import parser
from plume_python.samples.lsl import lsl_stream_pb2
from plume_python.samples.unity import transform_pb2


def test_parse_samples():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    packed_samples = parser.parse_packed_samples_from_file(file_path)


def test_parse_record():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parser.parse_record_from_file(file_path)


def test_simple_filtering():
    record = cast(parser.Record, pytest.record)
    filtered_lsl = [
        lsl_sample
        for lsl_sample in record[lsl_stream_pb2.StreamSample]
        if 0 <= lsl_sample.timestamp <= 5_000_000_000
    ]
    filtered_transform_updates = [
        frame
        for frame in record[transform_pb2.TransformUpdate]
        if 0 <= frame.timestamp <= 5_000_000_000
    ]
