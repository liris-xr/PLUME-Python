from unity import identifiers_pb2 as _identifiers_pb2
from unity.urp import rendering_pb2 as _rendering_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CameraOverrideOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CAMERA_OVERRIDE_OPTION_OFF: _ClassVar[CameraOverrideOption]
    CAMERA_OVERRIDE_OPTION_ON: _ClassVar[CameraOverrideOption]
    CAMERA_OVERRIDE_OPTION_USE_PIPELINE_SETTINGS: _ClassVar[CameraOverrideOption]

class CameraRenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    CAMERA_RENDER_TYPE_BASE: _ClassVar[CameraRenderType]
    CAMERA_RENDER_TYPE_OVERLAY: _ClassVar[CameraRenderType]
CAMERA_OVERRIDE_OPTION_OFF: CameraOverrideOption
CAMERA_OVERRIDE_OPTION_ON: CameraOverrideOption
CAMERA_OVERRIDE_OPTION_USE_PIPELINE_SETTINGS: CameraOverrideOption
CAMERA_RENDER_TYPE_BASE: CameraRenderType
CAMERA_RENDER_TYPE_OVERLAY: CameraRenderType

class AdditionalCameraDataCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class AdditionalCameraDataDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class AdditionalCameraDataUpdate(_message.Message):
    __slots__ = ["id", "version", "render_shadows", "requires_depth_option", "requires_color_option", "render_type", "requires_depth_texture", "requires_color_texture", "volume_layer_mask", "volume_trigger_id", "render_post_processing", "antialiasing", "antialiasing_quality", "stop_nan", "dithering", "allow_xr_rendering"]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RENDER_SHADOWS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_DEPTH_OPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_COLOR_OPTION_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_DEPTH_TEXTURE_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_COLOR_TEXTURE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LAYER_MASK_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_POST_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    ANTIALIASING_FIELD_NUMBER: _ClassVar[int]
    ANTIALIASING_QUALITY_FIELD_NUMBER: _ClassVar[int]
    STOP_NAN_FIELD_NUMBER: _ClassVar[int]
    DITHERING_FIELD_NUMBER: _ClassVar[int]
    ALLOW_XR_RENDERING_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    version: float
    render_shadows: bool
    requires_depth_option: CameraOverrideOption
    requires_color_option: CameraOverrideOption
    render_type: CameraRenderType
    requires_depth_texture: bool
    requires_color_texture: bool
    volume_layer_mask: int
    volume_trigger_id: _identifiers_pb2.ComponentIdentifier
    render_post_processing: bool
    antialiasing: _rendering_pb2.AntialiasingMode
    antialiasing_quality: _rendering_pb2.AntialiasingQuality
    stop_nan: bool
    dithering: bool
    allow_xr_rendering: bool
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., version: _Optional[float] = ..., render_shadows: bool = ..., requires_depth_option: _Optional[_Union[CameraOverrideOption, str]] = ..., requires_color_option: _Optional[_Union[CameraOverrideOption, str]] = ..., render_type: _Optional[_Union[CameraRenderType, str]] = ..., requires_depth_texture: bool = ..., requires_color_texture: bool = ..., volume_layer_mask: _Optional[int] = ..., volume_trigger_id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., render_post_processing: bool = ..., antialiasing: _Optional[_Union[_rendering_pb2.AntialiasingMode, str]] = ..., antialiasing_quality: _Optional[_Union[_rendering_pb2.AntialiasingQuality, str]] = ..., stop_nan: bool = ..., dithering: bool = ..., allow_xr_rendering: bool = ...) -> None: ...
