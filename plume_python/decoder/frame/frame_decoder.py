from plume.sample.unity.frame_pb2 import Frame as FrameSample
from plume.sample.unity.identifiers_pb2 import (
    SceneIdentifier,
    GameObjectIdentifier,
    ComponentIdentifier,
    AssetIdentifier
)

from plume_python.decoder.sample_registry import get_message_class_from_type_name
from plume_python.decoder.frame.frame_data_decoder_registry import (
    get_frame_data_decoder,
)

from plume_python.reader.sample_stream_reader import SampleStreamReader
from plume_python.proxy.unity.asset import Asset
from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.scene import Scene
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.component.transform import Transform

from uuid import UUID
from google.protobuf.message import Message
from warnings import warn

from typing import TypeVar, Type, Iterator

NULL_GUID = UUID(int=0)
TV = TypeVar("TV", bound=Component)

class FrameDecoder(Iterator[Frame]):

    _stream_reader: SampleStreamReader
    _decoded_frame: Frame

    def __init__(self, filepath: str):
        self._stream_reader = SampleStreamReader.open(filepath)
        self._decoded_frame = Frame()

    def close(self):
        self._stream_reader.close()

    def __next__(self) -> Frame:
        frame_sample, time_ns = self._stream_reader.parse_next(FrameSample)

        if frame_sample is None:
            raise StopIteration

        decode_frame(self._decoded_frame, frame_sample, time_ns)
        return self._decoded_frame
    

def decode_frame(frame: Frame, frame_sample: FrameSample, time_ns: int):

    frame._frame_number = frame_sample.frame_number
    frame._time_ns = time_ns

    for data in frame_sample.data:
        cls = get_message_class_from_type_name(data.TypeName())

        if cls is None:
            warn(f"Failed to get data payload class for type {data.TypeName()}")
            continue

        parsed_payload: Message = cls()
        success = data.Unpack(parsed_payload)
        if not success:
            warn(f"Failed to unpack payload with type {data.TypeName()}")
            continue

        try:
            frame_data_decoder = get_frame_data_decoder(type(parsed_payload))
        except:
            warn(
                f"Failed to get decoder for {parsed_payload.DESCRIPTOR.full_name}. Skipping."
            )
            continue

        frame_data_decoder.decode(frame, parsed_payload)


def get_or_create_scene(frame: Frame, scene_id: SceneIdentifier) -> Scene:
    scene = frame.scenes.get_by_guid(scene_id.guid)

    if scene is None:

        scene_guid = UUID(scene_id.guid)

        if scene_guid == NULL_GUID:
            return None

        scene = Scene(
            guid=scene_guid,
            name=scene_id.name,
            asset_bundle_path=scene_id.asset_bundle_path,
        )
        frame.scenes._add_scene(scene)

    return scene


def get_or_create_game_object(
    frame: Frame, game_object_id: GameObjectIdentifier
) -> GameObject:
    scene = get_or_create_scene(frame, game_object_id.scene)

    if scene is None:
        return None

    game_object = scene.game_objects.get_by_guid(game_object_id.guid)

    if game_object is None:

        game_object_guid = UUID(game_object_id.guid)

        if game_object_guid == NULL_GUID:
            return None

        game_object = GameObject(
            guid=game_object_guid,
            scene=scene,
        )
        scene.game_objects._add(game_object)

    transform = game_object.components.get_by_guid(game_object_id.transform_guid)

    if transform is None:
        transform = Transform(
            guid=game_object_id.transform_guid,
            game_object=game_object,
        )
        game_object.components._add(transform)

    return game_object


def get_or_create_component(
    frame: Frame,
    component_id: ComponentIdentifier,
    component_proxy_type: Type[TV],
) -> TV:
    game_object = get_or_create_game_object(frame, component_id.game_object)

    if game_object is None:
        return None

    component = game_object.components.get_by_guid(component_id.guid)

    if component is not None and not isinstance(component, component_proxy_type):
        warn(
            f"Found component with guid {component_id.guid} but it is not of the expected type {component_proxy_type.__name__}"
        )

    if component is None:
        component_guid = UUID(component_id.guid)

        if component_guid == NULL_GUID:
            return None

        component = component_proxy_type(
            guid=component_guid,
            game_object=game_object,
        )
        game_object.components._add(component)

    return component


def get_or_create_asset(frame: Frame, asset_id: AssetIdentifier) -> None:
    asset = frame.assets.get_by_guid(asset_id.guid)

    if asset is None:
        asset_uuid = UUID(asset_id.guid)

        if asset_uuid == NULL_GUID:
            return None

        asset = Asset(
            guid=asset_uuid,
            asset_bundle_path=asset_id.asset_bundle_path,
        )
        frame.assets._add(asset)

    return asset

def destroy_scene(frame: Frame, scene_id: SceneIdentifier) -> bool:
    scene = frame.scenes.get_by_guid(scene_id.guid)

    if scene is None:
        return False

    frame.scenes._remove(scene)
    return True


def destroy_game_object(frame: Frame, game_object_id: GameObjectIdentifier) -> bool:
    scene = frame.scenes.get_by_guid(game_object_id.scene.guid)

    if scene is None:
        return False

    game_object = scene.game_objects.get_by_guid(game_object_id.guid)

    if game_object is None:
        return False

    scene.game_objects._remove_by_guid(game_object)

    for component in game_object.components:
        game_object.components._remove_by_guid(component.guid)

    return True


def destroy_component(frame: Frame, component_id: ComponentIdentifier) -> bool:
    scene = frame.scenes.get_by_guid(component_id.game_object.scene.guid)

    if scene is None:
        return False

    game_object = scene.game_objects.get_by_guid(component_id.game_object.guid)

    if game_object is None:
        return False

    component = game_object.components.get_by_guid(component_id.guid)

    if component is None:
        return False

    game_object.components._remove_by_guid(component)
    return True
