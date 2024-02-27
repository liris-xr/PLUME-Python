import plume.record_reader
import os.path

def test_read_from_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_0.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    print(f"Read {len(samples)} samples from file {file_path}.")

if __name__ == '__main__':
    test_read_from_file()