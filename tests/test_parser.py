from plume import parser
import os.path

def test_parse_samples():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_2.plm")
    packed_samples = parser.parse_packed_samples_from_file(file_path)
    unpacked_samples = parser.unpack_samples(packed_samples)
    print(unpacked_samples)

def test_parse_record():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_1.plm")
    record = parser.parse_record_from_file(file_path)
    print(len(record.lsl_samples))
    print(len(record.frames))
    print(len(record.markers))
    print(record.metadata)

def test_simple_filtering():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_2.plm")
    record = parser.parse_record_from_file(file_path)

    filtered_lsl = [lsl_sample for lsl_sample in record.lsl if lsl_sample.timestamp >= 0 and lsl_sample.timestamp <= 5_000_000_000]
    filtered_frames = [frame for frame in record.frames if frame.timestamp >= 0 and frame.timestamp <= 5_000_000_000]
    print(len(filtered_lsl))
    print(len(filtered_frames))

if __name__ == '__main__':
    # test_parse_samples()
    test_parse_record()
    # test_simple_filtering()