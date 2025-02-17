from plume.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.sample.unity.xritk.xr_base_interactable_pb2 import (
    XRBaseInteractableCreate,
    XRBaseInteractableUpdate,
    XRBaseInteractableDestroy,
)

from plume.proxy.unity.frame import Frame
from plume.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume.decoder.frame.frame_decoder import (
    get_or_create_component,
    destroy_component,
)


@register_frame_data_decoder(XRBaseInteractableCreate)
class XRBaseInteractableCreateDecoder(
    FrameDataDecoder[XRBaseInteractableCreate]
):
    def decode(self, frame: Frame, data: XRBaseInteractableCreate) -> Frame:
        get_or_create_component(frame, data.component, XRBaseInteractable)


@register_frame_data_decoder(XRBaseInteractableUpdate)
class XRBaseInteractableUpdateDecoder(
    FrameDataDecoder[XRBaseInteractableUpdate]
):
    def decode(self, frame: Frame, data: XRBaseInteractableUpdate):
        interactable = get_or_create_component(
            frame, data.component, XRBaseInteractable
        )

        if data.HasField("enabled"):
            interactable._enabled = data.enabled


@register_frame_data_decoder(XRBaseInteractableDestroy)
class XRBaseInteractableDestroyDecoder(
    FrameDataDecoder[XRBaseInteractableDestroy]
):
    def decode(self, frame: Frame, data: XRBaseInteractableDestroy):
        destroy_component(frame, data.component)
