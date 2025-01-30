from tqdm import tqdm
from plume_python.decoder.record_decoder import RecordDecoder

from plume_python.proxy.unity.component.transform import Transform

record_decoder = RecordDecoder("tests/record.plm")

# for marker in tqdm(record_decoder.markers):
#     print(marker)

# for signal in tqdm(record_decoder.signals):
#     print(signal)

for input in tqdm(record_decoder.inputs):
    print(input)

# for frame in tqdm(record_decoder.frames):
#     print(frame)
#     # print(len(frame.scenes), "scenes")
#     # for scene_idx, scene in enumerate(frame.scenes):
#     #     print(f"Scene {scene_idx} has {len(scene.game_objects)} game objects")

#     #     for go_idx, go in enumerate(scene.game_objects):
#     #         print(f"    Game object {go_idx} has {len(go.components)} components")
#     # break
