import lz4.frame
import lz4
from dataclasses import dataclass, field
from typing import List, Tuple, Set, Dict
import time

from plume.sample.packed_sample_pb2 import PackedSample

import os
import numpy as np


@dataclass
class RecordIndex:

    chunk_size: int

    type_name_to_id: Dict[str, int] = field(default_factory=dict)
    next_id: int = 0

    _initial_size: int = 1000

    def __post_init__(self):
        # Initialize arrays with pre-allocated space
        self.timestamps = np.zeros(self._initial_size, dtype=np.int64)
        self.type_ids = np.zeros(self._initial_size, dtype=np.int32)
        self.chunk_start_indices = np.zeros(self._initial_size, dtype=np.int32)
        self.chunk_end_indices = np.zeros(self._initial_size, dtype=np.int32)
        self.uncompressed_chunk_offsets = np.zeros(self._initial_size, dtype=np.int32)
        self.uncompressed_sample_sizes = np.zeros(self._initial_size, dtype=np.int32)
        self._current_size = 0

    def _resize_if_needed(self):
        if self._current_size >= len(self.timestamps):
            new_size = len(self.timestamps) * 2
            self.timestamps = np.resize(self.timestamps, new_size)
            self.type_ids = np.resize(self.type_ids, new_size)
            self.chunk_start_indices = np.resize(self.chunk_start_indices, new_size)
            self.chunk_end_indices = np.resize(self.chunk_end_indices, new_size)
            self.uncompressed_chunk_offsets = np.resize(
                self.uncompressed_chunk_offsets, new_size
            )
            self.uncompressed_sample_sizes = np.resize(
                self.uncompressed_sample_sizes, new_size
            )

    def add_entry(
        self,
        time_ns: int,
        type_name: str,
        compressed_chunk_start: int,
        compressed_chunk_end: int,
        uncompressed_offset: int,
        sample_size: int,
    ):
        if type_name not in self.type_name_to_id:
            type_id = self.next_id
            self.type_name_to_id[type_name] = type_id
            self.next_id += 1
        else:
            type_id = self.type_name_to_id[type_name]

        self._resize_if_needed()

        # Add values to arrays at current position
        self.timestamps[self._current_size] = time_ns if time_ns is not None else -1
        self.type_ids[self._current_size] = type_id
        self.chunk_start_indices[self._current_size] = compressed_chunk_start
        self.chunk_end_indices[self._current_size] = compressed_chunk_end
        self.uncompressed_chunk_offsets[self._current_size] = uncompressed_offset
        self.uncompressed_sample_sizes[self._current_size] = sample_size

        self._current_size += 1

    def save_to_file(self, filepath: str):
        """Save the RecordIndex to a file using np.savez"""
        # Trim arrays to actual size
        actual_time_ns = self.timestamps[:self._current_size]
        actual_type_id = self.type_ids[:self._current_size]
        actual_chunk_start = self.chunk_start_indices[:self._current_size]
        actual_chunk_end = self.chunk_end_indices[:self._current_size]
        actual_offset = self.uncompressed_chunk_offsets[:self._current_size]
        actual_size = self.uncompressed_sample_sizes[:self._current_size]

        np.savez_compressed(
            filepath,
            chunk_size=self.chunk_size,
            type_name_to_id=np.array(list(self.type_name_to_id.items())),
            time_ns=actual_time_ns,
            type_id=actual_type_id,
            chunk_start_idx=actual_chunk_start,
            chunk_end_idx=actual_chunk_end,
            uncompressed_chunk_offset=actual_offset,
            uncompressed_sample_size=actual_size
        )

    @staticmethod
    def load_from_file(filepath: str):
        """Load a RecordIndex from a file using np.load"""
        with np.load(filepath, allow_pickle=True) as data:
            chunk_size = data['chunk_size']
            type_name_to_id = dict(data['type_name_to_id'])

            index = RecordIndex(chunk_size)
            index.type_name_to_id = type_name_to_id

            index.timestamps = data['time_ns']
            index.type_ids = data['type_id']
            index.chunk_start_indices = data['chunk_start_idx']
            index.chunk_end_indices = data['chunk_end_idx']
            index.uncompressed_chunk_offsets = data['uncompressed_chunk_offset']
            index.uncompressed_sample_sizes = data['uncompressed_sample_size']

            index._current_size = len(index.timestamps)

        return index

