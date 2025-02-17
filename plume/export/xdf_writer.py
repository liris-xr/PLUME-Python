import xml.etree.ElementTree as ET
from enum import Enum
from io import BytesIO
from typing import Dict, Optional, Any

import numpy as np
import datetime

BYTE_ORDER = "big"
STR_ENCODING = "utf-8"

formats = {
    "double64": np.float64,
    "float32": np.float32,
    "string": str,
    "int32": np.int32,
    "int16": np.int16,
    "int8": np.int8,
    "int64": np.int64,
}

DataType = (
    np.int8
    | np.int16
    | np.int32
    | np.int64
    | np.uint8
    | np.uint16
    | np.uint32
    | np.uint64
    | np.float32
    | np.float64
    | str
)


class ChunkTag(Enum):
    FILE_HEADER = 1
    STREAM_HEADER = 2
    SAMPLES = 3
    CLOCK_OFFSET = 4
    BOUNDARY = 5
    STREAM_FOOTER = 6
    UNDEFINED = 0


def _format_timestamp(timestamp: datetime.datetime) -> str:
    datetime_str = timestamp.astimezone(tz=datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%S%z"
    )
    datetime_str = "{0}:{1}".format(datetime_str[:-2], datetime_str[-2:])
    return datetime_str


def _write(output, val: DataType | bytes):
    if isinstance(val, str):
        output.write(bytes(val, encoding=STR_ENCODING))
    elif isinstance(val, bytes):
        output.write(val)
    elif isinstance(val, DataType):
        output.write(val.tobytes())
    else:
        raise Exception("Unsupported data type " + str(type(val)))


def _write_variable_length_integer(output, val: np.uint64):
    if not isinstance(val, np.uint64):
        raise Exception("Unsupported data type " + str(type(val)))

    if val <= 127:
        _write(output, np.uint8(1))
        _write(output, np.uint8(val))
    elif val <= 4_294_967_295:
        _write(output, np.uint8(4))
        _write(output, np.uint32(val))
    else:
        _write(output, np.uint8(8))
        _write(output, np.uint64(val))


def _write_fixed_length_integer(
    output,
    val: (
        np.int8
        | np.int16
        | np.int32
        | np.int64
        | np.uint8
        | np.uint16
        | np.uint32
        | np.uint64
    ),
):
    if not isinstance(
        val,
        np.int8
        | np.int16
        | np.int32
        | np.int64
        | np.uint8
        | np.uint16
        | np.uint32
        | np.uint64,
    ):
        raise Exception("Unsupported data type " + str(type(val)))

    _write(output, np.uint8(np.dtype(val).itemsize))
    _write(output, val.tobytes())


def _write_timestamp(output, timestamp: Optional[float] = None):
    if timestamp is None:
        _write(output, np.uint8(0))
    else:
        _write(output, np.uint8(np.dtype(np.float64).itemsize))
        _write(output, np.float64(timestamp))


class XDFStreamInfo:
    xml_header: str

    _min_timestamp_s: Optional[float]
    _max_timestamp_s: Optional[float]
    _sample_count: int

    def __init__(self, stream_xml_header: str):
        self.xml_header = stream_xml_header
        self._parse_stream_xml_header(stream_xml_header)
        self._min_timestamp_s = None
        self._max_timestamp_s = None
        self._sample_count = 0

    def _parse_stream_xml_header(self, stream_xml_header: str):
        root = ET.fromstring(stream_xml_header)
        name_str = root.findtext("name")
        channel_format_str = root.findtext("channel_format")
        source_id_str = root.findtext("source_id")

        if name_str is None:
            raise Exception("Stream name is required.")
        if channel_format_str is None:
            raise Exception("Channel format is required.")

        self._source_id = source_id_str if source_id_str else ""
        self._name = name_str
        self._channel_format = channel_format_str

    def __hash__(self):
        return hash((self._source_id, self._name, self._channel_format))

    def __eq__(self, other):
        if not isinstance(other, XDFStreamInfo):
            return False
        return (
            self._source_id == other._source_id
            and self._name == other._name
            and self._channel_format == other._channel_format
        )


