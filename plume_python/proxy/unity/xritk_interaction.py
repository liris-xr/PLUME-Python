from __future__ import annotations
from dataclasses import dataclass

from plume.sample.unity.xritk.xritk_interaction_pb2 import (
    XRITKInteractionType as XRITKInteractionTypeSample,
)
from plume_python.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume_python.proxy.unity.component.xr_base_interactor import XRBaseInteractor

from enum import Enum
from typing import List, Iterator, Iterable


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
        if type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_HOVER_ENTER:
            return XRITKInteractionType.HOVER_ENTER
        elif type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_HOVER_EXIT:
            return XRITKInteractionType.HOVER_EXIT
        elif type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_SELECT_ENTER:
            return XRITKInteractionType.SELECT_ENTER
        elif type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_SELECT_EXIT:
            return XRITKInteractionType.SELECT_EXIT
        elif type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_ACTIVATE_ENTER:
            return XRITKInteractionType.ACTIVATE_ENTER
        elif type == XRITKInteractionTypeSample.XRITK_INTERACTION_TYPE_ACTIVATE_EXIT:
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
        return self.interactor == other.interactor and self.interactable == other.interactable and self.type == other.type


class XRITKInteractionCollection(Iterable[XRITKInteraction]):
    _interactions: List[XRITKInteraction]

    def __init__(self, interactions: List[XRITKInteraction] = []):
        self._interactions = interactions.copy()

    def __len__(self) -> int:
        return len(self._interactions)

    def __getitem__(self, index: int) -> XRITKInteraction:
        return self._interactions[index]

    def __iter__(self) -> Iterator[XRITKInteraction]:
        return iter(self._interactions)

    def __contains__(self, interaction: XRITKInteraction) -> bool:
        return interaction in self._interactions

    def _add(self, interaction: XRITKInteraction):
        self._interactions.append(interaction)

    def _remove(self, interaction: XRITKInteraction) -> bool:
        if interaction in self._interactions:
            self._interactions.remove(interaction)
            return True
        return False

    def with_type(self, type: XRITKInteractionType) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.type == type
            ]
        )

    def with_interactor(
        self, interactor: XRBaseInteractor
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.interactor.guid == interactor.guid
            ]
        )

    def with_interactors(
        self, interactors: List[XRBaseInteractor]
    ) -> XRITKInteractionCollection:
        interactors_guids = [interactor.guid for interactor in interactors]
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.interactor.guid in interactors_guids
            ]
        )

    def with_interactable(
        self, interactable: XRBaseInteractable
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.interactable.guid == interactable.guid
            ]
        )

    def with_interactables(
        self, interactables: List[XRBaseInteractable]
    ) -> XRITKInteractionCollection:
        interactables_guids = [interactable.guid for interactable in interactables]
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.interactable.guid in interactables_guids
            ]
        )

    def with_interactor_and_interactable(
        self, interactor: XRBaseInteractor, interactable: XRBaseInteractable
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self._interactions
                if interaction.interactor.guid == interactor.guid
                and interaction.interactable.guid == interactable.guid
            ]
        )
