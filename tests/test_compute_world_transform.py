from __future__ import annotations
import plume.record_reader
import plume.sample_parser
import plume.frame_parser
import os.path
from dataclasses import dataclass, field
from copy import deepcopy
import numpy as np
import quaternion

from plume.samples.unity.frame_pb2 import Frame
from plume.samples.unity.transform_pb2 import TransformCreate, TransformUpdate, TransformDestroy

@dataclass
class LocalTransform:
    guid: str
    local_position: np.ndarray = field(default_factory=lambda: np.zeros(3, dtype=np.float32))
    local_rotation: quaternion = field(default_factory=lambda: np.quaternion(1, 0, 0, 0))
    local_scale: np.ndarray = field(default_factory=lambda: np.ones(3, dtype=np.float32))
    parent_transform: LocalTransform = None

    def compute_trs_matrix(self):
        translation_matrix = np.eye(4)
        translation_matrix[0:3, 3] = self.local_position
        rotation_matrix = np.eye(4)
        rotation_matrix[0:3, 0:3] = quaternion.as_rotation_matrix(self.local_rotation)
        scale_matrix = np.eye(4)
        scale_matrix[0:3, 0:3] = np.diag(self.local_scale)
        return translation_matrix @ rotation_matrix @ scale_matrix

    def compute_local_to_world_matrix(self):
        local_matrix = self.compute_trs_matrix()
        if self.parent_transform is not None:
            parent_matrix = self.parent_transform.compute_local_to_world_matrix()
            return parent_matrix @ local_matrix
        else:
            return local_matrix

    def get_world_position(self):
        local_to_world_matrix = self.compute_local_to_world_matrix()
        return local_to_world_matrix[0:3, 3].transpose()
    
    def get_world_rotation(self):
        local_to_world_matrix = self.compute_local_to_world_matrix()
        local_to_world_matrix[0:3, 0] /= np.linalg.norm(local_to_world_matrix[0:3, 0])
        local_to_world_matrix[0:3, 1] /= np.linalg.norm(local_to_world_matrix[0:3, 1])
        local_to_world_matrix[0:3, 2] /= np.linalg.norm(local_to_world_matrix[0:3, 2])
        return quaternion.from_rotation_matrix(local_to_world_matrix[0:3, 0:3])

    def get_world_scale(self):
        local_to_world_matrix = self.compute_local_to_world_matrix()
        sx = np.linalg.norm(local_to_world_matrix[0:3, 0])
        sy = np.linalg.norm(local_to_world_matrix[0:3, 1])
        sz = np.linalg.norm(local_to_world_matrix[0:3, 2])
        return np.array([sx, sy, sz])

@dataclass
class FrameTransforms:
    timestamp: int
    frame_number: int
    transforms: list[LocalTransform]

def test_parse_samples(samples):
    unpacked_frames = plume.sample_parser.parse_samples(samples, filter_descriptors=[Frame.DESCRIPTOR])

    frames_transforms = list[FrameTransforms]()
    frame_transforms = None
    
    print(f"Loaded {len(unpacked_frames)} frames.")

    for frame in unpacked_frames:
        if frame_transforms is None:
            frame_transforms = FrameTransforms(frame.timestamp, frame.payload.frame_number, [])
        else:
            # Copy all previous transforms for the new frame
            frame_transforms = FrameTransforms(frame.timestamp, frame.payload.frame_number, deepcopy(frame_transforms.transforms))
            frames_transforms.append(frame_transforms)

        transform_create = plume.frame_parser.parse_frame_data(frame, filter_descriptors=[TransformCreate.DESCRIPTOR])
        transform_destroy = plume.frame_parser.parse_frame_data(frame, filter_descriptors=[TransformDestroy.DESCRIPTOR])
        transform_updates = plume.frame_parser.parse_frame_data(frame, filter_descriptors=[TransformUpdate.DESCRIPTOR])

        # Add newly created transforms
        for transform in transform_create:
            transform_guid = transform.id.component_id
            frame_transforms.transforms.append(LocalTransform(transform_guid))

        # Remove transforms that were destroyed in this frame
        for transform in transform_destroy:
            transform_guid = transform.id.component_id
            frame_transforms.transforms = [t for t in frame_transforms.transforms if t.guid != transform_guid]

        # Apply transform updates
        for transform_update in transform_updates:
            transform_guid = transform_update.id.component_id
            transform = next((t for t in frame_transforms.transforms if t.guid == transform_guid), None)
            if transform_update.HasField('local_position'):
                transform.local_position = np.array([transform_update.local_position.x, transform_update.local_position.y, transform_update.local_position.z])
            if transform_update.HasField('local_rotation'):
                transform.local_rotation = np.quaternion(transform_update.local_rotation.w, transform_update.local_rotation.x, transform_update.local_rotation.y, transform_update.local_rotation.z)
            if transform_update.HasField('local_scale'):
                transform.local_scale = np.array([transform_update.local_scale.x, transform_update.local_scale.y, transform_update.local_scale.z])
            if transform_update.HasField('parent_transform_id'):
                parent_transform_guid = transform_update.parent_transform_id.component_id
                transform.parent_transform = next((t for t in frame_transforms.transforms if t.guid == parent_transform_guid), None)

        for transform in frame_transforms.transforms:
            print(transform.guid, transform.get_world_position())
            print(transform.guid, transform.get_world_scale())
            print(transform.guid, transform.get_world_rotation())

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "record_0.plm")
    samples = plume.record_reader.read_samples_from_file(file_path)
    test_parse_samples(samples)