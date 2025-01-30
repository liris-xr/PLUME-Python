from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union
from enum import Enum

from plume.sample.unity.input_action_pb2 import InputActionType as InputActionTypeSample

from plume_python.proxy.common.vector2 import Vector2
from plume_python.proxy.common.vector3 import Vector3
from plume_python.proxy.common.quaternion import Quaternion


class InputActionType(Enum):
    UNDEFINED = 0
    VALUE = 1
    BUTTON = 2
    PASSTHROUGH = 3

    @staticmethod
    def from_message(input_action_type: InputActionTypeSample) -> InputActionType:
        if input_action_type == InputActionTypeSample.INPUT_ACTION_TYPE_VALUE:
            return InputActionType.VALUE
        elif input_action_type == InputActionTypeSample.INPUT_ACTION_TYPE_BUTTON:
            return InputActionType.BUTTON
        elif input_action_type == InputActionTypeSample.INPUT_ACTION_TYPE_PASSTHROUGH:
            return InputActionType.PASSTHROUGH
        else:
            return InputActionType.UNDEFINED
        
    def __repr__(self):
        return self.name


@dataclass(frozen=True)
class ButtonValue:
    boolean_value: bool
    float_value: float
    threshold: float


@dataclass(frozen=True)
class InputAction:
    time_ns: int
    binding_paths: List[str]
    type: InputActionType
    value: Union[int, bool, float, Vector2, Vector3, Quaternion, ButtonValue]
