from plume.record import Record, FrameSample
from plume.samples.unity.game_object_pb2 import GameObjectUpdate
from plume.samples.unity.identifiers_pb2 import GameObjectIdentifier
from typing import Optional


def find_game_object_identifiers(record: Record, name: str) -> list[GameObjectIdentifier]:
    identifiers: list[GameObjectIdentifier] = []
    known_guids: set[str] = set()

    for frame in record.frames:
        for frame_data in frame.data:
            if isinstance(frame_data.payload, GameObjectUpdate):
                update_sample = frame_data.payload
                if update_sample.HasField("name"):
                    if name == update_sample.name and update_sample.id.game_object_id not in known_guids:
                        identifiers.append(update_sample.id)
                        known_guids.add(update_sample.id.game_object_id)
    return identifiers


def find_first_game_object_identifier(record: Record, name: str) -> Optional[GameObjectIdentifier]:
    for frame in record.frames:
        for frame_data in frame.data:
            if isinstance(frame_data.payload, GameObjectUpdate):
                update_sample = frame_data.payload
                if update_sample.HasField("name"):
                    if name == update_sample.name:
                        return update_sample.id
    return None
