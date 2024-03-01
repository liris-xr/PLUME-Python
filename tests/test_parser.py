from plume import parser, filtering
from plume.samples.unity.frame_pb2 import Frame
import os.path

def test_parse_samples():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_2.plm")
    packed_samples = parser.parse_packed_samples_from_file(file_path)
    unpacked_samples = parser.unpack_samples(packed_samples)
    print(unpacked_samples)

def test_parse_record():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_2.plm")
    record = parser.parse_record_from_file(file_path)
    print(record.lsl_samples)

if __name__ == '__main__':
    test_parse_record()