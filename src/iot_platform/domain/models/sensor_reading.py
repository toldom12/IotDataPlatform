from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime


class IsNotValidParameter(Exception):
    pass


@dataclass(frozen=True)
class SensorReading:
    name: str
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
            if self.value ==0 or self.value == 0.0:
                pass
            else:
                raise IsNotValidParameter(f"Empty parameter: {self.value}")
        if not self.unit:
            raise IsNotValidParameter(f"Empty parameter: {self.unit}")
        #TODO better verifcation for timestamp :
         # - datetime
         # - utc zone
         # - correctly time stamp for our system
        if not self.timestamp:
            raise IsNotValidParameter(f"Empty parameter: {self.timestamp}")
        if not isinstance(self.value,(float or int)):
            raise IsNotValidParameter(f"Not correctly param: {self.value}, type: {type(self.value)}")


class TelemetryBuffer:
    def __init__(self):
        self.__measurements : dict = {}

    def add_measurements(self, meas: SensorReading or list[SensorReading]) -> None:
        meas = meas if isinstance(meas, list) else [meas]
        measurements = self.__measurements.setdefault("measurements", {}) #
        for obj in meas:
           by_name = measurements.setdefault(obj.name, defaultdict(list))
           by_name[obj.device_id].append({
               "metric": obj.metric,
               "value": obj.value,
               "unit": obj.unit,
               "timestamp": obj.timestamp,
           })
    @property
    def get_measurements(self) -> dict:
        return self.__measurements

    def filter_by_device_id(self,
                            device_id : str or list[str],
                            name: str) -> dict:
        if isinstance(device_id, str):
             return {"device_id" :self.__measurements['measurements'][name][f'{device_id}']}
        else:
            device_id_dict  : dict = {}
            for expected_device in device_id:
                key = expected_device
                if key in self.__measurements['measurements'][name]:
                    device_id_dict[key] = self.__measurements['measurements'][name][key]

            return device_id_dict

    def filter_by_metrics(self,
                          device_id: str | list[str],
                          name: str,
                          metrics : str | list[str]) -> dict:
        if isinstance(metrics, str):
             results_metrics : list = []
             readings = self.__measurements['measurements'][name][f'{device_id}']
             for data_metrics in readings:
                 if metrics == data_metrics['metric']:
                     results_metrics.append(data_metrics)
             return {'metrics': results_metrics}
        else: # TODO: metrics filtering  in queue
            metrics_dict  : dict = {}
            for expected_metrics in metrics:
                key = expected_metrics
                if key in self.__measurements['measurements'][name]:
                    metrics_dict[key] = self.__measurements['measurements'][name][key]
            return metrics_dict

    @property
    def count_measurements(self) -> int:
        return len(self.__measurements)

    @property
    def clear_buffer(self) -> bool:
        return len(self.__measurements) == 0

    @clear_buffer.setter
    def clear_buffer(self, clear_buffer: bool = True):
        if clear_buffer:
            self.__measurements.clear()


if __name__ == "__main__":
    reading = SensorReading(
        name = 'temp_sensor',
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )
    reading1 = SensorReading(
        name='temp_sensor',
        device_id="TEMP-001",
        metric="temperature",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )

    reading2 = SensorReading(
        name='humidtity_sensor',
        device_id="HUM-002",
        metric="humidity",
        value=23.5,
        unit="C",
        timestamp=datetime.now(UTC)
    )
    a = TelemetryBuffer()
    a.add_measurements(meas=reading)
    a.add_measurements(meas=reading1)
    a.add_measurements(meas=reading2)
    results = a.filter_by_device_id(name='temp_sensor', device_id=['TEMP-001','TEMP-001'])
    results2 = a.filter_by_metrics(name=['temp_sensor', 'humidity_sensor'],
                                   device_id=['TEMP-001','HUM-002'],
                                    metrics = ['temperature','humidity'])
    # results = a.filter_by_device_id(name='temp_sensor', device_id='TEMP-003')
    pass
