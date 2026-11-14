from dataclasses import dataclass
from datetime import datetime, timezone


class IsNotValidParameter(Exception):
    pass


@dataclass
class SensorReading:
    device_id : str
    metric: str
    value: float
    unit: str
    timestamp: datetime

    def __post_init__(self):
        if not self.device_id:
            raise IsNotValidParameter(f"Empty parameter: {self.device_id}")
        if not self.metric:
            raise IsNotValidParameter(f"Empty parameter: {self.metric}")
        if not self.value:
            raise IsNotValidParameter(f"Empty parameter: {self.value}")
        if not self.unit:
            raise IsNotValidParameter(f"Empty parameter: {self.unit}")
        if not self.timestamp:
            raise IsNotValidParameter(f"Empty parameter: {self.timestamp}")
        if not isinstance(self.value,(float or int)):
            raise IsNotValidParameter(f"Not correctly param: {self.value}, type: {type(self.value)}")

if __name__ == "__main__":
    reading = SensorReading(
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(timezone.utc)
    )
    pass
