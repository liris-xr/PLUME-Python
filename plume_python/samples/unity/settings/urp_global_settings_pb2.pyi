from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class URPGlobalSettingsUpdate(_message.Message):
    __slots__ = ["name", "settings_asset_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    settings_asset_id: _identifiers_pb2.AssetIdentifier
    def __init__(self, name: _Optional[str] = ..., settings_asset_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...
