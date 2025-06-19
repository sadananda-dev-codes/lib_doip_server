import struct
from  doip_services.data_identifiers.doip_data_identifiers_util import  (
    read_data_by_identifier,
    write_data_by_identifier
    )
from  doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices

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

    def request(self):
        if isinstance(self, ReadDataByIdentifier):
            return struct.pack(self.request_format, self.service_id, self.data_identifier_lsb,
                           self.data_identifier_msb)
        if isinstance(self, WriteDataByIdentifier):
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

class ReadDataByIdentifier(DataIdentifiers):

    def __init__(self):
        super().__init__(DiagnosticServices.READ_DATA_BY_IDENTIFIER.value,
                         read_data_by_identifier[self.__class__.__name__])

    def get_did_response(self):
        return self.data_identifier_response

class WriteDataByIdentifier(DataIdentifiers):
    def __init__(self):
        super().__init__(DiagnosticServices.WRITE_DATA_BY_IDENTIFIER.value,
                         write_data_by_identifier[self.__class__.__name__])

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

'''
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
'''

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
print(e.request().hex())
print(e.response().hex())
