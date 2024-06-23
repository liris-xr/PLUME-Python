# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.14]

### Added

- Added ruff to enforce proper code formatting

### Changed

- Updated pandas dependency to >=2.2.2

- Updated CI/CD pipeline to separate development and release workflows

## [0.1.13]

### Changed

- Updated README

## [0.1.12]

### Added

- Added `get_timeless_samples` method to `Record` class to extract samples without timestamps.

### Changed

- Updated the required version of Python to >=3.10

### Fixed

- Fixed a bug where extracting samples by time range would throw an exception if the record contained timeless samples.
