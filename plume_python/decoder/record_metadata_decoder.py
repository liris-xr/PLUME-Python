from plume_python.proxy.record_metadata import RecordMetadata, RecorderVersion

from plume_python.decoder.sample_stream_reader import SampleStreamReader
from plume.sample.record_pb2 import RecordMetadata as RecordMetadataSample

import datetime


def decode_record_metadata(filepath: str) -> RecordMetadata:

    with open(filepath, "rb") as f:
        with SampleStreamReader(f) as reader:
            metadata_sample, _ = reader.parse_next(RecordMetadataSample)

            if metadata_sample is None:
                raise ValueError("Record metadata not found")

            return RecordMetadata(
                recorder_version=RecorderVersion(
                    name=metadata_sample.recorder_version.name,
                    major=metadata_sample.recorder_version.major,
                    minor=metadata_sample.recorder_version.minor,
                    patch=metadata_sample.recorder_version.patch,
                ),
                start_time=metadata_sample.start_time.ToDatetime(
                    tzinfo=datetime.timezone.utc
                ),
                name=metadata_sample.name,
                extra_metadata=metadata_sample.extra_metadata,
            )
