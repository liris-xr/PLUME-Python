from plume_python import parser
from plume_python.export.xdf_exporter import lsl_samples_to_xdf
import os.path
import pytest


def test_export_xdf():
    record = pytest.record
    with open('tests/test_outputs/test.xdf', 'wb') as f:
        lsl_samples_to_xdf(f, record.markers, record.lsl_open_streams, record.lsl_close_streams, record.lsl_samples,
                           record.metadata.start_time)
