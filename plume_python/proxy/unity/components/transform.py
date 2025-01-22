from plume_python.proxy.unity.component import Component
from plume_python.proxy.unity.gameobject import GameObject
from plume_python.proxy.common.vector3 import Vector3
from plume_python.proxy.common.quaternion import Quaternion

class Transform(Component):
    sibling_index: int
    local_position: Vector3
    local_rotation: Quaternion
    local_scale: Vector3

    def __init__(self, uuid: str, gameobject_uuid: str):
        super().__init__(uuid, gameobject_uuid)
        self.sibling_index = 0
        self.local_position = Vector3()
        self.local_rotation = Quaternion()
        self.local_scale = Vector3()