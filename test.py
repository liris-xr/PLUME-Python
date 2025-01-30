from tqdm import tqdm
from plume_python.decoder.record_decoder import RecordDecoder

from plume_python.proxy.unity.component.transform import Transform
from plume_python.proxy.unity.component.camera import Camera
from plume_python.proxy.unity.component.mesh_filter import MeshFilter

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
            mfs = game_object.components.get_by_type(MeshFilter)

            if mfs and mfs[0].mesh is None:
                print(mfs[0].game_object)
