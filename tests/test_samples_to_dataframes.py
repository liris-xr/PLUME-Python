import os.path

from plume_python import parser
from plume_python.export.dataframe_exporter import frames_to_dataframe, markers_to_dataframe
from plume_python.samples.unity.transform_pb2 import TransformUpdate
import pytest


def test_export_frames_dataframes():
    frames_df = frames_to_dataframe(pytest.record.frames)


def test_export_markers_dataframes():
    markers_df = markers_to_dataframe(pytest.record.markers)
