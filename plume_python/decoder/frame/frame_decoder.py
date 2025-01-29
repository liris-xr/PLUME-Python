from plume.sample.unity.frame_pb2 import Frame as FrameSample
from plume_python.reader.sample import Sample
from plume_python.proxy.unity.frame import Frame
from plume_python.utils.samples import get_message_class_from_type_name
from plume_python.decoder.frame.frame_data_decoder_registry import (
    get_frame_data_decoder,
)
from google.protobuf.message import Message
from warnings import warn


def decode_frame(frame: Frame, frame_sample: Sample[FrameSample]):

    frame._frame_number = frame_sample.payload.frame_number
    frame._time_ns = frame_sample.time_ns

    for data in frame_sample.payload.data:

        cls = get_message_class_from_type_name(data.TypeName())

        if cls is None:
            warn(f"Failed to get data payload class for type {data.TypeName()}")
            continue

        parsed_payload: Message = cls()
        success = data.Unpack(parsed_payload)
        if not success:
            warn(f"Failed to unpack payload with type {data.TypeName()}")
            continue

        try:
            frame_data_decoder = get_frame_data_decoder(type(parsed_payload))
        except:
            warn(
                f"Failed to get decoder for {parsed_payload.DESCRIPTOR.full_name}. Skipping."
            )
            continue

        frame_data_decoder.decode(frame, parsed_payload)
