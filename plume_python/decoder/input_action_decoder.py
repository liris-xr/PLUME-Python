from plume.sample.unity.input_action_pb2 import InputAction as InputActionSample, ButtonValue as ButtonValueSample
from plume.sample.common.vector2_pb2 import Vector2 as Vector2Sample
from plume.sample.common.vector3_pb2 import Vector3 as Vector3Sample
from plume.sample.common.quaternion_pb2 import Quaternion as QuaternionSample

from plume_python.decoder.sample_stream_reader import SampleStreamReader
from plume_python.proxy.unity.input_action import InputAction, InputActionType, ButtonValue
from plume_python.proxy.common.vector2 import Vector2
from plume_python.proxy.common.vector3 import Vector3
from plume_python.proxy.common.quaternion import Quaternion

from typing import Iterator

class InputActionDecoder(Iterator[InputAction]):

    _stream_reader: SampleStreamReader

    def __init__(self, filepath: str):
        self._stream_reader = SampleStreamReader.open(filepath)

    def close(self):
        self._stream_reader.close()

    def __next__(self) -> InputAction:

        input_action_sample, time_ns = self._stream_reader.parse_next(InputActionSample)

        if input_action_sample is None:
            raise StopIteration
        
        input_action_type = InputActionType.from_message(input_action_sample.type)
        binding_paths = input_action_sample.binding_paths
        value_field = input_action_sample.WhichOneof("value")
        value = getattr(input_action_sample, value_field)

        if isinstance(value, Vector2Sample):
            value = Vector2(value.x, value.y)
        elif isinstance(value, Vector3Sample):
            value = Vector3(value.x, value.y, value.z)
        elif isinstance(value, QuaternionSample):
            value = Quaternion(value.x, value.y, value.z, value.w)
        elif isinstance(value, ButtonValueSample):
            value = ButtonValue(value.boolean, value.float, value.threshold)

        return InputAction(
            time_ns=time_ns,
            binding_paths=binding_paths,
            type=input_action_type,
            value=value
        )