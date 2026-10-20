# Changelog

All notable changes to the MeasureMap schemas are documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the schemas follow the versioning policy described in the [README](README.md#versioning).

## [Unreleased]

### Fixed

- Every Measure of a MeasureMap and every entry of `next` is now validated. Previously, `items` was given in tuple form, so only the first element was checked. MeasureMaps that were wrongly accepted are now rejected.

## [1.0.0] - 2026-10-20

First versioned release. Apart from their `$id`s, the schemas are identical to the unversioned ones previously on `main`.

### Added

- `measure.schema.json`, describing a single Measure with the fields `ID`, `count`, `qstamp`, `number`, `name`, `time_signature`, `nominal_length`, `actual_length`, `start_repeat`, `end_repeat`, and `next`.
- `measuremap.schema.json`, describing a MeasureMap as an array of at least two Measures.
- Fixed, versioned `$id`s under `https://measure-map.github.io/specification/schema/1.0.0/`.
- MIT license.

[Unreleased]: https://github.com/measure-map/specification/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/measure-map/specification/releases/tag/v1.0.0
