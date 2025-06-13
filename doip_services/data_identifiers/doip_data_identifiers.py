import struct
from utils_constants.doip_constants import  read_data_by_identifier
from  doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices

class DataIdentifiers:

    __data_identifier_parameters__ = (
        'data_identifier_lsb',
        'data_identifier_msb',
        'struct_format',
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
        return struct.pack('3B', self.service_id, self.data_identifier_lsb,
                           self.data_identifier_msb)

    def response(self):
        return struct.pack(
                           self.struct_format,
                       self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                           self.data_identifier_lsb,
                           self.data_identifier_msb,
                           *self.data_identifier_response
                           )

class ReadDataByIdentifier(DataIdentifiers):

    def __init__(self):
        super().__init__(DiagnosticServices.READ_DATA_BY_IDENTIFIER.value,
                         read_data_by_identifier[self.__class__.__name__])

    def get_did_response(self):
        return self.data_identifier_response

class WriteDataByIdentifier(DataIdentifiers):
    service_id = DiagnosticServices.WRITE_DATA_BY_IDENTIFIER.value

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

ads = ActiveDiagnosticSession()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

ads = VehicleManufacturerSparePartNumber()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

ads = VehicleManufacturerEcuSoftwareVersionNumber()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

ads = VehicleManufacturerECUHardWareNumber()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

ads = SystemNameOrEngineType()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

ads = VehicleIdentificationNumber()
print(ads.request().hex())
print(ads.response().hex())
print(ads.get_did_response())

print('---------------------------')

