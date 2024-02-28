from __future__ import annotations
import plume.record_reader
import plume.sample_parser
import plume.frame_parser
import os.path

from plume.samples.record_pb2 import RecordMetadata

def test_parse_metadata(samples):
    unpacked_samples = plume.sample_parser.parse_samples(samples, filter_descriptors=[RecordMetadata.DESCRIPTOR])
    assert len(unpacked_samples) == 1
    assert not unpacked_samples[0].HasTimestamp() # The metadata sample should not have a timestamp
    metadata = unpacked_samples[0]
    print(metadata)

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_1.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    test_parse_metadata(samples)