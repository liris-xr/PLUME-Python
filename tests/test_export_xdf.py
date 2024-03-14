import pytest

from plume_python.export.xdf_exporter import export_xdf_from_record


def test_export_xdf():
    record = pytest.record
    with open('tests/test_outputs/test.xdf', 'wb') as f:
        export_xdf_from_record(f, record)
