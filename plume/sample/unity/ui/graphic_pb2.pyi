from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from plume.sample.common import vector4_pb2 as _vector4_pb2
from plume.sample.common import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GraphicUpdate(_message.Message):
    __slots__ = ("component", "color", "raycast_target", "raycast_padding", "material")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    RAYCAST_TARGET_FIELD_NUMBER: _ClassVar[int]
    RAYCAST_PADDING_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    color: _color_pb2.Color
    raycast_target: bool
    raycast_padding: _vector4_pb2.Vector4
    material: _identifiers_pb2.AssetIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., raycast_target: bool = ..., raycast_padding: _Optional[_Union[_vector4_pb2.Vector4, _Mapping]] = ..., material: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ...) -> None: ...
