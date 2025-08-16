from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import *
from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import *

def _doip_data_identifier_factory(
                                _data_identifier,
                                _method
                                ):
    
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value:
        if _method == DataIdentifiersFactoryMethods.request.value:
            return  VehicleManufacturerSparePartNumber().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return  VehicleManufacturerSparePartNumber().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return  VehicleManufacturerSparePartNumber().get_did_response()

    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerEcuSoftwareVersionNumber.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return VehicleManufacturerEcuSoftwareVersionNumber().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return VehicleManufacturerEcuSoftwareVersionNumber().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return VehicleManufacturerEcuSoftwareVersionNumber().get_did_response()

    
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerECUHardWareNumber.value:    
    
        if _method == DataIdentifiersFactoryMethods.request.value:
            return VehicleManufacturerECUHardWareNumber().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return VehicleManufacturerECUHardWareNumber().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return VehicleManufacturerECUHardWareNumber().get_did_response()

    
    if _data_identifier == DataIdentifiersFactoryClassEnum.SystemNameOrEngineType.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return SystemNameOrEngineType().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return SystemNameOrEngineType().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return SystemNameOrEngineType().get_did_response()

    
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleIdentificationNumber.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return VehicleIdentificationNumber().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return VehicleIdentificationNumber().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return VehicleIdentificationNumber().get_did_response()

    return None

