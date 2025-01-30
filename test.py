from tqdm import tqdm
from plume_python.decoder.record_decoder import RecordDecoder

from plume_python.proxy.unity.component.xr_base_interactable import XRBaseInteractable

record_decoder = RecordDecoder("tests/record.plm")

# for marker in tqdm(record_decoder.markers):
#     print(marker)

# for signal in tqdm(record_decoder.signals):
#     print(signal)

# for input in tqdm(record_decoder.inputs):
#     print(input)


for frame in tqdm(record_decoder.frames):
    scene1 = frame.scenes.get_by_name("HouseObjectivesSteamAudio")
    egg1 = scene1.game_objects.get_first_by_name("Egg (1)")
    egg1_local_pos = egg1.transform.local_position
    egg1_local_pos_np = egg1_local_pos.to_numpy()
    print(egg1_local_pos_np)