from plume_python.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume_python.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.xritk.xr_base_interactor_pb2 import (
    XRBaseInteractorCreate,
    XRBaseInteractorUpdate,
    XRBaseInteractorDestroy,
)

from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.component.xr_base_interactor import XRBaseInteractor
from plume_python.decoder.frame.frame_decoder import (
    get_or_create_component,
    destroy_component,
)


@register_frame_data_decoder(XRBaseInteractorCreate)
class XRBaseInteractorCreateDecoder(FrameDataDecoder[XRBaseInteractorCreate]):
    def decode(self, frame: Frame, data: XRBaseInteractorCreate) -> Frame:
        get_or_create_component(frame, data.component, XRBaseInteractor)


@register_frame_data_decoder(XRBaseInteractorUpdate)
class XRBaseInteractorUpdateDecoder(FrameDataDecoder[XRBaseInteractorUpdate]):
    def decode(self, frame: Frame, data: XRBaseInteractorUpdate):
        interactor = get_or_create_component(frame, data.component, XRBaseInteractor)

        if data.HasField("enabled"):
            interactor._enabled = data.enabled


@register_frame_data_decoder(XRBaseInteractorDestroy)
class XRBaseInteractorDestroyDecoder(FrameDataDecoder[XRBaseInteractorDestroy]):
    def decode(self, frame: Frame, data: XRBaseInteractorDestroy):
        destroy_component(frame, data.component)
