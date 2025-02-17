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

class XRITKInteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    XRITK_INTERACTION_TYPE_UNSPECIFIED: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_HOVER_ENTER: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_HOVER_EXIT: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_SELECT_ENTER: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_SELECT_EXIT: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_ACTIVATE_ENTER: _ClassVar[XRITKInteractionType]
    XRITK_INTERACTION_TYPE_ACTIVATE_EXIT: _ClassVar[XRITKInteractionType]

XRITK_INTERACTION_TYPE_UNSPECIFIED: XRITKInteractionType
XRITK_INTERACTION_TYPE_HOVER_ENTER: XRITKInteractionType
XRITK_INTERACTION_TYPE_HOVER_EXIT: XRITKInteractionType
XRITK_INTERACTION_TYPE_SELECT_ENTER: XRITKInteractionType
XRITK_INTERACTION_TYPE_SELECT_EXIT: XRITKInteractionType
XRITK_INTERACTION_TYPE_ACTIVATE_ENTER: XRITKInteractionType
XRITK_INTERACTION_TYPE_ACTIVATE_EXIT: XRITKInteractionType

class XRITKInteraction(_message.Message):
    __slots__ = ("interactable", "interactor", "type")
    INTERACTABLE_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    interactable: _identifiers_pb2.ComponentIdentifier
    interactor: _identifiers_pb2.ComponentIdentifier
    type: XRITKInteractionType
    def __init__(
        self,
        interactable: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
        interactor: _Optional[
            _Union[_identifiers_pb2.ComponentIdentifier, _Mapping]
        ] = ...,
        type: _Optional[_Union[XRITKInteractionType, str]] = ...,
    ) -> None: ...
