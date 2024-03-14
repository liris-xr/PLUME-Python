from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeightedMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    WEIGHTED_MODE_NONE: _ClassVar[WeightedMode]
    WEIGHTED_MODE_IN: _ClassVar[WeightedMode]
    WEIGHTED_MODE_OUT: _ClassVar[WeightedMode]
    WEIGHTED_MODE_BOTH: _ClassVar[WeightedMode]
WEIGHTED_MODE_NONE: WeightedMode
WEIGHTED_MODE_IN: WeightedMode
WEIGHTED_MODE_OUT: WeightedMode
WEIGHTED_MODE_BOTH: WeightedMode

class AnimationCurve(_message.Message):
    __slots__ = ["keyframes"]
    KEYFRAMES_FIELD_NUMBER: _ClassVar[int]
    keyframes: _containers.RepeatedCompositeFieldContainer[AnimationCurveKeyFrame]
    def __init__(self, keyframes: _Optional[_Iterable[_Union[AnimationCurveKeyFrame, _Mapping]]] = ...) -> None: ...

class AnimationCurveKeyFrame(_message.Message):
    __slots__ = ["time", "value", "in_tangent", "out_tangent", "weighted_mode", "in_weight", "out_weight"]
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IN_TANGENT_FIELD_NUMBER: _ClassVar[int]
    OUT_TANGENT_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_MODE_FIELD_NUMBER: _ClassVar[int]
    IN_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    time: float
    value: float
    in_tangent: float
    out_tangent: float
    weighted_mode: WeightedMode
    in_weight: float
    out_weight: float
    def __init__(self, time: _Optional[float] = ..., value: _Optional[float] = ..., in_tangent: _Optional[float] = ..., out_tangent: _Optional[float] = ..., weighted_mode: _Optional[_Union[WeightedMode, str]] = ..., in_weight: _Optional[float] = ..., out_weight: _Optional[float] = ...) -> None: ...
