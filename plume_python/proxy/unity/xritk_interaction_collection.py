from __future__ import annotations

from plume_python.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume_python.proxy.unity.component.xr_base_interactor import XRBaseInteractor
from plume_python.proxy.unity.xritk_interaction import XRITKInteraction, XRITKInteractionType

from typing import List, Iterator, Iterable

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
