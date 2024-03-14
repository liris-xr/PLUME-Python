import pytest

from plume_python.utils.transform import compute_transforms_time_series, compute_transform_time_series


def test_compute_single_transform_time_series():
    transform_time_series = compute_transform_time_series(pytest.record, "4a3f40e37eaf4c0a9d5d88ac993c0ebc")


def test_compute_all_transforms_time_series():
    transform_time_series = compute_transforms_time_series(pytest.record, {"4a3f40e37eaf4c0a9d5d88ac993c0ebc"})
