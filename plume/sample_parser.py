from plume.parser_utils import unpack_any
import warnings

import plume.sample

def parse_sample(sample):
    unpacked_payload, success = unpack_any(sample.payload)
    if not success:
        return None, False
    timestamp = sample.timestamp if sample.HasField('timestamp') else None
    sample = plume.sample.Sample(timestamp, unpacked_payload)
    return sample, True

def parse_samples(samples, filter_descriptors=None):
    unpacked_samples = []

    if filter_descriptors is not None:
        filter_descriptors_full_name = [descriptor.full_name for descriptor in filter_descriptors]

    for sample in samples:

        type_url = sample.payload.type_url
        short_type_url = type_url[type_url.find('/')+1:]
        
        if filter_descriptors is not None and short_type_url not in filter_descriptors_full_name:
            continue
        unpacked_sample, success = parse_sample(sample)

        if success:
            unpacked_samples.append(unpacked_sample)
        else:
            warnings.warn(f"Failed to parse data of type {type_url}. Skipping.")

    return unpacked_samples