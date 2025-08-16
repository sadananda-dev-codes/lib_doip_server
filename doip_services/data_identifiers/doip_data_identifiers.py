import struct

from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import (
    read_data_by_identifiers,
    write_data_by_identifiers,
    get_fmt_did_response
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
            return struct.pack(self.request_format, self.service_id, self.data_identifier_lsb,
                        self.data_identifier_msb)
            
        if isinstance(self, WriteDataByIdentifier):
            if write_did:
                self.data_identifier_response = write_did
            return struct.pack(self.request_format, self.service_id, self.data_identifier_lsb,
                               self.data_identifier_msb, *self.data_identifier_response)

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
print(list(a.request().hex()))
print(list(a.response().hex()))

s = SystemNameOrEngineType()
print(list(s.request().hex()))
print(list(s.response().hex()))

v = VehicleIdentificationNumber()
print(list(v.request().hex()))
print(list(v.response().hex()))

s = SystemNameOrEngineType()
print(list(s.request().hex()))
print(list(s.response().hex()))

_v = VehicleManufacturerECUHardWareNumber()
print(list(_v.request().hex()))
print(list(_v.response().hex()))

g = GlobalRealTime()
print(g.request().hex())
print(g.response().hex())

print('------------------------')

t = TotalDistance()
print(t.request().hex())
print(t.response().hex())

print('------------------------')

v = VehicleBatteryVoltage()
print(v.request().hex())
print(v.response().hex())

print('------------------------')

u = UsageMode()
print(u.request().hex())
print(u.response().hex())

print('------------------------')

e = ElectricPowerLevel()
print(e.request([32]).hex())
print(e.response().hex())
print(e.data_identifier_response)
print(write_data_by_identifiers)

e1 = ElectricPowerLevel()
print(e1.request([85]).hex())
print(e1.response().hex())
print(e1.data_identifier_response)
print(write_data_by_identifiers)

u1 = UsageMode()
print(u1.request().hex())
print(u1.response().hex())

print(hex(id(e)) , hex(id(e1)), hex(id(u)), hex(id(u1)))

print('End of my requirement')
print('')