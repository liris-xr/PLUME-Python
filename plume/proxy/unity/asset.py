from __future__ import annotations
from dataclasses import dataclass

from uuid import UUID

@dataclass(frozen=True)
class Asset:
    guid: UUID
    asset_bundle_path: str