from plume.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.game_object_pb2 import (
    GameObjectCreate,
    GameObjectUpdate,
    GameObjectDestroy,
)

from plume.proxy.unity.frame import Frame
from plume.decoder.frame.frame_decoder import (
    get_or_create_game_object,
    get_or_create_scene,
    destroy_game_object,
)


@register_frame_data_decoder(GameObjectCreate)
class GameObjectCreateDecoder(FrameDataDecoder[GameObjectCreate]):
    def decode(self, frame: Frame, data: GameObjectCreate) -> Frame:
        get_or_create_game_object(frame, data.id)


@register_frame_data_decoder(GameObjectUpdate)
class GameObjectUpdateDecoder(FrameDataDecoder[GameObjectUpdate]):
    def decode(self, frame: Frame, data: GameObjectUpdate):
        game_object = get_or_create_game_object(frame, data.id)

        if data.HasField("name"):
            scene = game_object.scene
            prev_name = game_object._name
            scene.game_objects._name_to_game_objects.get(prev_name, []).remove(
                game_object
            )
            game_object._name = data.name
            scene.game_objects._name_to_game_objects.setdefault(
                data.name, []
            ).append(game_object)

        if data.HasField("tag"):
            game_object._tag = data.tag

        if data.HasField("layer"):
            game_object._layer = data.layer

        if data.HasField("active"):
            game_object._active = data.active

        if data.HasField("scene"):
            old_scene = game_object.scene
            old_scene.game_objects._remove_by_guid(game_object.guid)
            new_scene = get_or_create_scene(frame, data.scene)
            if new_scene is not None:
                new_scene.game_objects._add(game_object)
            game_object._scene = new_scene


@register_frame_data_decoder(GameObjectDestroy)
class GameObjectDestroyDecoder(FrameDataDecoder[GameObjectDestroy]):
    def decode(self, frame: Frame, data: GameObjectDestroy):
        destroy_game_object(frame, data.id)
