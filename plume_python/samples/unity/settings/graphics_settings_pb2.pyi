from unity import identifiers_pb2 as _identifiers_pb2
from common import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GraphicsSettings(_message.Message):
    __slots__ = ["default_render_pipeline_asset_id", "color_space"]
    DEFAULT_RENDER_PIPELINE_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    default_render_pipeline_asset_id: _identifiers_pb2.AssetIdentifier
    color_space: _color_pb2.ColorSpace
    def __init__(self, default_render_pipeline_asset_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., color_space: _Optional[_Union[_color_pb2.ColorSpace, str]] = ...) -> None: ...
