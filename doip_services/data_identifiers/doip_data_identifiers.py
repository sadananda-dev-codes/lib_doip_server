import struct

from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import (
    read_data_by_identifiers,
    write_data_by_identifiers,
    get_fmt_did_response,
)
from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices
class SingletonDataIdentifiers(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
class DataIdentifiers:

    __data_identifier_parameters__ = (
        'data_identifier_lsb',
        'data_identifier_msb',
        'request_format',
        'response_format',
        'data_identifier_response'
    )

    def __init__(self,
                service_type,
                data_identifier_values
                ):
        self.service_id = service_type

        for data_identifier_attr, data_id_values in zip(self.__data_identifier_parameters__,
                                                        data_identifier_values):
            setattr(self, data_identifier_attr, data_id_values)

    def request(self, write_did = []):

        if isinstance(self, ReadDataByIdentifier):
            return struct.pack(
                        self.request_format,
                        self.service_id,
                        self.data_identifier_lsb,
                        self.data_identifier_msb
                        )
            
        if isinstance(self, WriteDataByIdentifier):
            if write_did:
                self.data_identifier_response = write_did
            return struct.pack(
                            self.request_format, 
                            self.service_id,
                            self.data_identifier_lsb,
                            self.data_identifier_msb,
                            *self.data_identifier_response
                            )

    def response(self):
        if isinstance(self, ReadDataByIdentifier):
            return struct.pack(
                        self.response_format,
                        self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                        self.data_identifier_lsb,
                        self.data_identifier_msb,
                        *self.data_identifier_response
                        )
        if isinstance(self, WriteDataByIdentifier):
            return struct.pack(
                self.response_format,
                self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                self.data_identifier_lsb,
                self.data_identifier_msb
            )
            
    def get_did_response(self):
        fmt = get_fmt_did_response(self.__class__.__name__)
        return struct.pack(fmt, *self.data_identifier_response)
class ReadDataByIdentifier(DataIdentifiers, metaclass=SingletonDataIdentifiers):

    def __init__(self):
        read_did_key =  self.__class__.__name__
        super().__init__(DiagnosticServices.READ_DATA_BY_IDENTIFIER.value,
                        read_data_by_identifiers[read_did_key])

class WriteDataByIdentifier(DataIdentifiers, metaclass=SingletonDataIdentifiers):
    def __init__(self):
        write_did_key = self.__class__.__name__
        super().__init__(DiagnosticServices.WRITE_DATA_BY_IDENTIFIER.value,
                        write_data_by_identifiers[write_did_key])
class ActiveDiagnosticSession(ReadDataByIdentifier):
    pass
class VehicleManufacturerSparePartNumber(ReadDataByIdentifier):
    pass
class VehicleManufacturerEcuSoftwareVersionNumber(ReadDataByIdentifier):
    pass
class VehicleManufacturerECUHardWareNumber(ReadDataByIdentifier):
    pass
class SystemNameOrEngineType(ReadDataByIdentifier):
    pass
class VehicleIdentificationNumber(ReadDataByIdentifier):
    pass
class GlobalRealTime(WriteDataByIdentifier):
    pass
class TotalDistance(WriteDataByIdentifier):
    pass
class VehicleBatteryVoltage(WriteDataByIdentifier):
    pass
class UsageMode(WriteDataByIdentifier):
    pass
class ElectricPowerLevel(WriteDataByIdentifier):
    pass


print('Sadananda Maharaj')

a = ActiveDiagnosticSession()
data = a.request()
print(" ".join(f"{b:02x}" for b in data))

data = a.response()
print(" ".join(f"{b:02x}" for b in data))

print('------------------------------------')

s = SystemNameOrEngineType()

data = s.request()
print(" ".join(f"{b:02x}" for b in data))

data = s.response()
print(" ".join(f"{b:02x}" for b in data))

print('------------------------------------')

v = VehicleIdentificationNumber()
data = v.request()
print(" ".join(f"{b:02x}" for b in data))

data = v.response()
print(" ".join(f"{b:02x}" for b in data))
print('------------------------------------')

s = SystemNameOrEngineType()
data = s.request()
print(" ".join(f"{b:02x}" for b in data))

data = s.response()
print(" ".join(f"{b:02x}" for b in data))
print('------------------------------------')

_v = VehicleManufacturerECUHardWareNumber()
data = _v.request()
print(" ".join(f"{b:02x}" for b in data))

data = _v.response()
print(" ".join(f"{b:02x}" for b in data))
print('------------------------------------')

g = GlobalRealTime()
data = g.request()
print(" ".join(f"{b:02x}" for b in data))

data = g.response()
print(" ".join(f"{b:02x}" for b in data))

print('------------------------------------')

t = TotalDistance()
data = t.request()
print(" ".join(f"{b:02x}" for b in data))

data = t.response()
print(" ".join(f"{b:02x}" for b in data))

print('----------------------------------')

v = VehicleBatteryVoltage()
data = v.request()
print(" ".join(f"{b:02x}" for b in data))

data = v.response()
print(" ".join(f"{b:02x}" for b in data))

print('-----------------------------------')

u = UsageMode()
data = u.request()
print(" ".join(f"{b:02x}" for b in data))

data = u.response()
print(" ".join(f"{b:02x}" for b in data))

print('------------------------------------')

e = ElectricPowerLevel()
data = e.request([32])
print(" ".join(f"{b:02x}" for b in data))

data = e.response()
print(" ".join(f"{b:02x}" for b in data))

print(e.data_identifier_response)
print(write_data_by_identifiers)

e1 = ElectricPowerLevel()
data = e1.request([85])
print(" ".join(f"{b:02x}" for b in data))

data = e1.response()
print(" ".join(f"{b:02x}" for b in data))

print(e1.data_identifier_response)
print(write_data_by_identifiers)

u1 = UsageMode()
data = u1.request()
print(" ".join(f"{b:02x}" for b in data))

data = u1.response()
print(" ".join(f"{b:02x}" for b in data))

print('End of my requirement')
print('')