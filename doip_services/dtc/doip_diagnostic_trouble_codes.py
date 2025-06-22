import random
from abc import ABC, abstractmethod
from doip_services.dtc.doip_dtcs import *
import struct

class Dtc(ABC):
    service_id = 0x19
    dtc_status = 0x2F
    dtc_available_status = 0xFF

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
        return struct.pack('3B', cls.service_id, cls.sub_function, cls.dtc_status)

    @classmethod
    def response(cls):
        _dcts_with_status = DTC.get_all_dtc_codes_by_status(cls.dtc_status)
        struct_format = len(_dcts_with_status) * 4 + 5
        return _dcts_with_status

class ReadDtcSnapShot(Dtc):
    sub_function = 0x04
    snap_shot_dtc = 0x00

    @classmethod
    def request(cls):
        pass

    @classmethod
    def response(cls):
        pass

class ReadDtcExtendedSnapshot(Dtc):
    sub_function = 0x06
    extended_id = 0x01
    extended_dtc = 0x00

    @classmethod
    def request(cls):
        return struct.pack('6B', cls.service_id,
                           cls.sub_function,
                           cls.extended_dtc.to_bytes(3, 'big'),
                           DTC[cls.extended_dtc].dtc_status,
                           cls.extended_id,
                           random.random(0xFF)
                           )

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

read = ReadDtcInformation()
print(read.request().hex())
#print(read.response())

read = ReadDtcExtendedSnapshot()
print(read.request().hex())