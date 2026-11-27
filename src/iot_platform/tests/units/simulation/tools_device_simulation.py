from enum import Enum
from typing import NamedTuple


class GenerateSimulations(NamedTuple):
    device_id: str
    name: str
    is_active: bool
    count: int = 1


class GenerateParameters(Enum):
    test_1 = GenerateSimulations(device_id="TEMP-001",name="Living Room",is_active=True, count = 100)