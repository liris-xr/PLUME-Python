from plume.sample.unity.frame_pb2 import Frame as FrameSample
from plume_python.proxy.unity.frame import Frame
from plume.sample import get_message_class_from_type_name
from plume_python.decoder.registry import get_frame_data_decoder
from google.protobuf.message import Message

from warnings import warn

def decode_frame_data(frame: Frame, parsed_payload: Message):
    try:
        decoder = get_frame_data_decoder(type(parsed_payload))
    except:
        warn(
            f"Failed to get decoder for {parsed_payload.DESCRIPTOR.full_name}"
        )
        return

    try:
        decoder.decode(frame, parsed_payload)
    except:
        warn(
            f"Failed to decode {type(parsed_payload)}"
        )
        return

def decode_frame(frame: Frame, frame_sample: FrameSample):
    
    for data in frame_sample.data:
        try:
            cls = get_message_class_from_type_name(data.TypeName())
            parsed_payload = cls()
            success = data.Unpack(parsed_payload)
            if not success:
                warn(
                    f"Failed to unpack payload with type name {data.TypeName()}"
                )
                continue

            decode_frame_data(frame, parsed_payload)
        except:
            warn(
                f"Failed to decode payload with type name {data.TypeName()}"
            )

