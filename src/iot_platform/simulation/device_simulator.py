from iot_platform.domain.devices.base import Device
from iot_platform.domain.devices.temperature_sensor import TemperatureSensor
from iot_platform.domain.models.sensor_reading import SensorReading


class DeviceSimulator:
    def generate_readings(self, device: Device, count : int) -> list[SensorReading]:
        generate_objects : list = []
        for index in range(count):
                reading = device.generate_reading()
                generate_objects.append(reading)
        return generate_objects




if __name__ == "__main__":
    sensor = TemperatureSensor(
        device_id="TEMP-001",
        name="Living Room",
        is_active=True
    )

    simulator = DeviceSimulator()

    readings = simulator.generate_readings(device=sensor, count=100)
    pass

