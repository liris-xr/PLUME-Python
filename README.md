<div align="center">
    <a href="https://github.com/liris-xr/PLUME">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="Resources~/Images/plume_python_dark.png">
            <source media="(prefers-color-scheme: light)" srcset="Resources~/Images/plume_python_light.png">
            <img alt="PLUME banner." src="Resources~/Images/plume_python_light.png" width="350">
        </picture>
    </a><br/><br/>
    <p>
        <a href="https://opensource.org/license/gpl-3-0"><img alt="License badge" src="https://img.shields.io/badge/license-GPLv3-blue.svg"/></a>
        <a href="https://discord.gg/c3evqEWMge"><img alt="Discord badge" src="https://img.shields.io/discord/1151165491767935107?logo=discord&logoColor=white&label=discord"/></a>
    </p>
</div>
<p align="center">
    Charles Javerliat, Sophie Villenave, Pierre Raimbaud, Guillaume Lavoué
    <br />
    <em>IEEE Conference on Virtual Reality and 3D User Interfaces (Journal Track)</em>
    <br />
    <a href="https://www.youtube.com/watch?v=_6krSw7fNqg"><strong>Video »</strong></a>&emsp;
    <a href="https://hal.science/hal-04488824"><strong>Paper »</strong></a>&emsp;
    <a href="https://liris-xr.github.io/PLUME/"><strong>Explore the docs »</strong></a>
    <br />
</p>

PLUME Python is a Python package that allows you to load and extract data from PLUME record files. The package also comes with a set of utilities to simplify the conversion of the data into more commonly used formats in data analysis like pandas dataframe or CSV files. Embedded data such as LabStreamingLayer's samples can be exported to XDF files for external use in tools such as SigViewer, EEGLAB or MoBILAB.

## Getting Started

PLUME Python can be installed directly from PyPI (requires Python >= 3.10) using the following command:

```bash
pip install plume-python
```

Basic CLI commands are available for simple operations:
```bash
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

For more advanced usage, the package can be imported in a Python script:

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

Please refer to the [getting started guide](https://liris-xr.github.io/PLUME/get-started/) for more information on getting started with PLUME.


## Documentation

The full documentation is available at [liris-xr.github.io/PLUME/](https://liris-xr.github.io/PLUME/). It includes a detailed description of the installation process, the file format specifications, the usage of the different tools, etc.

[![Button Docs]][Explore the docs]

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. You can [open an issue](https://github.com/liris-xr/PLUME-Recorder/issues) to report a bug, request a feature, or submit a pull request.

### Development setup
Use the following commands to install the package in dev mode and run tests:
```sh
# Install the package with dev dependencies
make install
# Running tests locally with pytest
make tests
```

## Contact

Discord server **(Recommended)** <a href="https://discord.gg/c3evqEWMge">
            <img alt="Discord badge" src="https://img.shields.io/discord/1151165491767935107?logo=discord&logoColor=white&label=discord"/>
        </a>

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

[Button Docs]: https://img.shields.io/badge/Explore%20the%20docs-%E2%86%92-brightgreen
[Explore the docs]: https://liris-xr.github.io/PLUME/
