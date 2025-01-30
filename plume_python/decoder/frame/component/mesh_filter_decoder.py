from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.mesh_filter_pb2 import (
    MeshFilterCreate,
    MeshFilterUpdate,
    MeshFilterDestroy,
)

from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component.mesh_filter import MeshFilter
from plume_python.decoder.frame.frame_decoder import get_or_create_component, get_or_create_asset, destroy_component


@register_frame_data_decoder(MeshFilterCreate)
class MeshFilterCreateDecoder(FrameDataDecoder[MeshFilterCreate]):
    def decode(self, frame: Frame, data: MeshFilterCreate) -> Frame:
        get_or_create_component(frame, data.component, MeshFilter)


@register_frame_data_decoder(MeshFilterUpdate)
class MeshFilterUpdateDecoder(FrameDataDecoder[MeshFilterUpdate]):
    def decode(self, frame: Frame, data: MeshFilterUpdate):
        mf = get_or_create_component(frame, data.component, MeshFilter)

        if data.HasField("mesh"):
            mf._mesh = get_or_create_asset(frame, data.mesh)


@register_frame_data_decoder(MeshFilterDestroy)
class MeshFilterDestroyDecoder(FrameDataDecoder[MeshFilterDestroy]):
    def decode(self, frame: Frame, data: MeshFilterDestroy):
        destroy_component(frame, data.component)