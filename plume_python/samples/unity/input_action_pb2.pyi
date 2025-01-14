from common import vector2_pb2 as _vector2_pb2
from common import vector3_pb2 as _vector3_pb2
from common import quaternion_pb2 as _quaternion_pb2
from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InputActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VALUE: _ClassVar[InputActionType]
    BUTTON: _ClassVar[InputActionType]
    PASSTHROUGH: _ClassVar[InputActionType]
VALUE: InputActionType
BUTTON: InputActionType
PASSTHROUGH: InputActionType

class InputAction(_message.Message):
    __slots__ = ["id", "name", "binding_paths", "type", "boolean", "integer", "float", "double", "vector2", "vector3", "quaternion", "button"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BINDING_PATHS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    INTEGER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    VECTOR2_FIELD_NUMBER: _ClassVar[int]
    VECTOR3_FIELD_NUMBER: _ClassVar[int]
    QUATERNION_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    name: str
    binding_paths: _containers.RepeatedScalarFieldContainer[str]
    type: InputActionType
    boolean: bool
    integer: int
    float: float
    double: float
    vector2: _vector2_pb2.Vector2
    vector3: _vector3_pb2.Vector3
    quaternion: _quaternion_pb2.Quaternion
    button: ButtonValue
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., name: _Optional[str] = ..., binding_paths: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[InputActionType, str]] = ..., boolean: bool = ..., integer: _Optional[int] = ..., float: _Optional[float] = ..., double: _Optional[float] = ..., vector2: _Optional[_Union[_vector2_pb2.Vector2, _Mapping]] = ..., vector3: _Optional[_Union[_vector3_pb2.Vector3, _Mapping]] = ..., quaternion: _Optional[_Union[_quaternion_pb2.Quaternion, _Mapping]] = ..., button: _Optional[_Union[ButtonValue, _Mapping]] = ...) -> None: ...

class ButtonValue(_message.Message):
    __slots__ = ["boolean", "float", "threshold"]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    boolean: bool
    float: float
    threshold: float
    def __init__(self, boolean: bool = ..., float: _Optional[float] = ..., threshold: _Optional[float] = ...) -> None: ...
