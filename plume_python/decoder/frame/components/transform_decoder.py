from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.transform_pb2 import (
    TransformCreate,
    TransformUpdate,
    TransformDestroy,
)

from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component.transform import Transform
from plume_python.decoder.frame.frame_decoder import get_or_create_component, destroy_component


@register_frame_data_decoder(TransformCreate)
class TransformCreateDecoder(FrameDataDecoder[TransformCreate]):
    def decode(self, frame: Frame, data: TransformCreate) -> Frame:
        get_or_create_component(frame, data.component, Transform)


@register_frame_data_decoder(TransformUpdate)
class TransformUpdateDecoder(FrameDataDecoder[TransformUpdate]):
    def decode(self, frame: Frame, data: TransformUpdate):
        t = get_or_create_component(frame, data.component, Transform)

        if data.HasField("local_position"):
            t._local_position._x = data.local_position.x
            t._local_position._y = data.local_position.y
            t._local_position._z = data.local_position.z

        if data.HasField("local_rotation"):
            t._local_rotation._x = data.local_rotation.x
            t._local_rotation._y = data.local_rotation.y
            t._local_rotation._z = data.local_rotation.z
            t._local_rotation._w = data.local_rotation.w

        if data.HasField("local_scale"):
            t._local_scale._x = data.local_scale.x
            t._local_scale._y = data.local_scale.y
            t._local_scale._z = data.local_scale.z


@register_frame_data_decoder(TransformDestroy)
class TransformDestroyDecoder(FrameDataDecoder[TransformDestroy]):
    def decode(self, frame: Frame, data: TransformDestroy):
        destroy_component(frame, data.component)
