from plume.samples.packed_sample_pb2 import PackedSample
from delimited_protobuf import read as __read_delimited
import lz4.frame

# Required to add all DESCRIPTORS into the default descriptor pool
from plume.samples import *

from io import BytesIO

def __read_packed_samples(data: BytesIO):
    packed_samples = []
    total_size = len(data.getbuffer())

    while data.tell() < total_size:
        packed_sample = __read_delimited(data, PackedSample)
        packed_samples.append(packed_sample)
    return packed_samples

def __is_lz4_compressed(raw_bytes: bytes) -> bool:
    magic_number = raw_bytes[:4][::-1]
    return magic_number == bytes.fromhex("184d2204")

def read_samples_from_file(filepath: str):

    with open(filepath, "rb") as file:
        raw_bytes = file.read()

        if __is_lz4_compressed(raw_bytes):
            decompressor = lz4.frame.LZ4FrameDecompressor()
            data = BytesIO(decompressor.decompress(raw_bytes))
        else:
            data = BytesIO(raw_bytes)

        return __read_packed_samples(data)
