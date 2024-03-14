from plume_python import parser
import os.path
import pytest

def test_parse_samples():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    packed_samples = parser.parse_packed_samples_from_file(file_path)
    unpacked_samples = parser.unpack_samples(packed_samples)


def test_parse_record():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parser.parse_record_from_file(file_path)


def test_simple_filtering():
    filtered_lsl = [lsl_sample for lsl_sample in pytest.record.lsl_samples if 0 <= lsl_sample.timestamp <= 5_000_000_000]
    filtered_frames = [frame for frame in pytest.record.frames if 0 <= frame.timestamp <= 5_000_000_000]
