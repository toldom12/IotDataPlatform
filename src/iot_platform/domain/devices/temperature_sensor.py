import random
from datetime import datetime, UTC

from iot_platform.domain.devices.base import Device
from iot_platform.domain.models.sensor_reading import SensorReading


class TemperatureSensor(Device):
   def _generate_reading(self) -> SensorReading:
       temperature = round(random.uniform(-10.0, 50.0), 1)
       temp_obj = SensorReading(
           name=self.name,
           device_id=self.device_id,
           metric="temperature",
           value=temperature,
           unit="C",
           timestamp=datetime.now(UTC)
       )
       return temp_obj





