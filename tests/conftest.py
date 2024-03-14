import os

import pytest

from plume_python.parser import parse_record_from_file


def pytest_configure():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    pytest.record = parse_record_from_file(file_path)
