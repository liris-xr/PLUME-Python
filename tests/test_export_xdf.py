import pytest

from plume_python.export.xdf_exporter import export_xdf_from_record
from pathlib import Path


def test_export_xdf():
    record = pytest.record
    # create directory tests/test_outputs if it does not exist
    Path("tests/test_outputs").mkdir(parents=True, exist_ok=True)
    with open("tests/test_outputs/test.xdf", "wb") as f:
        export_xdf_from_record(f, record)
