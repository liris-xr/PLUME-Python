from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpeakerMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SPEAKER_MODE_MONO: _ClassVar[SpeakerMode]
    SPEAKER_MODE_STEREO: _ClassVar[SpeakerMode]
    SPEAKER_MODE_QUAD: _ClassVar[SpeakerMode]
    SPEAKER_MODE_SURROUND: _ClassVar[SpeakerMode]
    SPEAKER_MODE_SURROUND_5POINT1: _ClassVar[SpeakerMode]
    SPEAKER_MODE_SURROUND_7POINT1: _ClassVar[SpeakerMode]
    SPEAKER_MODE_PROLOGIC: _ClassVar[SpeakerMode]
SPEAKER_MODE_MONO: SpeakerMode
SPEAKER_MODE_STEREO: SpeakerMode
SPEAKER_MODE_QUAD: SpeakerMode
SPEAKER_MODE_SURROUND: SpeakerMode
SPEAKER_MODE_SURROUND_5POINT1: SpeakerMode
SPEAKER_MODE_SURROUND_7POINT1: SpeakerMode
SPEAKER_MODE_PROLOGIC: SpeakerMode

class AudioSettingsUpdate(_message.Message):
    __slots__ = ["speakerMode", "spatializer_plugin_name"]
    SPEAKERMODE_FIELD_NUMBER: _ClassVar[int]
    SPATIALIZER_PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    speakerMode: SpeakerMode
    spatializer_plugin_name: str
    def __init__(self, speakerMode: _Optional[_Union[SpeakerMode, str]] = ..., spatializer_plugin_name: _Optional[str] = ...) -> None: ...
