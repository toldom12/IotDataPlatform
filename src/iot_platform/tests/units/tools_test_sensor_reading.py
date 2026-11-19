from datetime import datetime, UTC
from enum import Enum
from typing import NamedTuple

from iot_platform.domain.models.sensor_reading import SensorReading


class CreateObj(NamedTuple):
    name: str
    device_id: str
    metric: str
    value: float
    unit: str
    timestamp: datetime



class ObjValidation(Enum):
    test_1 = CreateObj(
        name='',
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )

    test_2 = CreateObj(
        name='temp_sensor',
        device_id="",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )

    test_3 = CreateObj(
        name='temp_sensor',
        device_id="",
        metric="temperature",
        value="23.5",
        unit="C",
        timestamp=datetime.now(UTC)
    )
