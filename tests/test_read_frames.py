import pytest
import plume


def test_load():
    reader = plume.RecordReader("tests/data/record.plm")

    try:
        for frame in reader.frames:
            pass
    except Exception as e:
        pytest.fail("Failed to read frames: " + str(e))
