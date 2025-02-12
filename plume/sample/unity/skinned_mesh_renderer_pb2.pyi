from plume.sample.unity import identifiers_pb2 as _identifiers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkinnedMeshRendererCreate(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class SkinnedMeshRendererDestroy(_message.Message):
    __slots__ = ("component",)
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ...) -> None: ...

class SkinnedMeshRendererUpdate(_message.Message):
    __slots__ = ("component", "mesh", "root_bone", "bones", "blend_shape_weights")
    class Bones(_message.Message):
        __slots__ = ("ids",)
        IDS_FIELD_NUMBER: _ClassVar[int]
        ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.ComponentIdentifier]
        def __init__(self, ids: _Optional[_Iterable[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]]] = ...) -> None: ...
    class BlendShapeWeights(_message.Message):
        __slots__ = ("weights",)
        class BlendShapeWeight(_message.Message):
            __slots__ = ("index", "weight")
            INDEX_FIELD_NUMBER: _ClassVar[int]
            WEIGHT_FIELD_NUMBER: _ClassVar[int]
            index: int
            weight: float
            def __init__(self, index: _Optional[int] = ..., weight: _Optional[float] = ...) -> None: ...
        WEIGHTS_FIELD_NUMBER: _ClassVar[int]
        weights: _containers.RepeatedCompositeFieldContainer[SkinnedMeshRendererUpdate.BlendShapeWeights.BlendShapeWeight]
        def __init__(self, weights: _Optional[_Iterable[_Union[SkinnedMeshRendererUpdate.BlendShapeWeights.BlendShapeWeight, _Mapping]]] = ...) -> None: ...
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    MESH_FIELD_NUMBER: _ClassVar[int]
    ROOT_BONE_FIELD_NUMBER: _ClassVar[int]
    BONES_FIELD_NUMBER: _ClassVar[int]
    BLEND_SHAPE_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    component: _identifiers_pb2.ComponentIdentifier
    mesh: _identifiers_pb2.AssetIdentifier
    root_bone: _identifiers_pb2.ComponentIdentifier
    bones: SkinnedMeshRendererUpdate.Bones
    blend_shape_weights: SkinnedMeshRendererUpdate.BlendShapeWeights
    def __init__(self, component: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., mesh: _Optional[_Union[_identifiers_pb2.AssetIdentifier, _Mapping]] = ..., root_bone: _Optional[_Union[_identifiers_pb2.ComponentIdentifier, _Mapping]] = ..., bones: _Optional[_Union[SkinnedMeshRendererUpdate.Bones, _Mapping]] = ..., blend_shape_weights: _Optional[_Union[SkinnedMeshRendererUpdate.BlendShapeWeights, _Mapping]] = ...) -> None: ...
