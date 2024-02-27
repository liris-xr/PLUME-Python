import plume.record_reader
import plume.sample_parser
import plume.frame_parser
import os.path
import plume.samples.unity.frame_pb2

def test_parse_samples(samples):
    unpacked_samples = plume.sample_parser.parse_samples(samples)
    print(unpacked_samples)
    unpacked_frames = plume.sample_parser.parse_samples(samples, filter_descriptor=plume.samples.unity.frame_pb2.Frame.DESCRIPTOR)
    print(unpacked_frames)
    

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_0.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    test_parse_samples(samples)