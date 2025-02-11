from plume.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.transform_pb2 import (
    TransformCreate,
    TransformUpdate,
    TransformDestroy,
)

from plume.proxy.common.vector3 import Vector3
from plume.proxy.common.quaternion import Quaternion
from plume.proxy.unity.frame import Frame
from plume.proxy.unity.component.transform import Transform
from plume.decoder.frame.frame_decoder import (
    get_or_create_component,
    destroy_component,
)


@register_frame_data_decoder(TransformCreate)
class TransformCreateDecoder(FrameDataDecoder[TransformCreate]):
    def decode(self, frame: Frame, data: TransformCreate) -> Frame:
        get_or_create_component(frame, data.component, Transform)


@register_frame_data_decoder(TransformUpdate)
class TransformUpdateDecoder(FrameDataDecoder[TransformUpdate]):
    def decode(self, frame: Frame, data: TransformUpdate):
        t = get_or_create_component(frame, data.component, Transform)

        if data.HasField("parent_transform"):
            prev_parent = t._parent
            new_parent = get_or_create_component(
                frame, data.parent_transform, Transform
            )
            t._parent = new_parent
            if prev_parent is not None:
                prev_parent._children.remove(t)
            if new_parent is not None:
                new_parent._children.append(t)
            t._invalidate_cached_world_matrix()

        if data.HasField("sibling_idx"):
            t._sibling_index = data.sibling_idx

        if data.HasField("local_position"):
            t._local_position = Vector3(
                data.local_position.x, data.local_position.y, data.local_position.z
            )
            t._invalidate_cached_world_matrix()

        if data.HasField("local_rotation"):
            t._local_rotation = Quaternion(
                data.local_rotation.x,
                data.local_rotation.y,
                data.local_rotation.z,
                data.local_rotation.w,
            )
            t._invalidate_cached_world_matrix()

        if data.HasField("local_scale"):
            t._local_scale = Vector3(
                data.local_scale.x, data.local_scale.y, data.local_scale.z
            )
            t._invalidate_cached_world_matrix()


@register_frame_data_decoder(TransformDestroy)
class TransformDestroyDecoder(FrameDataDecoder[TransformDestroy]):
    def decode(self, frame: Frame, data: TransformDestroy):
        destroy_component(frame, data.component)
