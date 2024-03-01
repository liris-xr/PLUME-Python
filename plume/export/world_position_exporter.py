from __future__ import annotations

from dataclasses import dataclass, field
from copy import deepcopy
import numpy as np
import quaternion
from plume.filtering import filter_samples
from plume.record import Frame
from plume.samples.unity.transform_pb2 import TransformCreate, TransformUpdate, TransformDestroy
from tqdm import tqdm

@dataclass
class LocalTransform:
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

@dataclass(frozen=True)
class WorldTransform:
    world_position: np.ndarray
    world_rotation: quaternion
    world_scale: np.ndarray

@dataclass
class FrameTransforms:
    timestamp: int
    frame_number: int
    transforms: list[LocalTransform]

def compute_world_positions(frames: list[Frame]) -> list[dict[str, WorldTransform]]:

    world_transforms: list[dict[str, WorldTransform]] = []

    last_frame_local_transforms = None

    for frame in tqdm(frames, desc="Computing world positions"):
        if last_frame_local_transforms is None:
            frame_local_transforms: dict[str, LocalTransform] = {}
        else:
            # Copy all previous transforms for the new frame
            frame_local_transforms = deepcopy(last_frame_local_transforms)

        transform_create_samples = filter_samples(frame.data, TransformCreate)
        transform_destroy_samples = filter_samples(frame.data, TransformDestroy)
        transform_update_samples = filter_samples(frame.data, TransformUpdate)

        # Add newly created transforms
        for transform_create_sample in transform_create_samples:
            transform_guid = transform_create_sample.payload.id.component_id
            if transform_guid not in frame_local_transforms:
                frame_local_transforms[transform_guid] = LocalTransform()

        # Remove transforms that were destroyed in this frame
        for transform_destroy_sample in transform_destroy_samples:
            transform_guid = transform_destroy_sample.payload.id.component_id
            if transform_guid in frame_local_transforms:
                del frame_local_transforms[transform_guid]

        # Apply transform updates
        for transform_update_sample in transform_update_samples:
            transform_guid = transform_update_sample.payload.id.component_id
            local_transform = frame_local_transforms[transform_guid]
            if transform_update_sample.payload.HasField('local_position'):
                local_position = transform_update_sample.payload.local_position
                local_transform.local_position = np.array([local_position.x, local_position.y, local_position.z])
            if transform_update_sample.payload.HasField('local_rotation'):
                local_rotation = transform_update_sample.payload.local_rotation
                local_transform.local_rotation = np.quaternion(local_rotation.w, local_rotation.x, local_rotation.y, local_rotation.z)
            if transform_update_sample.payload.HasField('local_scale'):
                local_scale = transform_update_sample.payload.local_scale
                local_transform.local_scale = np.array([local_scale.x, local_scale.y, local_scale.z])
            if transform_update_sample.payload.HasField('parent_transform_id'):
                parent_transform_guid = transform_update_sample.payload.parent_transform_id.component_id
                if parent_transform_guid == "00000000000000000000000000000000": # null guid
                    local_transform.parent_transform = None
                else:
                    if parent_transform_guid not in frame_local_transforms:
                        frame_local_transforms[parent_transform_guid] = LocalTransform()
                    local_transform.parent_transform = frame_local_transforms[parent_transform_guid]

        frame_world_transforms: dict[str, WorldTransform] = {}

        # When all transforms are updated, compute world transforms
        for transform_guid, local_transform in frame_local_transforms.items():
            world_transform = WorldTransform(world_position=local_transform.get_world_position(),
                                             world_rotation=local_transform.get_world_rotation(),
                                             world_scale=local_transform.get_world_scale())
            frame_world_transforms[transform_guid] = world_transform
        
        world_transforms.append(frame_world_transforms)
        last_frame_local_transforms = frame_local_transforms

    return world_transforms
            
