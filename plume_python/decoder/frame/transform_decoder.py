from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.registry import register_frame_data_decoder
from plume.sample.unity.transform_pb2 import TransformCreate

from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.gameobject import GameObject
from plume_python.proxy.unity.components.transform import Transform

@register_frame_data_decoder(TransformCreate)
class TransformCreateDecoder(FrameDataDecoder[TransformCreate]):
    def decode(self, frame: Frame, data: TransformCreate):
        component_uuid = data.id.component_id
        game_object_uuid = data.id.parent_id.game_object_id

        if component_uuid in frame._components.keys():
            return

        gameobject = self.get_or_create_gameobject(frame, game_object_uuid)
        transform = Transform(uuid=component_uuid, game_object_uuid=gameobject)
        self.create_component(frame, transform)