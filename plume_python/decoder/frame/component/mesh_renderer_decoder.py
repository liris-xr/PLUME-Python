from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.mesh_renderer_pb2 import (
    MeshRendererCreate,
    MeshRendererDestroy,
)

from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component.mesh_renderer import MeshRenderer
from plume_python.decoder.frame.frame_decoder import get_or_create_component, destroy_component


@register_frame_data_decoder(MeshRendererCreate)
class MeshRendererCreateDecoder(FrameDataDecoder[MeshRendererCreate]):
    def decode(self, frame: Frame, data: MeshRendererCreate) -> Frame:
        get_or_create_component(frame, data.component, MeshRenderer)

@register_frame_data_decoder(MeshRendererDestroy)
class MeshRendererDestroyDecoder(FrameDataDecoder[MeshRendererDestroy]):
    def decode(self, frame: Frame, data: MeshRendererDestroy):
        destroy_component(frame, data.component)