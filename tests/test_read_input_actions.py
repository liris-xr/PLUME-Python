import pytest
import plume

def test_read_input_actions():
    reader = plume.RecordReader("tests/data/record.plm")

    try:
        for frame in reader.input_actions:
            pass
    except Exception as e:
        pytest.fail("Failed to read input actions: " + str(e))
