import random
import struct
from abc import ABC, abstractmethod

from src.lib_doip_server.doip_services.dtc.doip_dtcs import *
from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices
from src.lib_doip_server.doip_services.dtc.doip_dtc_utils import  get_snap_shot_dids

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
        _response = [cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function, cls.dtc_available_status]
        for _dtc, _status in DTC.get_all_dtc_codes_by_status(cls.dtc_status):
            _response.extend(_dtc.to_bytes(3, 'big'))
            _response.append(_status)

        _format = str(len(_response)) + "B"
        return struct.pack(_format, *_response)

class ReadDtcSnapShot(Dtc):
    sub_function = 0x04
    snap_shot_id = 0x20
    snap_shot_dtc = 0x00
    number_of_snapshot_did = 0x5

    @classmethod
    def request(cls):
        _request = [cls.service_id, cls.sub_function]
        _request.extend(cls.snap_shot_dtc.to_bytes(3, 'big'))
        _request.append(cls.snap_shot_id)
        return struct.pack('6B', *_request)

    @classmethod
    def response(cls):
        _response = [cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function]
        _response.extend(cls.snap_shot_dtc.to_bytes(3, 'big'))
        _response.append(DTC.get_dtc_status(cls.snap_shot_dtc))
        _response.append(cls.number_of_snapshot_did)
        _response.extend(get_snap_shot_dids())
        format = str(len(_response)) + 'B'
        return struct.pack(format, *_response)

class ReadDtcExtendedSnapshot(Dtc):
    sub_function = 0x06
    extended_snap_shot_id = 0x01
    extended_snap_shot_dtc = 0x00

    @classmethod
    def request(cls):
        return struct.pack(
                    '6B', cls.service_id,
                    cls.sub_function,
                    *cls.extended_snap_shot_dtc.to_bytes(3, 'big'),
                    cls.extended_snap_shot_id
                    )

    @classmethod
    def response(cls):
        return struct.pack(
                        '8B', cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                        cls.sub_function,
                        *cls.extended_snap_shot_dtc.to_bytes(3, 'big'),
                        DTC[cls.extended_snap_shot_dtc].dtc_status,
                        cls.extended_snap_shot_id,
                        random.randint(1,0xFF)
                        )

class ReadSupportedDtc(Dtc):
    sub_function = 0xA

    @classmethod
    def request(cls):
        return struct.pack('2B', cls.service_id, cls.sub_function)

    @classmethod
    def response(cls):
        _response = [cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function, cls.dtc_available_status]
        for _dtc, _status in DTC.get_all_dtc_codes_by_status(cls.dtc_status):
            _response.extend(_dtc.to_bytes(3, 'big'))
            _response.append(_status)

        _format = str(len(_response)) + "B"
        return struct.pack(_format, *_response)

class ReadAvailableDtc(Dtc):
    sub_function = 0x03

    @classmethod
    def request(cls):
        return struct.pack('2B', cls.service_id, cls.sub_function)

    @classmethod
    def response(cls):
        _response = [cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function]
        for _dtc in DTC.get_all_dtc_codes():
            _response.extend(_dtc.to_bytes(3, 'big'))
            _response.append(ReadDtcSnapShot.snap_shot_id)
        _format = str(len(_response)) + "B"
        return struct.pack(_format, *_response)

read = ReadDtcInformation()
print(read.request().hex())
print(read.response().hex())

ReadDtcSnapShot.snap_shot_dtc = 0x328511
print(ReadDtcSnapShot.request().hex())
print(ReadDtcSnapShot.response().hex())

print('---------------------------------')

ReadDtcExtendedSnapshot.extended_snap_shot_dtc = 0x328511
print(ReadDtcExtendedSnapshot.request().hex())
print(ReadDtcExtendedSnapshot.response().hex())

print('---------------------------------')

print(ReadSupportedDtc.request().hex())
print(ReadSupportedDtc.response().hex())

print('---------------------------------')

print(ReadAvailableDtc.request().hex())
print(ReadAvailableDtc.response().hex())
print(' '.join(f'{b:02X}' for b in ReadAvailableDtc.response()))