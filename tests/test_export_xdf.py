from plume import parser
from plume.export.xdf_exporter import lsl_samples_to_xdf
import os.path

def test_export_xdf():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parser.parse_record_from_file(file_path)
    with open('test.xdf', 'wb') as f:
        lsl_samples_to_xdf(f, record.markers, record.lsl_open_streams, record.lsl_close_streams, record.lsl_samples, record.metadata.start_time)

if __name__ == '__main__':
    test_export_xdf()