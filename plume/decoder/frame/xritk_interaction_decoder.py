from plume.decoder.frame.frame_data_decoder import FrameDataDecoder
from plume.decoder.frame.frame_data_decoder_registry import (
    register_frame_data_decoder,
)
from plume.proxy.unity.frame import Frame
from plume.proxy.unity.component.xr_base_interactor import XRBaseInteractor
from plume.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume.proxy.unity.xritk_interaction import (
    XRITKInteraction,
    XRITKInteractionType,
)
from plume.sample.unity.xritk.xritk_interaction_pb2 import (
    XRITKInteraction as XRITKInteractionSample,
)

from plume.decoder.frame.frame_decoder import get_or_create_component


@register_frame_data_decoder(XRITKInteractionSample)
class XRITKInteractionDecoder(FrameDataDecoder[XRITKInteractionSample]):
    def decode(self, frame: Frame, data: XRITKInteractionSample):
        interactor = get_or_create_component(
            frame, data.interactor, XRBaseInteractor
        )
        interactable = get_or_create_component(
            frame, data.interactable, XRBaseInteractable
        )
        type = XRITKInteractionType.from_message(data.type)

        interaction = XRITKInteraction(
            interactor=interactor,
            interactable=interactable,
            type=type,
        )
        frame.xritk_interactions._add(interaction)