class XDFWriter:
    def __init__(self, filepath: str, start_time: datetime.datetime):
        self.output = open(filepath, "wb")
        self.next_stream_id = 1  # LSL stream id always starts from 1
        self.stream_info_to_id: Dict[XDFStreamInfo, int] = {}
        self.id_to_stream_info: Dict[int, XDFStreamInfo] = {}
        self._write_file_header("1.0", start_time)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self._write_stream_footers()
        self.output.close()

    def get_or_create_stream(self, stream_xml_header: str) -> int:
        stream_info = XDFStreamInfo(stream_xml_header)

        if stream_info in self.stream_info_to_id:
            return self.stream_info_to_id[stream_info]

        stream_id = self.next_stream_id
        self.stream_info_to_id[stream_info] = stream_id
        self.id_to_stream_info[stream_id] = stream_info
        self.next_stream_id += 1

        self._write_stream_xml_header(
            stream_xml_header,
            stream_id=stream_id,
        )
        return stream_id

    def write_stream_sample(
        self,
        stream_id: int,
        sample: Any,
        timestamp_s: float,
    ):
        stream_info = self.id_to_stream_info[stream_id]

        fmt = formats[stream_info._channel_format]

        self._write_stream_sample_chunk(
            np.array([sample], dtype=fmt),
            [timestamp_s],
            stream_info._channel_format,
            np.uint32(stream_id),
        )
        stream_info._min_timestamp_s = (
            min(stream_info._min_timestamp_s, timestamp_s)
            if stream_info._min_timestamp_s
            else timestamp_s
        )
        stream_info._max_timestamp_s = (
            max(stream_info._max_timestamp_s, timestamp_s)
            if stream_info._max_timestamp_s
            else timestamp_s
        )
        stream_info._sample_count += 1

    def _write_file_header(self, version: str, start_time: datetime.datetime):
        datetime_str = _format_timestamp(start_time)
        self.output.write(b"XDF:")
        info_element = ET.Element("info")
        version_element = ET.SubElement(info_element, "version")
        datetime_element = ET.SubElement(info_element, "datetime")
        version_element.text = version
        datetime_element.text = datetime_str
        xml_str = ET.tostring(
            info_element, xml_declaration=True, encoding=STR_ENCODING
        )
        self._write_chunk(ChunkTag.FILE_HEADER, xml_str)

    def _write_chunk(
        self,
        chunk_tag: ChunkTag,
        content: bytes,
        stream_id: np.uint32 = None,
    ):
        if not isinstance(content, bytes):
            raise Exception("Content should be bytes.")

        length = np.dtype(np.uint16).itemsize + len(content)

        if stream_id is not None and stream_id != 0:
            length += np.dtype(np.uint32).itemsize

        _write_variable_length_integer(self.output, np.uint64(length))
        _write(self.output, np.uint16(chunk_tag.value))

        if stream_id is not None and stream_id != 0:
            _write(self.output, np.uint32(stream_id))

        _write(self.output, content)

    def _write_stream_xml_header(
        self, xml_header: str | bytes, stream_id: Optional[int] = None
    ):
        if isinstance(xml_header, str):
            xml_header = bytes(xml_header, encoding=STR_ENCODING)

        self._write_chunk(
            ChunkTag.STREAM_HEADER,
            xml_header,
            None if stream_id is None else np.uint32(stream_id),
        )

    def _write_stream_footers(self):
        for stream_id, stream_info in self.id_to_stream_info.items():
            self._write_stream_footer(
                stream_info._min_timestamp_s,
                stream_info._max_timestamp_s,
                stream_info._sample_count,
                stream_id=np.uint32(stream_id),
            )

    def _write_stream_footer(
        self,
        first_timestamp: float,
        last_timestamp: float,
        sample_count: int,
        stream_id: np.uint32 = None,
    ):
        first_timestamp = np.float64(first_timestamp)
        last_timestamp = np.float64(last_timestamp)
        sample_count = np.uint64(sample_count)
        info_element = ET.Element("info")
        first_timestamp_element = ET.SubElement(
            info_element, "first_timestamp"
        )
        last_timestamp_element = ET.SubElement(info_element, "last_timestamp")
        sample_count_element = ET.SubElement(info_element, "sample_count")
        first_timestamp_element.text = str(first_timestamp)
        last_timestamp_element.text = str(last_timestamp)
        sample_count_element.text = str(sample_count)

        xml_str = ET.tostring(
            info_element, xml_declaration=True, encoding=STR_ENCODING
        )
        self._write_chunk(
            ChunkTag.STREAM_FOOTER,
            xml_str,
            None if stream_id is None else np.uint32(stream_id),
        )

    def _write_stream_sample_chunk(
        self,
        chunk: np.ndarray,
        timestamps: list[float],
        channel_format: str,
        stream_id: np.uint32 = None,
    ):
        if channel_format not in formats:
            raise Exception(
                "Unsupported channel format '{}'".format(channel_format)
            )

        fmt = formats[channel_format]
        chunk = np.array(chunk, dtype=fmt)
        timestamps = np.array(timestamps, dtype=np.float64)

        tmp_output = BytesIO()
        _write_fixed_length_integer(tmp_output, np.uint32(len(chunk)))

        for i in range(len(chunk)):
            sample = chunk[i]
            timestamp = timestamps[i]
            _write_timestamp(tmp_output, timestamp)

            if sample.ndim == 0:
                if isinstance(sample, str):
                    str_bytes = bytes(sample, STR_ENCODING)
                    _write_variable_length_integer(
                        tmp_output, np.uint64(len(str_bytes))
                    )
                    _write(tmp_output, str_bytes)
                elif isinstance(sample, DataType):
                    _write(tmp_output, sample)
                else:
                    raise Exception(
                        "Unsupported data type " + str(type(sample))
                    )
            else:
                for channel in sample:
                    if isinstance(channel, str):
                        str_bytes = bytes(channel, STR_ENCODING)
                        _write_variable_length_integer(
                            tmp_output, np.uint64(len(str_bytes))
                        )
                        _write(tmp_output, str_bytes)
                    elif isinstance(channel, DataType):
                        _write(tmp_output, channel)
                    else:
                        raise Exception(
                            "Unsupported data type " + str(type(channel))
                        )

        self._write_chunk(
            ChunkTag.SAMPLES,
            tmp_output.getvalue(),
            None if stream_id is None else np.uint32(stream_id),
        )
