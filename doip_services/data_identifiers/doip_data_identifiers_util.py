from enum import Enum
from lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticSessionStatus

class DataIdentifiersFactoryClassEnum(Enum):
    ActiveDiagnosticSession = 'ActiveDiagnosticSession'
    VehicleManufacturerSparePartNumber = 'VehicleManufacturerSparePartNumber'
    VehicleManufacturerEcuSoftwareVersionNumber = 'VehicleManufacturerEcuSoftwareVersionNumber'
    VehicleManufacturerECUHardWareNumber = 'VehicleManufacturerECUHardWareNumber'
    SystemNameOrEngineType = 'SystemNameOrEngineType'
    VehicleIdentificationNumber = 'VehicleIdentificationNumber'
    GlobalRealTime = 'GlobalRealTime'
    TotalDistance = 'TotalDistance'
    VehicleBatteryVoltage = 'VehicleBatteryVoltage'
    UsageMode = 'UsageMode'
    ElectricPowerLevel ='ElectricPowerLevel'

def get_fmt_did_response(data_identifiers):
    
    if data_identifiers == DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value:
        return '5B'
    
    if data_identifiers == DataIdentifiersFactoryClassEnum.VehicleManufacturerEcuSoftwareVersionNumber.value:
        return '3B'
    
    if data_identifiers == DataIdentifiersFactoryClassEnum.VehicleManufacturerECUHardWareNumber.value:
        return '4B'
    
    if data_identifiers == DataIdentifiersFactoryClassEnum.SystemNameOrEngineType.value:
        return '11B'
    
    if data_identifiers == DataIdentifiersFactoryClassEnum.VehicleIdentificationNumber.value:
        return '6B'

class DataIdentifiersFactoryMethods(Enum):
    request = 1
    response = 2
    get_did_response = 3

read_data_by_identifiers = {
        'ActiveDiagnosticSession': (
            0xF1,
            0x86,
            '3B',
            '4B',
            (DiagnosticSessionStatus.ACTIVE_SESSION,)
        ),
        
        'VehicleManufacturerSparePartNumber': (
            0xF1,
            0x87,
            '3B',
            '8B',
            (0x31, 0x35, 0x36, 0x41, 0x48)
        ),
        
        'VehicleManufacturerEcuSoftwareVersionNumber': (
            0xF1,
            0x89,
            '3B',
            '6B',
            (0x34, 0x33, 0x37)
        ),
        
        'VehicleManufacturerECUHardWareNumber': (
            0xF1,
            0x91,
            '3B',
            '7B',
            (0x38, 0x35, 0x45, 0x39)
        ),
        
        'SystemNameOrEngineType': (
            0xF1,
            0x97,
            '3B',
            '14B',
            (0x48, 0x43, 0x22, 0xE4, 0xC6, 0xF7, 0x72, 0x20, 0x20, 0x20, 0x20)
        ),
        
        'VehicleIdentificationNumber': (
            0xF1,
            0x90,
            '3B',
            '9B',
            (0x32, 0x85, 0x32, 0x85, 0x32, 0x85)
        )
    }

write_data_by_identifiers = {
        'GlobalRealTime': (
            0xDD,
            0x00,
            '7B',
            '3B',
            [0x20, 0x05, 0x16, 0x12]
        ),
        
        'TotalDistance':(
            0xDD,
            0x32,
            '6B',
            '3B',
            [0x56, 0x32, 0x85]
        ),
        
        'VehicleBatteryVoltage':(
            0xDD,
            0x85,
            '4B',
            '3B',
            [0x32]
        ), 
        
        'UsageMode':(
            0xDD,
            0x56,
            '4B',
            '3B',
            [0x02]
        ), #one byte
        
        'ElectricPowerLevel':(
            0xDD,
            0x51,
            '4B',
            '3B',
            [0x0F]
        ) # one byte
    }

