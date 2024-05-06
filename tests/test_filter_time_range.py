import pytest
import os.path
import plume_python as plm


def test_filter_time_range():
    record = pytest.record

    start_time = 5000
    end_time = 100_000_000

    samples = record.get_samples_in_time_range(start_time, end_time)

    for _, samples in samples.items():
        for sample in samples:
            assert start_time <= sample.timestamp <= end_time


def test_get_timeless_samples():
    record = pytest.record
    samples = record.get_timeless_samples()
    for sample in samples:
        assert sample.is_timestamped() is False
