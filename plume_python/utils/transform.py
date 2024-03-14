from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import quaternion
from tqdm import tqdm
from typing import Optional

from ..record import Record, FrameSample, RawSample
from ..samples.unity.transform_pb2 import TransformCreate, TransformUpdate, TransformDestroy


def _extract_transform_samples_from_frame(frame: FrameSample):
    transform_create_samples: list[RawSample[TransformCreate]] = []
    transform_update_samples: list[RawSample[TransformUpdate]] = []
    transform_destroy_samples: list[RawSample[TransformDestroy]] = []

    for frame_data in frame.data:
        if isinstance(frame_data.payload, TransformCreate):
            transform_create_samples.append(frame_data)
        elif isinstance(frame_data.payload, TransformUpdate):
            transform_update_samples.append(frame_data)
        elif isinstance(frame_data.payload, TransformDestroy):
            transform_destroy_samples.append(frame_data)

    return transform_create_samples, transform_destroy_samples, transform_update_samples


@dataclass(slots=True)
class Transform:
    _local_position: np.ndarray = field(default_factory=lambda: np.array(3, dtype=np.float32))
    _local_rotation: quaternion.quaternion = field(default_factory=lambda: quaternion.quaternion(1, 0, 0, 0))
    _local_scale: np.ndarray = field(default_factory=lambda: np.array(4, dtype=np.float32))
    _local_T_mtx: np.ndarray = field(default_factory=lambda: np.eye(4, dtype=np.float32))
    _local_R_mtx: np.ndarray = field(default_factory=lambda: np.eye(4, dtype=np.float32))
    _local_S_mtx: np.ndarray = field(default_factory=lambda: np.eye(4, dtype=np.float32))
    _local_to_world_mtx: np.ndarray = None
    _parent: Optional[Transform] = None
    _dirty: bool = True

    def copy(self) -> Transform:
        parent_copy = None if self._parent is None else self._parent.copy()
        copy = Transform(_local_position=self._local_position, _local_rotation=self._local_rotation,
                         _local_scale=self._local_scale, _local_T_mtx=self._local_T_mtx, _local_R_mtx=self._local_R_mtx,
                         _local_S_mtx=self._local_S_mtx, _parent=parent_copy, _dirty=self._dirty,
                         _local_to_world_mtx=self._local_to_world_mtx)
        return copy

    def _is_dirty(self) -> bool:
        return self._dirty or self._parent is not None and self._parent._is_dirty()

    def set_local_position(self, local_position: np.ndarray):
        self._local_T_mtx[0:3, 3] = local_position
        self._local_position = local_position
        self._dirty = True

    def set_local_rotation(self, local_rotation: quaternion):
        self._local_R_mtx[0:3, 0:3] = quaternion.as_rotation_matrix(local_rotation)
        self._local_rotation = local_rotation
        self._dirty = True

    def set_local_scale(self, local_scale: np.ndarray):
        self._local_S_mtx[0, 0] = local_scale[0]
        self._local_S_mtx[1, 1] = local_scale[1]
        self._local_S_mtx[2, 2] = local_scale[2]
        self._local_scale = local_scale
        self._dirty = True

    def get_local_position(self) -> np.ndarray:
        return self._local_position

    def get_local_rotation(self) -> quaternion:
        return self._local_rotation

    def get_local_scale(self) -> np.ndarray:
        return self._local_scale

    def set_parent(self, parent: Optional[Transform]):
        self._parent = parent
        self._dirty = True

    def get_parent(self) -> Optional[Transform]:
        return self._parent

    def get_local_to_world_matrix(self) -> np.ndarray:
        if self._is_dirty() or self._local_to_world_mtx is None:

            trs_mtx = self._local_T_mtx @ self._local_R_mtx @ self._local_S_mtx

            if self._parent is None:
                self._local_to_world_mtx = trs_mtx
            else:
                self._local_to_world_mtx = self._parent.get_local_to_world_matrix() @ trs_mtx

            self._dirty = False

        return self._local_to_world_mtx

    def get_world_position(self) -> np.ndarray:
        return self.get_local_to_world_matrix()[0:3, 3].transpose()

    def get_world_rotation(self) -> quaternion:
        return quaternion.from_rotation_matrix(self.get_local_to_world_matrix()[0:3, 0:3])

    def get_world_scale(self) -> np.ndarray:
        local_to_world_mtx = self.get_local_to_world_matrix()
        sx = np.linalg.norm(local_to_world_mtx[0:3, 0])
        sy = np.linalg.norm(local_to_world_mtx[0:3, 1])
        sz = np.linalg.norm(local_to_world_mtx[0:3, 2])
        scale = np.array([sx, sy, sz])
        return scale


