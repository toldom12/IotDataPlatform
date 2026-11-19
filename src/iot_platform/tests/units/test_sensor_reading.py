from logging import exception

import pytest

from iot_platform.domain.models.sensor_reading import IsNotValidParameter, SensorReading
from iot_platform.tests.units.tools_test_sensor_reading import ObjValidation, CaseName
from tools.TestStepsVerificator.StepsVerficator import TesStepsVerifcator

@pytest.mark.daily
@pytest.mark.parametrize("data_obj",[data.value for data in ObjValidation])
def test_create_obj_sensor_reading(data_obj: SensorReading):
    test = TesStepsVerifcator()

    name = data_obj.name
    device_id = data_obj.device_id
    metric = data_obj.metric
    value = data_obj.value
    unit = data_obj.unit
    timestamp = data_obj.timestamp


    try:
        create_obj = SensorReading(name = name,
                                   device_id=device_id,
                                   metric = metric,
                                   value = value,
                                   unit = unit,
                                   timestamp=timestamp)

    except IsNotValidParameter:
        test.add_test(condition=True, fail_msg='')

    except exception as e:
        test.add_test(condition=False, fail_msg=f'Not expected exception {e}')

    if data_obj.name in CaseName.ZeroValue:
        test.add_test(condition=bool(data_obj.value == 0),
                      fail_msg=f'Data obj is != value {data_obj.value}')

    assert test.expected_results == test.received_results



