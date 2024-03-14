from common import animation_curve_pb2 as _animation_curve_pb2
from unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AudioSourceCreate(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class AudioSourceDestroy(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class AudioSourceUpdate(_message.Message):
    __slots__ = ["id", "audio_clip_id", "audio_mixer_group_id", "is_playing", "time_samples", "mute", "bypass_effects", "bypass_listener_effects", "bypass_reverb_zones", "priority", "volume", "pitch", "stereo_pan", "spatial_blend", "reverb_zone_mix", "doppler_level", "spread", "volume_rolloff"]
    ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_MIXER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PLAYING_FIELD_NUMBER: _ClassVar[int]
    TIME_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    BYPASS_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_LISTENER_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_REVERB_ZONES_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    STEREO_PAN_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_BLEND_FIELD_NUMBER: _ClassVar[int]
    REVERB_ZONE_MIX_FIELD_NUMBER: _ClassVar[int]
    DOPPLER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SPREAD_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ROLLOFF_FIELD_NUMBER: _ClassVar[int]
    id: _identifiers_pb2.ComponentIdentifier
    audio_clip_id: _identifiers_pb2.AssetIdentifier
    audio_mixer_group_id: _identifiers_pb2.AssetIdentifier
    is_playing: bool
    time_samples: int
    mute: bool
    bypass_effects: bool
    bypass_listener_effects: bool
    bypass_reverb_zones: bool
    priority: int
    volume: float
    pitch: float
    stereo_pan: float
    spatial_blend: _animation_curve_pb2.AnimationCurve
    reverb_zone_mix: _animation_curve_pb2.AnimationCurve
    doppler_level: float
    spread: _animation_curve_pb2.AnimationCurve
    volume_rolloff: _animation_curve_pb2.AnimationCurve
    def __init__(self, id: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., audio_clip_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., audio_mixer_group_id: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., is_playing: bool = ..., time_samples: _Optional[int] = ..., mute: bool = ..., bypass_effects: bool = ..., bypass_listener_effects: bool = ..., bypass_reverb_zones: bool = ..., priority: _Optional[int] = ..., volume: _Optional[float] = ..., pitch: _Optional[float] = ..., stereo_pan: _Optional[float] = ..., spatial_blend: _Optional[_Union[_animation_curve_pb2.AnimationCurve, _Mapping]] = ..., reverb_zone_mix: _Optional[_Union[_animation_curve_pb2.AnimationCurve, _Mapping]] = ..., doppler_level: _Optional[float] = ..., spread: _Optional[_Union[_animation_curve_pb2.AnimationCurve, _Mapping]] = ..., volume_rolloff: _Optional[_Union[_animation_curve_pb2.AnimationCurve, _Mapping]] = ...) -> None: ...
