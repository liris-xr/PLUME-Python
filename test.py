from tqdm import tqdm
from plume_python.decoder.record_decoder import RecordDecoder

from plume_python.proxy.unity.component.transform import Transform
from plume_python.proxy.unity.component.camera import Camera

record_decoder = RecordDecoder("tests/record.plm")

# for marker in tqdm(record_decoder.markers):
#     print(marker)

# for signal in tqdm(record_decoder.signals):
#     print(signal)

# for input in tqdm(record_decoder.inputs):
#     print(input)

for frame in tqdm(record_decoder.frames):
    for scene in frame.scenes:
        for game_object in scene.game_objects:
            cameras = game_object.components.get_by_type(Camera)

            if cameras:
                print(cameras[0])
