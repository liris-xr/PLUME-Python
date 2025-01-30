from tqdm import tqdm
from plume_python.decoder.record_decoder import RecordDecoder

from plume_python.proxy.unity.component.xr_base_interactable import XRBaseInteractable
from plume_python.proxy.unity.component.mesh_filter import MeshFilter

record_decoder = RecordDecoder("tests/record.plm")

# for marker in tqdm(record_decoder.markers):
#     print(marker)

# for signal in tqdm(record_decoder.signals):
#     print(signal)

# for input in tqdm(record_decoder.inputs):
#     print(input)


for frame in tqdm(record_decoder.frames):
    scene = frame.scenes.first_with_name("HouseObjectivesSteamAudio")
    egg1 = scene.game_objects.first_with_name("Egg (1)")
    mfs_go = scene.game_objects.with_component_type(MeshFilter)
    print(len(mfs_go))