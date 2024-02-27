import argparse

from re import sub
from os import makedirs, path
from plume.sample_parser import parse_record
from dataframe_exporter import to_dataframes
from xdf_exporter import to_xdf
from typing import List

import google.protobuf.descriptor_pool as descriptor_pool
from google.protobuf.descriptor import Descriptor
from samples import *

def _snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()


def _descriptors_from_names(filters: List[str]):
    descriptors = []

    for filter in filters:
        descriptor = None

        derivatives = [filter,
                               f"plume.{filter}",
                               f"plume.sample.{filter}",
                               f"plume.sample.{filter}",
                               f"plume.sample.lsl.{filter}",
                               f"plume.sample.unity.{filter}",
                               f"plume.sample.unity.ui.{filter}",
                               f"plume.sample.common.{filter}"]
                
        for derivative in derivatives:
            try:
                descriptor = descriptor_pool.Default().FindMessageTypeByName(derivative)
                if descriptor is not None:
                    descriptors.append(descriptor)
                    break
            except:
                pass

        if descriptor is None:
            raise Exception(f"Sample descriptor not found for '{filter}'.")
    
    return descriptors

def plm_to_csv(record, output_dir, descriptors: List[Descriptor] = None):

    file_basename = path.splitext(path.basename(record.filepath))[0]

    if descriptors is None or len(descriptors) == 0:
        dataframes = to_dataframes(record)
    else:
        dataframes = to_dataframes(record, descriptors)

    makedirs(output_dir, exist_ok=True)

    for (descriptor, df) in dataframes.items():
        output_file = path.join(output_dir, file_basename + "_" + _snake_case(descriptor.name) + ".csv")
        with open(output_file, "w") as csv_file:
            df.to_csv(csv_file, index=False, na_rep='N/A', lineterminator='\n')

def plm_to_xdf(record, output_dir):

    file_basename = path.splitext(path.basename(record.filepath))[0]
    output_file = path.join(output_dir, file_basename + ".xdf")

    with open(output_file, "wb") as xdf_file:
        to_xdf(xdf_file, record)

def main():
    parser = argparse.ArgumentParser(description="Convert PLM to CSV or XDF")
    parser.add_argument("input_file", help="Input PLUME file to be converted.")
    parser.add_argument("output_dir", help="Output directory where all files will be saved. The directory is created if it does not exists.")
    parser.add_argument("--csv", "-c", action="store_true", help="Convert to CSV with optional filters")
    parser.add_argument("--xdf", "-x", action="store_true", help="Convert to XDF")
    parser.add_argument("--descriptors", "-d", nargs="*", help="Descriptor name used for filtering which samples to output as CSV files. Short name will automatically be preprended (eg. TransformUpdatePosition -> plume.sample.unity.TransformUpdatePosition)")

    args = parser.parse_args()

    if not args.csv and not args.xdf:
        print("Please specify at least one of --csv or --xdf")
    else:
        record = parse_record(args.input_file)

        if args.csv:
            descriptors = _descriptors_from_names(args.descriptors)
            plm_to_csv(record, args.output_dir, descriptors)
            print(f"PLUME file '{args.input_file}' converted to CSVs and saved in '{args.output_dir}'")
        
        if args.xdf:
            plm_to_xdf(record, args.output_dir)
            print(f"PLUME file '{args.input_file}' converted to XDF and saved in '{args.output_dir}'")

if __name__ == "__main__":
    main()
