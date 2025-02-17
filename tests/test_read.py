import plume
import pytest

def test_read_all():
    reader = plume.RecordReader("tests/record.plm")

    for frame in reader.frames:
        pass

