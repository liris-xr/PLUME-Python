import plume.record_reader
import plume.sample_parser
import plume.frame_parser
import os.path

from plume.samples.unity.frame_pb2 import Frame
from plume.samples.unity.transform_pb2 import TransformCreate

def test_parse_samples(samples):
    unpacked_frames = plume.sample_parser.parse_samples(samples, filter_descriptors=[Frame.DESCRIPTOR])
    
    for frame in unpacked_frames:
        unfiltered_data = plume.frame_parser.parse_frame_data(frame)
        print(unfiltered_data)
        filtered_data = plume.frame_parser.parse_frame_data(frame, filter_descriptors=[TransformCreate.DESCRIPTOR])
        print(filtered_data)

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_0.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    test_parse_samples(samples)