from enum import Enum

class DataIdentifiersFactoryEnum(Enum):
    VehicleManufacturerSparePartNumber = 'VehicleManufacturerSparePartNumber'
    VehicleManufacturerEcuSoftwareVersionNumber = 'VehicleManufacturerEcuSoftwareVersionNumber'
    VehicleManufacturerECUHardWareNumber = 'VehicleManufacturerECUHardWareNumber'
    SystemNameOrEngineType = 'SystemNameOrEngineType'
    VehicleIdentificationNumber = 'VehicleIdentificationNumber'

class DataIdentifiersFactoryMethods(Enum):
    request = 1
    response = 2
    get_did_response = 3
