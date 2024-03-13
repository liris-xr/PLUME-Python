import os.path
from plume.parser import parse_record_from_file
from plume.utils.game_object import find_game_object_identifiers, find_first_game_object_identifier


def test_find_first_game_object_identifier():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parse_record_from_file(file_path)
    identifier = find_first_game_object_identifier(record, "Main Camera")
    print(identifier)


def test_find_game_object_identifiers():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record.plm")
    record = parse_record_from_file(file_path)
    identifiers = find_game_object_identifiers(record, "Main Camera")
    print(identifiers)


if __name__ == '__main__':
    # test_find_game_object_identifiers()
    test_find_first_game_object_identifier()