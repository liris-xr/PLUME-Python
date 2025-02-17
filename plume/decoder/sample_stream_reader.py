from __future__ import annotations

import io
from typing import Union, Type, TypeVar, Optional, Sequence, Tuple
from delimited_protobuf import read as _read_delimited
from plume.sample import packed_sample_pb2
from google.protobuf.message import Message
from google.protobuf import symbol_database
from warnings import warn

import lz4.frame

symbol_database = symbol_database.Default()

LZ4_MAGIC_NUMBER = bytes.fromhex("184d2204")

T = TypeVar("T", bound=Message)


class SampleStreamReader:
    def __init__(self, stream: Union[io.RawIOBase, io.BufferedIOBase]):
        assert isinstance(
            stream, (io.RawIOBase, io.BufferedIOBase)
        ), "Expected a binary stream"

        prev_pos = stream.tell()
        magic_number = stream.read(4)[::-1]

        if magic_number == LZ4_MAGIC_NUMBER:
            stream.seek(prev_pos)
            self._stream = lz4.frame.LZ4FrameFile(stream)
        else:
            self._stream = stream

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read_next(self) -> packed_sample_pb2.PackedSample:
        try:
            packed_sample = _read_delimited(
                self._stream, packed_sample_pb2.PackedSample
            )
        except EOFError:
            return None
        return packed_sample

    def parse_next(
        self, type_filter: Optional[Union[Type[T], Sequence[Type[T]]]] = None
    ) -> Tuple[T, Optional[int]]:
        """
        Parse the next sample of the given type from the stream.

        Args:
            type_filter: The type of the sample to parse. If None, any sample will be parsed.

        Returns:
            A tuple containing the parsed sample and an optional timestamp of the sample in nanoseconds.
        """

        while True:
            packed_sample = self.read_next()

            if packed_sample is None:
                return None, None

            if type_filter is not None:
                expected_type_names = (
                    [t.DESCRIPTOR.full_name for t in type_filter]
                    if isinstance(type_filter, Sequence)
                    else [type_filter.DESCRIPTOR.full_name]
                )

                if packed_sample.payload.TypeName() not in expected_type_names:
                    continue

            try:
                parsed_payload = symbol_database.GetSymbol(
                    packed_sample.payload.TypeName()
                )()
            except KeyError:
                warn(
                    f"Failed to get proto class for type {packed_sample.payload.TypeName()}"
                )
                return None, None

            if not packed_sample.payload.Unpack(parsed_payload):
                warn(
                    f"Failed to unpack payload with type name {packed_sample.payload.DESCRIPTOR.full_name}. Skipping."
                )
                return None, None

            return parsed_payload, (
                packed_sample.timestamp
                if packed_sample.HasField("timestamp")
                else None
            )

    @staticmethod
    def open(file: str) -> SampleStreamReader:
        return SampleStreamReader(io.open(file, "rb"))

    def close(self):
        self._stream.close()
