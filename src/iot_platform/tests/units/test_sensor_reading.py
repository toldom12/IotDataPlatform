import pytest

from iot_platform.domain.models.sensor_reading import SensorReading
from iot_platform.tests.units.tools_test_sensor_reading import CreateObj


@pytest.mark.parametrize("data_obj",[data.value for data in CreateObj])
def test_create_obj_sensor_reading(data_obj: SensorReading):
    pass    
