from __future__ import annotations

from plume_python.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume_python.proxy.unity.component.xr_base_interactor import XRBaseInteractor
from plume_python.proxy.unity.xritk_interaction import (
    XRITKInteraction,
    XRITKInteractionType,
)

from plume_python.proxy.collection import Collection

from typing import List


class XRITKInteractionCollection(Collection[XRITKInteraction]):

    def with_type(self, type: XRITKInteractionType) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [interaction for interaction in self if interaction.type == type]
        )

    def with_interactor(
        self, interactor: XRBaseInteractor
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self
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
                for interaction in self
                if interaction.interactor.guid in interactors_guids
            ]
        )

    def with_interactable(
        self, interactable: XRBaseInteractable
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self
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
                for interaction in self
                if interaction.interactable.guid in interactables_guids
            ]
        )

    def with_interactor_and_interactable(
        self, interactor: XRBaseInteractor, interactable: XRBaseInteractable
    ) -> XRITKInteractionCollection:
        return XRITKInteractionCollection(
            [
                interaction
                for interaction in self
                if interaction.interactor.guid == interactor.guid
                and interaction.interactable.guid == interactable.guid
            ]
        )

    def _clear(self):
        self._items.clear()
