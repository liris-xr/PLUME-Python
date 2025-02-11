from enum import Enum
from dataclasses import dataclass
from uuid import UUID

from typing import Union, List

class StreamChannelFormat(Enum):
    UNDEFINED = 0
    DOUBLE64 = 1
    FLOAT32 = 2
    INT8 = 3
    INT16 = 4
    INT32 = 5
    INT64 = 6
    STRING = 7

    @staticmethod
    def from_string(channel_format_str: str):
        if channel_format_str == "double64":
            return StreamChannelFormat.DOUBLE64
        elif channel_format_str == "float32":
            return StreamChannelFormat.FLOAT32
        elif channel_format_str == "int8":
            return StreamChannelFormat.INT8
        elif channel_format_str == "int16":
            return StreamChannelFormat.INT16
        elif channel_format_str == "int32":
            return StreamChannelFormat.INT32
        elif channel_format_str == "int64":
            return StreamChannelFormat.INT64
        elif channel_format_str == "string":
            return StreamChannelFormat.STRING
        else:
            return StreamChannelFormat.UNDEFINED
        
    def to_string(self):
        if self == StreamChannelFormat.DOUBLE64:
            return "double64"
        elif self == StreamChannelFormat.FLOAT32:
            return "float32"
        elif self == StreamChannelFormat.INT8:
            return "int8"
        elif self == StreamChannelFormat.INT16:
            return "int16"
        elif self == StreamChannelFormat.INT32:
            return "int32"
        elif self == StreamChannelFormat.INT64:
            return "int64"
        elif self == StreamChannelFormat.STRING:
            return "string"
        else:
            return "undefined"

@dataclass(frozen=True)
class LslStreamInfo:
    name: str
    type: str
    channel_count: int
    nominal_sample_rate: float
    channel_format: StreamChannelFormat
    source_id: str
    created_at: float
    uid: UUID
    version: str

    hostname: str
    v4address: str
    v4data_port: int
    v4service_port: int

    v6address: str
    v6data_port: int
    v6service_port: int

    desc: str

    raw_xml_header: str

    def __repr__(self):
        return f"LslStreamInfo(name={self.name}, type={self.type}, channel_count={self.channel_count}, nominal_sample_rate={self.nominal_sample_rate:.2f}, channel_format={self.channel_format}, source_id={self.source_id}, created_at={self.created_at}, uid={self.uid}, version={self.version}, hostname={self.hostname}, v4address={self.v4address}, v4data_port={self.v4data_port}, v4service_port={self.v4service_port}, v6address={self.v6address}, v6data_port={self.v6data_port}, v6service_port={self.v6service_port}, desc={self.desc})"

@dataclass(frozen=True)
class LslStreamSample:
    stream_info: LslStreamInfo
    time_ns: int
    values: List[Union[float, int, str]]

    @property
    def time_s(self):
        return self.time_ns / 1e9

    def __repr__(self):
        return f"LslStreamSample(stream_name={self.stream_info.name}, values={self.values}, time_ns={self.time_ns})"
