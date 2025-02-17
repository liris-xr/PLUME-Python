from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMAGE_TYPE_SIMPLE: _ClassVar[ImageType]
    IMAGE_TYPE_SLICED: _ClassVar[ImageType]
    IMAGE_TYPE_TILED: _ClassVar[ImageType]
    IMAGE_TYPE_FILLED: _ClassVar[ImageType]

IMAGE_TYPE_SIMPLE: ImageType
IMAGE_TYPE_SLICED: ImageType
IMAGE_TYPE_TILED: ImageType
IMAGE_TYPE_FILLED: ImageType

class ImageCreate(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...

class ImageDestroy(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
    ) -> None: ...

class ImageUpdate(_message.Message):
    __slots__ = ("component", "sprite", "type")
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SPRITE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    sprite: _identifiers_pb2.AssetIdentifier
    type: ImageType
    def __init__(
        self,
        component: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
        sprite: _Optional[
            _Union[_identifiers_pb2.AssetIdentifier, _Mapping]
        ] = ...,
        type: _Optional[_Union[ImageType, str]] = ...,
    ) -> None: ...
