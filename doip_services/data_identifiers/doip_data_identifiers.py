import struct

from lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticSessionStatus

from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import (
    read_data_by_identifiers,
    write_data_by_identifiers,
    get_fmt_did_response,
)
from lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticServices
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
    
    def response(self):
        return struct.pack(
                    self.response_format,
                    self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                    self.data_identifier_lsb,
                    self.data_identifier_msb,
                    DiagnosticSessionStatus.ACTIVE_SESSION
                    )
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

