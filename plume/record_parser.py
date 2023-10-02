import gzip
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.message_factory import GetMessageClass
from tqdm import tqdm

# Required to add all DESCRIPTORS into the default descriptor pool
from samples import *
from samples import packed_sample_pb2

from sample import Sample
from record import Record

def _parse_from_delimited(msg, buf, buf_pos):
    msg_len, new_pos = _DecodeVarint32(buf, buf_pos)
    msg_buf = buf[new_pos:new_pos+msg_len]
    new_pos += msg_len
    msg.ParseFromString(msg_buf)
    return new_pos

def _read_next_sample(buf, buf_pos):
    sample = packed_sample_pb2.PackedSample()
    new_buf_pos = _parse_from_delimited(sample, buf, buf_pos)
    return sample, new_buf_pos

def _parse_next_sample(buf, buf_pos):
    sample, buf_pos = _read_next_sample(buf, buf_pos)
    try:
        payload_descriptor = _descriptor_pool.Default().FindMessageTypeByName(sample.payload.TypeName())
        unpacked_payload = GetMessageClass(payload_descriptor)()
        sample.payload.Unpack(unpacked_payload)
        unpacked_sample = Sample(header=sample.header, payload=unpacked_payload)
    except:
        print(f"Failed to parse sample with payload of type '{sample.payload.TypeName()}'")
    return unpacked_sample, buf_pos

def parse_record(filepath : str):

    record = Record(filepath)
    record.samples = []

    with gzip.open(filepath, "rb") as f:
        buf = f.read()
        buf_pos = 0

        record.record_header, buf_pos = _parse_next_sample(buf, buf_pos)

        with tqdm(total=1, desc="Parsing samples") as pbar:
            while buf_pos < len(buf):
                last_buf_pos = buf_pos
                sample, buf_pos = _parse_next_sample(buf, buf_pos)
                if sample is not None:
                    record.samples.append(sample)
                pbar.update((buf_pos - last_buf_pos) / len(buf))

    return record
