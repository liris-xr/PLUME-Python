from record import Record
import pandas as pd
from google.protobuf.json_format import MessageToDict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf.descriptor import Descriptor
from tqdm import tqdm
from typing import List, Optional

# Required to add all DESCRIPTORS into the default descriptor pool
from samples import *

def to_dataframes(record: Record, descriptors: List[Descriptor] = None):

    dataframes = {}
    desc_pool = _descriptor_pool.Default()

    if descriptors is None or len(descriptors) == 0:
        samples = record.samples
    else:
        samples = record.GetSamplesByDescriptors(descriptors)

    pbar = tqdm(miniters=1)
    pbar.reset(total=len(samples))
    pbar.set_description("Grouping sample by type.", refresh=True)

    groups = {}
    for s in samples:
        if s.payload.DESCRIPTOR not in groups:
            groups[s.payload.DESCRIPTOR] = []
        groups[s.payload.DESCRIPTOR].append(s)
        pbar.update(1)

    for (group_key, group_samples) in groups.items():
        pbar.reset(total=len(group_samples))
        pbar.set_description(f"Converting '{group_key.full_name}' samples", refresh=True)

        sample_dicts = []

        for sample in group_samples:
            sample_header_dict = MessageToDict(sample.header, including_default_value_fields=True, descriptor_pool=desc_pool)
            sample_payload_dict = MessageToDict(sample.payload, including_default_value_fields=True, descriptor_pool=desc_pool)
            sample_dicts.append(sample_header_dict | sample_payload_dict)
            pbar.update(1)

        pbar.set_description(f"Generating column names for '{group_key.full_name}' samples.", refresh=True)
        dataframes[group_key] = pd.json_normalize(sample_dicts)

    pbar.close()

    return dataframes