import pytest
import plume


def test_load():
    reader = plume.RecordReader("tests/data/record.plm")

    for frame in reader.frames:
        print(frame)
