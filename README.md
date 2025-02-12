<div align="center">
    <a href="https://github.com/liris-xr/PLUME">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="docs/imgs/plume_python_dark.png">
            <source media="(prefers-color-scheme: light)" srcset="docs/imgs/plume_python_light.png">
            <img alt="PLUME banner." src="docs/imgs/plume_python_light.png" width="350">
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

Please refer to the [getting started guide](https://liris-xr.github.io/PLUME/get-started/) for information on getting started with PLUME-Python.


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
