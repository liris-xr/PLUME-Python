import os.path
from plume.parser import parse_record_from_file
from plume.export.world_position_exporter import compute_world_positions
import cProfile

def test_compute_world_positions():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_2.plm")
    record = parse_record_from_file(file_path)
    world_positions = compute_world_positions(record.frames)
    print(world_positions[1])
    

if __name__ == '__main__':
    test_compute_world_positions()