def decode_varint(buffer: memoryview, offset: int) -> Tuple[int, int]:
    result = 0
    shift = 0
    for i in range(offset, offset + 10):  # Max 10 bytes for a varint
        byte = buffer[i]
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return result, i - offset + 1
        shift += 7
    raise ValueError("Malformed varint")


def process_file(filepath: str):

    file_size = os.path.getsize(filepath)

    with open(filepath, "rb") as f:
        decompressor = lz4.frame.LZ4FrameDecompressor()
        packed_sample = PackedSample()
        chunk_size = 1024 * 1024

        # Preallocate buffer
        buffer = bytearray(chunk_size * 2)
        buffer_view = memoryview(buffer)

        chunk_indices = []
        chunk_sizes = []

        chunk_index = 0
        buffer_size = 0
        uncompressed_offset = 0

        index = RecordIndex(chunk_size)

        while chunk_index * chunk_size < file_size:

            # Read compressed chunk
            compressed_chunk = f.read(chunk_size)

            # Decompress
            uncompressed_chunk = decompressor.decompress(compressed_chunk)
            chunk_size_current = len(uncompressed_chunk)

            # Extend buffer if needed
            if buffer_size + chunk_size_current > len(buffer):
                new_buffer = bytearray(
                    max(len(buffer) * 2, buffer_size + chunk_size_current)
                )
                new_buffer[:buffer_size] = buffer[:buffer_size]
                buffer = new_buffer
                buffer_view = memoryview(buffer)

            # Append chunk to buffer
            buffer[buffer_size : buffer_size + chunk_size_current] = uncompressed_chunk
            buffer_size += chunk_size_current
            chunk_indices.append(chunk_index)
            chunk_sizes.append(chunk_size_current)

            # Process messages
            while True:
                try:
                    message_size, varint_len = decode_varint(
                        buffer_view, uncompressed_offset
                    )
                    message_end = uncompressed_offset + varint_len + message_size

                    if message_end > buffer_size:
                        break

                    # Parse message
                    packed_sample.ParseFromString(
                        buffer_view[uncompressed_offset + varint_len : message_end]
                    )

                    index.add_entry(
                        time_ns=(
                            packed_sample.timestamp
                            if packed_sample.HasField("timestamp")
                            else None
                        ),
                        type_name=packed_sample.payload.TypeName(),
                        compressed_chunk_start=chunk_indices[0],
                        compressed_chunk_end=chunk_indices[-1],
                        uncompressed_offset=uncompressed_offset,
                        sample_size=message_size,
                    )

                    uncompressed_offset = message_end

                    # Remove processed chunks from buffer
                    while chunk_sizes and uncompressed_offset >= chunk_sizes[0]:
                        uncompressed_offset -= chunk_sizes[0]
                        buffer_size -= chunk_sizes[0]
                        if buffer_size > 0:
                            buffer_view[:buffer_size] = buffer_view[
                                chunk_sizes[0] : chunk_sizes[0] + buffer_size
                            ]
                        chunk_indices.pop(0)
                        chunk_sizes.pop(0)

                except ValueError:
                    break

            chunk_index += 1

        return index


if __name__ == "__main__":

    start = time.time()
    filepath = "C:/Users/javerlia/Desktop/XP Matthieu/3_2.plm"
    index = process_file(filepath)
    end = time.time()
    print(f"Decoded in {end - start:.2f} seconds")

    start = time.time()
    index_file = "C:/Users/javerlia/Desktop/XP Matthieu/index.npz"
    index.save_to_file(index_file)
    end = time.time()
    print(f"Saved in {end - start:.2f} seconds")

    start = time.time()
    index = RecordIndex.load_from_file(index_file)
    end = time.time()
    print(f"Loaded in {end - start:.2f} seconds")

    # Wait
    input("Press Enter to continue...")

    # # Find the last SampleIndex where the type_name is Frame
    # frame_index = next(
    #     i for i in reversed(indices) if i.type_name == "plume.sample.unity.Frame"
    # )

    # # Convert duration in nanoseconds to HH:MM:SS:ms
    # duration_s = frame_index.time_ns / 1e9
    # duration = time.strftime("%H:%M:%S", time.gmtime(duration_s))
    # duration += f".{frame_index.time_ns % 1e9:.0f}"

    # print(duration)

    # print(f"Decoded {len(indices)} messages in {end - start:.2f} seconds")
