from __future__ import annotations
from typing import List, Union, Optional, Iterable, Iterator

from plume_python.proxy.unity.asset import Asset

from uuid import UUID

class AssetCollection(Iterable[Asset]):
    _assets: List[Asset]
    _guid_to_asset: dict[UUID, Asset]

    def __init__(self, assets: List[Asset] = []):
        self._assets = assets.copy()
        self._guid_to_asset = {asset.guid: asset for asset in self._assets}

    def __len__(self) -> int:
        return len(self._assets)

    def __getitem__(self, index: int) -> Asset:
        return self._assets[index]

    def __iter__(self) -> Iterator[Asset]:
        return iter(self._assets)

    def __contains__(self, asset: Asset) -> bool:
        return asset.guid in self._guid_to_asset

    def _remove(self, asset: Asset) -> bool:
        if asset is None or asset.guid not in self._guid_to_asset:
            return False
        self._assets.remove(asset)
        del self._guid_to_asset[asset.guid]
        return True

    def _add(self, asset: Asset):
        self._assets.append(asset)
        self._guid_to_asset[asset.guid] = asset

    def _remove_by_guid(self, guid: Union[str, UUID]) -> bool:
        asset = self.with_guid(guid)
        return self._remove(asset)

    def with_guid(self, guid: Union[str, UUID]) -> Optional[Asset]:
        try:
            guid = UUID(guid) if isinstance(guid, str) else guid
        except ValueError:
            return None
        return self._guid_to_asset.get(guid, None)
