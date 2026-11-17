from datetime import datetime, UTC
from enum import Enum
from typing import NamedTuple

from iot_platform.domain.models.sensor_reading import SensorReading


class CreateObj(Enum):
    test_1 = SensorReading(
        name='temp_sensor',
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC))

    test2 = [SensorReading(
        name='temp_sensor',
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)),
        SensorReading(
            name='temp_sensor',
            device_id="TEMP-001",
            metric="temperature",
            value=23.5,
            unit="C",
            timestamp=datetime.now(UTC),
    )]
