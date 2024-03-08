from plume import parser
from plume.export.dataframe_exporter import frames_to_dataframe, markers_to_dataframe
from plume.samples.unity.transform_pb2 import TransformUpdate
import os.path

def test_export_frames_dataframes():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parser.parse_record_from_file(file_path)
    frames_df = frames_to_dataframe(record.frames)
    print(frames_df[TransformUpdate])

def test_export_markers_dataframes():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parser.parse_record_from_file(file_path)
    markers_df = markers_to_dataframe(record.markers)
    print(markers_df)

if __name__ == '__main__':
    test_export_markers_dataframes()
    # test_export_frames_dataframes()