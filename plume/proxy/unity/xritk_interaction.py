from __future__ import annotations
from dataclasses import dataclass

from plume.sample.unity.xritk.xritk_interaction_pb2 import (
    XRITKInteractionType as XRITKInteractionTypeSample,
)
from plume.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume.proxy.unity.component.xr_base_interactor import XRBaseInteractor

from enum import Enum


class XRITKInteractionType(Enum):
    UNSPECIFIED = 0
    HOVER_ENTER = 1
    HOVER_EXIT = 2
    SELECT_ENTER = 3
    SELECT_EXIT = 4
    ACTIVATE_ENTER = 5
    ACTIVATE_EXIT = 6

    @staticmethod
    def from_message(type: XRITKInteractionTypeSample) -> XRITKInteractionType:
        if (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_HOVER_ENTER
        ):
            return XRITKInteractionType.HOVER_ENTER
        elif (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_HOVER_EXIT
        ):
            return XRITKInteractionType.HOVER_EXIT
        elif (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_SELECT_ENTER
        ):
            return XRITKInteractionType.SELECT_ENTER
        elif (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_SELECT_EXIT
        ):
            return XRITKInteractionType.SELECT_EXIT
        elif (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_ACTIVATE_ENTER
        ):
            return XRITKInteractionType.ACTIVATE_ENTER
        elif (
            type
            == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_ACTIVATE_EXIT
        ):
            return XRITKInteractionType.ACTIVATE_EXIT
        else:
            return XRITKInteractionType.UNSPECIFIED


@dataclass(frozen=True)
class XRITKInteraction:
    interactor: XRBaseInteractor
    interactable: XRBaseInteractable
    type: XRITKInteractionType

    def __hash__(self):
        return hash((self.interactor, self.interactable, self.type))

    def __eq__(self, other):
        if not isinstance(other, XRITKInteraction):
            return False
        return (
            self.interactor == other.interactor
            and self.interactable == other.interactable
            and self.type == other.type
        )
