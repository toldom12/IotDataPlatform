from logging import exception

import pytest

from iot_platform.domain.devices.temperature_sensor import TemperatureSensor
from iot_platform.simulation.device_simulator import DeviceSimulator
from iot_platform.tests.units.simulation.tools_device_simulation import GenerateParameters, GenerateSimulations
from tools.TestStepsVerificator.StepsVerficator import TesStepsVerifcator


@pytest.mark.parametrize("data", [params.value for params in GenerateParameters])
def test_device_simulator(data: GenerateSimulations ):

    test = TesStepsVerifcator()


    try:

        sensor = TemperatureSensor(
            device_id=data.device_id,
            name=data.name,
            is_active=True
        )

        simulator = DeviceSimulator()

        readings = simulator.generate_readings(device=sensor, count=data.count)

    except  Exception as e :
        print(e)