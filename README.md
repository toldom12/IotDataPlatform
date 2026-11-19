# IoT Data Platform

An early-stage Python project for modeling IoT sensor readings and collecting telemetry. The repository currently contains core domain models, sensor device modules, and unit tests; ingestion services, persistence, and a runnable application entry point are not yet included.

## Requirements

- Python 3.12 or newer

## Setup

Create and activate a virtual environment, then install the project with its development dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

## Development

Run the unit tests:

```powershell
python -m pytest
```

Check code style and lint:

```powershell
ruff check .
ruff format --check .
```

## Project layout

```text
src/iot_platform/
  domain/
    devices/     Sensor device definitions
    models/      Telemetry and reading models
    enums.py     Domain enumerations
  tests/         Unit tests
  tools/         Development utilities
```

The package is configured in `pyproject.toml` and uses a `src` layout. Pytest is configured to discover tests under `tests/` and add `src/` to the import path. Development dependencies include pytest, pytest-cov, and Ruff.

## Current scope

`SensorReading` represents an individual measurement, and `TelemetryBuffer` groups readings by sensor name and device ID with basic filtering helpers. The device modules provide the beginnings of sensor-specific domain behavior. The platform is under active development, so APIs and project structure may change.
