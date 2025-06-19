from abc import ABC, abstractmethod

class DTC(ABC):
    service_id = 0x19

    @abstractmethod
    def request(self):
        pass

    @abstractmethod
    def response(self):
        pass

class ReadDtcInformation:
    sub_function = 0x02

class ReadDtcSnapShot:
    sub_function = 0x04

class ReadDtcExtendedSnapshot:
    sub_function = 0x06