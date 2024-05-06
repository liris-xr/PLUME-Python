# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.12]

### Changed

- Updated the required version of Python to >=3.7.1

### Fixed

- Fixed a bug where extracting samples by time range would throw an exception if the record contained timeless samples.