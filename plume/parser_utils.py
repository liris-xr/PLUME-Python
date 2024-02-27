from google.protobuf import descriptor_pool
from google.protobuf.message_factory import GetMessageClass
from google.protobuf import any_pb2

# Required to add all DESCRIPTORS into the default descriptor pool
from plume.samples import *
__descriptor_pool = descriptor_pool.Default()

def unpack_any(payload):
    descriptor = __descriptor_pool.FindMessageTypeByName(payload.TypeName())
    unpacked_any = GetMessageClass(descriptor)()
    success = payload.Unpack(unpacked_any)
    return unpacked_any, success
