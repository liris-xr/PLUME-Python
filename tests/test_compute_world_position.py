import plume.record_reader
import plume.sample_parser
import plume.frame_parser
import os.path

from plume.samples.unity.frame_pb2 import Frame
from plume.samples.unity.transform_pb2 import TransformCreate, TransformUpdate, TransformDestroy

def test_parse_samples(samples):
    unpacked_frames = plume.sample_parser.parse_samples(samples, filter_descriptors=[Frame.DESCRIPTOR])

    for frame in unpacked_frames:
        # copy all previous positions and hierarchy to new frame
        # delete all position marked destroyed

        frame_time = frame.timestamp

        transform_updates = plume.frame_parser.parse_frame_data(frame, filter_descriptors=[TransformUpdate.DESCRIPTOR])
        
        for transform_update in transform_updates:
            # update with new position
            pass

    # for each frame, compute the local TRS matrix for each transform, and using their parent, compute the world TRS matrix

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_0.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    test_parse_samples(samples)