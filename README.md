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

Download the latest release or clone the repository.

### Usage

Use the CLI to load and convert your records

```
python cli.py input_file output_dir --csv --xdf --descriptors [DESCRIPTORS ...]
```

* **input_file**: Input PLUME record file (.plm) to be converted.
* **output_dir**: Output directory where all generated files will be saved. Directory will be created if it does not
  exist.
* **--csv**: Convert to CSV with optional filters.
* **--xdf**: Convert markers and physiological signals to XDF .
* **-descriptors**: Descriptor name used for filtering which samples to output as CSV files. Short name will
  automatically be preprended (eg. TransformUpdate -> plume.sample.unity.TransformUpdate).

## Customization

If you have customized your PLUME Record as
instructed <a href="https://github.com/liris-xr/PLUME-Recorder?tab=readme-ov-file#customisation">here</a>, import your
generated protos for Python in the samples folder: `PLUME-Python/plume/samples`.

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