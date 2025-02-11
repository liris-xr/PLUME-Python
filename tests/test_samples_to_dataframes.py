import pytest

from plume.sample.common import marker_pb2
from plume.utils.dataframe import samples_to_dataframe, record_to_dataframes


def test_export_record_dataframes():
    frames_df = record_to_dataframes(pytest.record)


def test_export_markers_dataframes():
    markers_df = samples_to_dataframe(pytest.record[marker_pb2.Marker])
