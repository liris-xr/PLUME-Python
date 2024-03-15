<a name="readme-top"></a>
<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/liris-xr/PLUME-Python/master/Documentation%7E/Images/plume_banner_dark.png">
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/liris-xr/PLUME-Python/master/Documentation%7E/Images/plume_banner_light.png">
        <img alt="PLUME banner." src="https://raw.githubusercontent.com/liris-xr/PLUME-Python/master/Documentation%7E/Images/plume_banner_light.png">
    </picture>
    <br />
    <br />
    <p align="center">
        <strong>PLUME: Record, Replay, Analyze and Share User Behavior in 6DoF XR Experiences</strong>
        <br />
        Charles Javerliat, Sophie Villenave, Pierre Raimbaud, Guillaume Lavoué
        <br />
        <em>(Journal Track) IEEE Conference on Virtual Reality and 3D User Interfaces</em>
        <br />
        <a href="https://www.youtube.com/watch?v=_6krSw7fNqg"><strong>Video »</strong><a>
        <a href="https://hal.science/hal-04488824"><strong>Paper »</strong></a>
        <a href="https://github.com/liris-xr/PLUME/wiki/"><strong>Explore the docs »</strong></a>
        <br />
        <br />
        <a href="https://github.com/liris-xr/PLUME/issues">Report Bug</a>
        ·
        <a href="https://github.com/liris-xr/PLUME/issues">Request Feature</a>
    </p>
</div>

<img alt="PLUME Python" src="https://raw.githubusercontent.com/liris-xr/PLUME-Python/master/Documentation%7E/Images/plume_python.png">

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#about-plume-python">About PLUME Python</a></li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#prerequisites">Prerequisites</a></li>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#usage">Usage</a></li>
            </ul>
        </li>
        <li><a href="#customization">Customization</a></li>
        <li><a href="#customization">Roadmap</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#citation">Citation</a></li>
    </ol>
</details>

## About PLUME Python

The interoperability of PLUME record files allows for other language to load those files for external analysis. PLUME
Python is a module that can load record files using the Protobuf package to filter and convert the data into more
commonly used formats in data analysis like pandas dataframe or CSV files. Embedded data such as LabStreamingLayer's
samples can be exported to XDF files for external use in tools such as SigViewer, EEGLAB or MoBILAB.

## Getting Started

### Prerequisites

* Python 3.10 or later
* protobuf
* pandas

### Installation

To install the latest release, use pip:

```shell
pip install plume-python
```

### Usage

#### CLI

```shell
Usage: plume-python [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
  
Commands:
  export-csv               Export samples from the record to CSV files.
  export-world-transforms  Export world transforms of a GameObject with the given GUID to a CSV file.
  export-xdf               Export a XDF file including LSL samples and markers.
  find-guid                Find the GUID(s) of a GameObject by the given name.
  find-name                Find the name(s) of a GameObject with the given GUID in the record.
```

#### API

```python
import plume_python as plm
from plume_python.utils.dataframe import samples_to_dataframe, record_to_dataframes
from plume_python.samples.unity import transform_pb2
from plume_python.export import xdf_exporter 
from plume_python.utils.game_object import find_names_by_guid, find_first_identifier_by_name

# Load a record file
record = plm.parser.parse_record_from_file("path/to/record.plm")

# Find the name(s) of a game object by its GUID
names = find_names_by_guid(record, "4a3f40e37eaf4c0a9d5d88ac993c0ebc")

# Find the identifier (go + transform GUID) of a game object by its name
identifier = find_first_identifier_by_name(record, "MyGameObjectName")

# Get samples of a given type
transform_updates = record.get_samples_by_type(transform_pb2.TransformUpdate)

# Get samples in a given time range (in nanoseconds)
record.get_samples_in_time_range(0, 10_000)

# Get samples of a given type in a given time range (in nanoseconds)
record.get_samples_by_type_in_time_range(transform_pb2.TransformUpdate, 0, 10_000)

# Get sample absolute timestamp (in nanoseconds) since epoch
record.get_sample_timestamp_since_epoch(transform_updates[0])

# Convert samples to a pandas dataframe
transform_updates_df = samples_to_dataframe(transform_updates)

# Convert all samples to pandas dataframes
dataframes = record_to_dataframes(record)
transform_updates_df_2 = dataframes[transform_pb2.TransformUpdate]

# Export samples to a XDF file
with open("path/to/output.xdf", "wb") as xdf_file:
    xdf_exporter.export_xdf_from_record(xdf_file, record)
```

## Roadmap

See the [open issues](https://github.com/liris-xr/PLUME/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.
Don't forget to give the project a star! Thanks again!

## License

Distributed under the <a rel="license" href="https://github.com/liris-xr/PLUME-Python/blob/master/LICENSE">GPLv3
License</a>.

## Contact

Charles JAVERLIAT - charles.javerliat@gmail.com

Sophie VILLENAVE - sophie.villenave@ec-lyon.fr

## Citation

```
@article{javerliat_plume_2024,
	title = {{PLUME}: {Record}, {Replay}, {Analyze} and {Share} {User} {Behavior} in {6DoF} {XR} {Experiences}},
	url = {https://ieeexplore.ieee.org/document/10458415},
	doi = {10.1109/TVCG.2024.3372107},
	journal = {IEEE Transactions on Visualization and Computer Graphics},
	author = {Javerliat, Charles and Villenave, Sophie and Raimbaud, Pierre and Lavoué, Guillaume},
	year = {2024},
	note = {Conference Name: IEEE Transactions on Visualization and Computer Graphics},
	pages = {1--11}
}
```