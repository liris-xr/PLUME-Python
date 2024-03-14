import xml.etree.ElementTree as ET
from enum import Enum
from io import BufferedWriter, BytesIO

import numpy as np

BYTE_ORDER = "big"
STR_ENCODING = "utf-8"

formats = dict(
    double64=np.float64,
    float32=np.float32,
    string=str,
    int32=np.int32,
    int16=np.int16,
    int8=np.int8,
    int64=np.int64,
)

DataType = np.int8 | np.int16 | np.int32 | np.int64 | np.uint8 | np.uint16 | np.uint32 | np.uint64 | np.float32 | np.float64 | str


class ChunkTag(Enum):
    FILE_HEADER = 1
    STREAM_HEADER = 2
    SAMPLES = 3
    CLOCK_OFFSET = 4
    BOUNDARY = 5
    STREAM_FOOTER = 6
    UNDEFINED = 0


def write_file_header(output: BufferedWriter, version: str, datetime: str):
    output.write(b'XDF:')
    info_element = ET.Element("info")
    version_element = ET.SubElement(info_element, "version")
    datetime_element = ET.SubElement(info_element, "datetime")
    version_element.text = version
    datetime_element.text = datetime
    xml_str = ET.tostring(
        info_element, xml_declaration=True, encoding=STR_ENCODING)
    write_chunk(output, ChunkTag.FILE_HEADER, xml_str)


def write_chunk(output: BufferedWriter, chunk_tag: ChunkTag, content: bytes, stream_id: np.uint32 = None):
    if not isinstance(content, bytes):
        raise Exception("Content should be bytes.")

    length = np.dtype(np.uint16).itemsize + len(content)

    if stream_id is not None and stream_id != 0:
        length += np.dtype(np.uint32).itemsize

    write_variable_length_integer(output, np.uint64(length))
    write(output, np.uint16(chunk_tag.value))

    if stream_id is not None and stream_id != 0:
        write(output, None if stream_id is None else np.uint32(stream_id))

    write(output, content)


def write_stream_header(output: BufferedWriter, xml_header: str | bytes, stream_id: np.uint32 = None):
    if isinstance(xml_header, str):
        xml_header = bytes(xml_header, encoding=STR_ENCODING)

    write_chunk(output, ChunkTag.STREAM_HEADER, xml_header, None if stream_id is None else np.uint32(stream_id))


def write_stream_footer(output: BufferedWriter, first_timestamp: float, last_timestamp: float,
                        sample_count: int, stream_id: np.uint32 = None):
    first_timestamp = np.float64(first_timestamp)
    last_timestamp = np.float64(last_timestamp)
    sample_count = np.uint64(sample_count)
    info_element = ET.Element("info")
    first_timestamp_element = ET.SubElement(info_element, "first_timestamp")
    last_timestamp_element = ET.SubElement(info_element, "last_timestamp")
    sample_count_element = ET.SubElement(info_element, "sample_count")
    first_timestamp_element.text = str(first_timestamp)
    last_timestamp_element.text = str(last_timestamp)
    sample_count_element.text = str(sample_count)

    xml_str = ET.tostring(
        info_element, xml_declaration=True, encoding=STR_ENCODING)
    write_chunk(output, ChunkTag.STREAM_FOOTER, xml_str, None if stream_id is None else np.uint32(stream_id))


def write_stream_sample(output: BufferedWriter, sample: np.ndarray, timestamp: float, channel_format: str,
                        stream_id: np.uint32 = None):
    if channel_format not in formats:
        raise Exception("Unsupported channel format '{}'".format(channel_format))

    fmt = formats[channel_format]
    write_stream_sample_chunk(output, np.array([sample], dtype=fmt), np.array([timestamp], dtype=np.float64),
                              channel_format, None if stream_id is None else np.uint32(stream_id))


def write_stream_sample_chunk(output: BufferedWriter, chunk: np.ndarray, timestamps: np.ndarray, channel_format: str,
                              stream_id: np.uint32 = None):
    if channel_format not in formats:
        raise Exception("Unsupported channel format '{}'".format(channel_format))

    fmt = formats[channel_format]
    chunk = np.array(chunk, dtype=fmt)
    timestamps = np.array(timestamps, dtype=np.float64)

    tmp_output = BytesIO()
    write_fixed_length_integer(tmp_output, np.uint32(len(chunk)))

    for i in range(len(chunk)):
        sample = chunk[i]
        timestamp = timestamps[i]
        write_timestamp(tmp_output, timestamp)

        if sample.ndim == 0:
            if isinstance(sample, str):
                str_bytes = bytes(sample, STR_ENCODING)
                write_variable_length_integer(tmp_output, np.uint64(len(str_bytes)))
                write(tmp_output, str_bytes)
            elif isinstance(sample, DataType):
                write(tmp_output, sample)
            else:
                raise Exception("Unsupported data type " + str(type(sample)))
        else:
            for channel in sample:
                if isinstance(channel, str):
                    str_bytes = bytes(channel, STR_ENCODING)
                    write_variable_length_integer(tmp_output, np.uint64(len(str_bytes)))
                    write(tmp_output, str_bytes)
                elif isinstance(channel, DataType):
                    write(tmp_output, channel)
                else:
                    raise Exception("Unsupported data type " + str(type(channel)))

    write_chunk(output, ChunkTag.SAMPLES, tmp_output.getvalue(), None if stream_id is None else np.uint32(stream_id))


def write_timestamp(output: BufferedWriter, timestamp: np.float64 = None):
    if timestamp is None:
        write(output, np.uint8(0))
    else:
        write(output, np.uint8(np.dtype(np.float64).itemsize))
        write(output, np.float64(timestamp))


def write_variable_length_integer(output: BufferedWriter, val: np.uint64):
    if not isinstance(val, np.uint64):
        raise Exception("Unsupported data type " + str(type(val)))

    if val <= 127:  # byte max value
        write(output, np.uint8(1))
        write(output, np.uint8(val))
    elif val <= 4_294_967_295:  # uint32 max value
        write(output, np.uint8(4))
        write(output, np.uint32(val))
    else:  # val <= 18_446_744_073_709_551_615: # uint64 max value
        write(output, np.uint8(8))
        write(output, np.uint64(val))


def write_fixed_length_integer(output: BufferedWriter,
                               val: np.int8 | np.int16 | np.int32 | np.int64 | np.uint8 | np.uint16 | np.uint32 | np.uint64):
    if not isinstance(val, np.int8 | np.int16 | np.int32 | np.int64 | np.uint8 | np.uint16 | np.uint32 | np.uint64):
        raise Exception("Unsupported data type " + str(type(val)))

    write(output, np.uint8(np.dtype(val).itemsize))
    write(output, val.tobytes())


def write(output: BufferedWriter, val: DataType | bytes):
    if isinstance(val, str):
        output.write(bytes(val, encoding=STR_ENCODING))
    elif isinstance(val, bytes):
        output.write(val)
    elif isinstance(val, DataType):
        output.write(val.tobytes())
    else:
        raise Exception("Unsupported data type " + str(type(val)))
