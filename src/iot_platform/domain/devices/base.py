from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self,
                 device_id: str,
                 name: str,
                 is_active: bool):
        self.device_id = device_id
        self.name = name
        self.is_active = is_active

    @property
    def is_active(self) -> bool:
        return self.is_active

    @is_active.setter
    def is_active(self, value):
        if isinstance(value, bool):
            self.is_active = value
        else:
            raise

    @abstractmethod
    def generate_reading(self) -> None:
        pass

    @is_active.setter
    def is_active(self, value):
        self._is_active = value


if __name__ =="__main__":
    pass





