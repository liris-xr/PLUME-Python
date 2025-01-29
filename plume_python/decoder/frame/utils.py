from plume_python.proxy.unity.frame import Frame
from plume_python.proxy.unity.scene import Scene
from plume_python.proxy.unity.game_object import GameObject
from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.component.transform import Transform

from plume.sample.unity.identifiers_pb2 import (
    SceneIdentifier,
    GameObjectIdentifier,
    ComponentIdentifier,
)

from warnings import warn

from typing import TypeVar, Type

TV = TypeVar("TV", bound=Component)


def get_or_create_scene(frame: Frame, scene_id: SceneIdentifier) -> Scene:
    scene = frame.scenes.get_by_guid(scene_id.guid)

    if scene is None:
        scene = Scene(
            guid=scene_id.guid,
            name=scene_id.name,
            asset_bundle_path=scene_id.asset_bundle_path,
        )
        frame.scenes._add_scene(scene)

    return scene


def get_or_create_game_object(
    frame: Frame, game_object_id: GameObjectIdentifier
) -> GameObject:
    scene = get_or_create_scene(frame, game_object_id.scene)

    game_object = scene.game_objects.get_by_guid(game_object_id.guid)

    if game_object is None:
        game_object = GameObject(
            guid=game_object_id.guid,
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
    component = game_object.components.get_by_guid(component_id.guid)

    if component is not None and not isinstance(component, component_proxy_type):
        warn(
            f"Found component with guid {component_id.guid} but it is not of the expected type {component_proxy_type.__name__}"
        )

    if component is None:
        component = component_proxy_type(
            guid=component_id.guid,
            game_object=game_object,
        )
        game_object.components._add(component)

    return component


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
