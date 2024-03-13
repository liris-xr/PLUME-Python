import os.path
from plume.parser import parse_record_from_file
from plume.utils.transform import compute_transforms_time_series, compute_transform_time_series


def test_compute_single_transform_time_series():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parse_record_from_file(file_path)
    transform_time_series = compute_transform_time_series(record, "4a3f40e37eaf4c0a9d5d88ac993c0ebc")
    # print(transform_time_series)


def test_compute_all_transforms_time_series():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parse_record_from_file(file_path)
    transform_time_series = compute_transforms_time_series(record)
    # print(transform_time_series)


if __name__ == '__main__':
    # test_compute_all_transforms_time_series()
    test_compute_single_transform_time_series()