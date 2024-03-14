from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColorSpace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COLOR_SPACE_UNINITIALIZED: _ClassVar[ColorSpace]
    COLOR_SPACE_GAMMA: _ClassVar[ColorSpace]
    COLOR_SPACE_LINEAR: _ClassVar[ColorSpace]
COLOR_SPACE_UNINITIALIZED: ColorSpace
COLOR_SPACE_GAMMA: ColorSpace
COLOR_SPACE_LINEAR: ColorSpace

class Color(_message.Message):
    __slots__ = ["r", "g", "b", "a"]
    R_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    r: float
    g: float
    b: float
    a: float
    def __init__(self, r: _Optional[float] = ..., g: _Optional[float] = ..., b: _Optional[float] = ..., a: _Optional[float] = ...) -> None: ...

class ColorGradient(_message.Message):
    __slots__ = ["color_space", "mode", "color_keys", "alpha_keys"]
    class GradientMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        GRADIENT_MODE_BLEND: _ClassVar[ColorGradient.GradientMode]
        GRADIENT_MODE_FIXED: _ClassVar[ColorGradient.GradientMode]
        GRADIENT_MODE_PERCEPTUAL_BLEND: _ClassVar[ColorGradient.GradientMode]
    GRADIENT_MODE_BLEND: ColorGradient.GradientMode
    GRADIENT_MODE_FIXED: ColorGradient.GradientMode
    GRADIENT_MODE_PERCEPTUAL_BLEND: ColorGradient.GradientMode
    class ColorKey(_message.Message):
        __slots__ = ["color", "time"]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        color: Color
        time: float
        def __init__(self, color: _Optional[_Union[Color, _Mapping]] = ..., time: _Optional[float] = ...) -> None: ...
    class AlphaKey(_message.Message):
        __slots__ = ["alpha", "time"]
        ALPHA_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        alpha: float
        time: float
        def __init__(self, alpha: _Optional[float] = ..., time: _Optional[float] = ...) -> None: ...
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_KEYS_FIELD_NUMBER: _ClassVar[int]
    ALPHA_KEYS_FIELD_NUMBER: _ClassVar[int]
    color_space: ColorSpace
    mode: ColorGradient.GradientMode
    color_keys: _containers.RepeatedCompositeFieldContainer[ColorGradient.ColorKey]
    alpha_keys: _containers.RepeatedCompositeFieldContainer[ColorGradient.AlphaKey]
    def __init__(self, color_space: _Optional[_Union[ColorSpace, str]] = ..., mode: _Optional[_Union[ColorGradient.GradientMode, str]] = ..., color_keys: _Optional[_Iterable[_Union[ColorGradient.ColorKey, _Mapping]]] = ..., alpha_keys: _Optional[_Iterable[_Union[ColorGradient.AlphaKey, _Mapping]]] = ...) -> None: ...
