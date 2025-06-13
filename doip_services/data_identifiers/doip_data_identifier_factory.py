from doip_services.data_identifiers.doip_data_identifiers_util import *
from doip_services.data_identifiers.doip_data_identifiers import *

def _doip_data_identifier_factory(data_identifier_class , _method):

    match data_identifier_class:
        case DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return  VehicleManufacturerSparePartNumber().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return  VehicleManufacturerSparePartNumber().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return  VehicleManufacturerSparePartNumber().get_did_response()

        case DataIdentifiersFactoryClassEnum.VehicleManufacturerEcuSoftwareVersionNumber.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return VehicleManufacturerEcuSoftwareVersionNumber().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return VehicleManufacturerEcuSoftwareVersionNumber().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return VehicleManufacturerEcuSoftwareVersionNumber().get_did_response()

        case DataIdentifiersFactoryClassEnum.VehicleManufacturerECUHardWareNumber.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return VehicleManufacturerECUHardWareNumber().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return VehicleManufacturerECUHardWareNumber().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return VehicleManufacturerECUHardWareNumber().get_did_response()

        case DataIdentifiersFactoryClassEnum.SystemNameOrEngineType.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return SystemNameOrEngineType().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return SystemNameOrEngineType().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return SystemNameOrEngineType().get_did_response()

        case DataIdentifiersFactoryClassEnum.VehicleIdentificationNumber.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return VehicleIdentificationNumber().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return VehicleIdentificationNumber().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return VehicleIdentificationNumber().get_did_response()