@dataclass(frozen=True, slots=True)
class TimestampedTransform:
    timestamp: int
    frame_number: int
    transform: Transform

    def get_local_position(self) -> np.ndarray:
        return self.transform.get_local_position()

    def get_local_rotation(self) -> quaternion:
        return self.transform.get_local_rotation()

    def get_local_scale(self) -> np.ndarray:
        return self.transform.get_local_scale()

    def get_world_position(self) -> np.ndarray:
        return self.transform.get_world_position()

    def get_world_rotation(self) -> quaternion:
        return self.transform.get_world_rotation()

    def get_world_scale(self) -> np.ndarray:
        return self.transform.get_world_scale()


def compute_transform_time_series(record: Record, guid: str) -> list[TimestampedTransform]:
    transform_time_series = compute_transforms_time_series(record, {guid})
    return transform_time_series.get(guid, {})


def compute_transforms_time_series(record: Record, included_guids: set[str] = None) \
        -> dict[str, list[TimestampedTransform]]:
    result: dict[str, list[TimestampedTransform]] = {}
    current_transforms: dict[str, Transform] = {}

    for frame in tqdm(record.frames, desc="Computing world positions"):

        creation_samples, destruction_samples, update_samples = _extract_transform_samples_from_frame(frame)

        # Add newly created transforms
        for creation_sample in creation_samples:
            guid = creation_sample.payload.id.component_id
            if guid not in current_transforms:
                current_transforms[guid] = Transform()

        # Remove transforms that were destroyed in this frame
        for destruction_sample in destruction_samples:
            guid = destruction_sample.payload.id.component_id
            if guid in current_transforms:
                del current_transforms[guid]

        # Apply transform updates
        for update_sample in update_samples:
            guid = update_sample.payload.id.component_id
            local_transform = current_transforms[guid]
            if update_sample.payload.HasField('local_position'):
                local_position = update_sample.payload.local_position
                local_transform.set_local_position(np.array([local_position.x, local_position.y, local_position.z]))
            if update_sample.payload.HasField('local_rotation'):
                local_rotation = update_sample.payload.local_rotation
                q = quaternion.quaternion(local_rotation.w, local_rotation.x, local_rotation.y, local_rotation.z)
                local_transform.set_local_rotation(q)
            if update_sample.payload.HasField('local_scale'):
                local_scale = update_sample.payload.local_scale
                local_transform.set_local_scale(np.array([local_scale.x, local_scale.y, local_scale.z]))
            if update_sample.payload.HasField('parent_transform_id'):
                parent_guid = update_sample.payload.parent_transform_id.component_id
                if parent_guid == "00000000000000000000000000000000":  # null guid
                    local_transform.set_parent(None)
                elif parent_guid in current_transforms:
                    local_transform.set_parent(current_transforms[parent_guid])
                else:
                    parent = Transform()
                    local_transform.set_parent(parent)
                    current_transforms[parent_guid] = parent

        if included_guids is not None:
            for included_guid in included_guids:
                if included_guid in current_transforms:
                    if included_guid not in result:
                        result[included_guid] = []
                    transform_copy = current_transforms[included_guid].copy()
                    timestamped_transform = TimestampedTransform(frame.timestamp, frame.frame_number, transform_copy)
                    result[included_guid].append(timestamped_transform)
        else:
            for guid, transform in current_transforms.items():
                if guid not in result:
                    result[guid] = []
                transform_copy = transform.copy()
                result[guid].append(TimestampedTransform(frame.timestamp, frame.frame_number, transform_copy))

    return result
