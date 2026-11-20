from abc import ABC, abstractmethod
from typing import Any

from iot_platform.domain.models.sensor_reading import SensorReading


class Device(ABC):
    def __init__(self,
                 device_id: str,
                 name: str,
                 is_active: bool):
        self.device_id = device_id
        self.name = name
        self.is_active = is_active
        if not isinstance(self.name, str):
            raise TypeError(f' Name shpuld be a str {type(self.name)}')

        if not isinstance(self.device_id, str):
            raise TypeError(f' Name shpuld be a str {type(self.device_id)}')


    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        if isinstance(value, bool):
            self._is_active = value
        else:
            raise TypeError("Is active must be a boolean")

    def generate_reading(self) -> None | SensorReading:
        if not self.is_active:
            raise RuntimeError("Cannot generate reading: device is inactive")
        return self._generate_reading()

    @abstractmethod
    def _generate_reading(self) -> SensorReading | Any:
        pass


if __name__ =="__main__":
    pass





