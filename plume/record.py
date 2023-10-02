from samples.record_header_pb2 import RecordHeader
from google.protobuf.descriptor import Descriptor

from typing import List, Optional

class Record:

    def __init__(self, filepath : str, record_header: RecordHeader = None, samples: list = []):
        self.filepath = filepath
        self.record_header = record_header
        self.samples = samples

    def GetSamplesByDescriptor(self, descriptor: Descriptor):
        if descriptor is None:
            return self.samples
        
        return [s for s in self.samples if s.payload.DESCRIPTOR.full_name == descriptor.full_name]

    def GetSamplesByDescriptors(self, descriptors: List[Descriptor] = None):
        if descriptors is None:
            return self.samples
        
        filtered_samples  = []
        for descriptor in descriptors:
            filtered_samples.extend([s for s in self.samples if s.payload.DESCRIPTOR.full_name == descriptor.full_name])
        return filtered_samples