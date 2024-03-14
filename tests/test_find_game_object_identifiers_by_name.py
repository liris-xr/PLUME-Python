import pytest

from plume_python.utils.game_object import find_identifiers_by_name, find_first_identifier_by_name


def test_find_first_game_object_identifier():
    identifier = find_first_identifier_by_name(pytest.record, "Main Camera")


def test_find_game_object_identifiers():
    identifiers = find_identifiers_by_name(pytest.record, "Main Camera")
