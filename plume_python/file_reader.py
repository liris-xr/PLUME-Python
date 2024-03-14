from io import BytesIO
from typing import BinaryIO

import lz4.frame


def _is_lz4_compressed(raw_bytes: bytes) -> bool:
    magic_number = raw_bytes[:4][::-1]
    return magic_number == bytes.fromhex("184d2204")


def read_file(filepath: str) -> BinaryIO:
    if not filepath.endswith('.plm'):
        raise ValueError("File must be a .plm file")

    with open(filepath, "rb") as file:
        raw_bytes = file.read()

        if _is_lz4_compressed(raw_bytes):
            decompressor = lz4.frame.LZ4FrameDecompressor()
            return BytesIO(decompressor.decompress(raw_bytes))
        else:
            return BytesIO(raw_bytes)
