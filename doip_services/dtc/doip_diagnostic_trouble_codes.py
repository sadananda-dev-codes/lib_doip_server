from abc import ABC, abstractmethod
from doip_services.dtc.doip_dtc_utils import DTC

class Dtc(ABC):
    service_id = 0x19
    dtc_status = 0x2F

    @classmethod
    @abstractmethod
    def request(cls):
        pass

    @classmethod
    @abstractmethod
    def response(cls):
        pass

class ReadDtcInformation(Dtc):
    sub_function = 0x02

    @classmethod
    def request(cls):
        _dct = DTC.get_all_dtc_codes_by_status(cls.dtc_status)
        return

    @classmethod
    def response(cls):
        return

class ReadDtcSnapShot(Dtc):
    sub_function = 0x04

    @classmethod
    def request(cls):
        pass

    @classmethod
    def response(cls):
        pass

class ReadDtcExtendedSnapshot(Dtc):
    sub_function = 0x06

    @classmethod
    def request(cls):
        pass

    @classmethod
    def response(cls):
        pass

class ReadSupportedDtc(Dtc):
    sub_function = 0xA

    @classmethod
    def request(cls):
        pass

    @classmethod
    def response(cls):
        pass

class ReadAvailableDtc(Dtc):
    sub_function = 0x03

    @classmethod
    def request(cls):
        pass

    @classmethod
    def response(cls):
        pass

