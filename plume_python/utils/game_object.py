from typing import Optional

from ..record import Record
from ..samples.unity.game_object_pb2 import GameObjectUpdate
from ..samples.unity.identifiers_pb2 import GameObjectIdentifier


def find_names_by_guid(record: Record, guid: str) -> list[str]:
    names: list[str] = []
    for go_update_sample in record[GameObjectUpdate]:
        go_update = go_update_sample.payload
        if go_update.id.game_object_id == guid:
            if go_update.HasField("name"):
                names.append(go_update.name)
    return names


def find_first_name_by_guid(record: Record, guid: str) -> Optional[str]:
    for go_update_sample in record[GameObjectUpdate]:
        go_update = go_update_sample.payload
        if go_update.id.game_object_id == guid:
            if go_update.HasField("name"):
                return go_update.name
    return None


def find_identifiers_by_name(record: Record, name: str) -> list[GameObjectIdentifier]:
    identifiers: list[GameObjectIdentifier] = []
    known_guids: set[str] = set()

    for go_update_sample in record[GameObjectUpdate]:
        go_update = go_update_sample.payload
        if go_update.HasField("name"):
            if name == go_update.name and go_update.id.game_object_id not in known_guids:
                identifiers.append(go_update.id)
                known_guids.add(go_update.id.game_object_id)
    return identifiers


def find_first_identifier_by_name(record: Record, name: str) -> Optional[GameObjectIdentifier]:
    for go_update_sample in record[GameObjectUpdate]:
        go_update = go_update_sample.payload
        if go_update.HasField("name"):
            if name == go_update.name:
                return go_update.id
    return None
