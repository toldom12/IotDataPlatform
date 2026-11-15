from dataclasses import dataclass
from datetime import UTC, datetime


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


class TelemetryBuffer:
    def __init__(self):
        self.__measurements : dict = {}

    def add_measurements(self, meas: SensorReading or [SensorReading]) -> None:
        if isinstance(meas, object):
            meas = [meas]
        for index, obj in enumerate(meas):
            self.__measurements[f'{obj.device_id}'] = [obj.metric, obj.value, obj.unit, obj.timestamp]

    @property
    def get_measurements(self) -> dict:
        return self.__measurements

    def filter_by_device_id(self,device_id : int or list) -> dict:
        if isinstance(device_id, int):
             return self.__measurements[f'{device_id}']
        else:
            device_id_dict  : dict = {}
            for expected_device in device_id:
                key = f'{expected_device}'
                if key in self.__measurements:
                    device_id_dict[key] = self.__measurements[key]
                pass
            return device_id_dict











if __name__ == "__main__":
    reading = SensorReading(
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )
    reading1 = SensorReading(
        device_id="TEMP-002",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )
    a = TelemetryBuffer()
    a.add_measurements(meas=reading)
    a.add_measurements(meas=reading1)
    results = a.filter_by_device_id(device_id=['TEMP-001','TEMP-002'])
    pass
