
from plume.parser_utils import unpack_any

import warnings

def parse_frame_data(frame_sample, filter_descriptors=None):
    unpacked_data = []

    if filter_descriptors is not None:
        filter_descriptors_full_name = [descriptor.full_name for descriptor in filter_descriptors]
    
    for data in frame_sample.payload.data:

        type_url = data.type_url
        short_type_url = type_url[type_url.find('/')+1:]

        if filter_descriptors is not None and short_type_url not in filter_descriptors_full_name:
            continue

        d, success = unpack_any(data)

        if success:
            unpacked_data.append(d)
        else:
            warnings.warn(f"Failed to parse data of type {data.type_url}. Skipping.")

    return unpacked_data