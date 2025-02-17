from __future__ import annotations
from typing import Union, Optional

from plume.proxy.collection import Collection
from plume.proxy.unity.asset import Asset

from uuid import UUID


class AssetCollection(Collection[Asset]):
    _guid_to_asset: dict[UUID, Asset]

    def __post_init__(self):
        self._guid_to_asset = {asset.guid: asset for asset in self}

    def _remove(self, asset: Asset) -> bool:
        if asset is None or asset.guid not in self._guid_to_asset:
            return False
        if not super()._remove(asset):
            return False
        del self._guid_to_asset[asset.guid]
        return True

    def _add(self, asset: Asset) -> bool:
        if asset.guid in self._guid_to_asset:
            return False
        if not super()._add(asset):
            return False
        self._guid_to_asset[asset.guid] = asset

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        asset = self.with_guid(guid)

        if not super()._remove(asset):
            return False

        del self._guid_to_asset[asset.guid]
        return True

    def with_guid(self, guid: Union[str, UUID]) -> Optional[Asset]:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_asset.get(guid, None)
