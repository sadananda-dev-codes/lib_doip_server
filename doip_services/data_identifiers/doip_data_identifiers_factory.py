from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import *
from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import *

def _doip_data_identifier_factory(_data_identifier, _method):
    
    print('Sadananda Maharaj',_data_identifier, _method)
    
    diag_object = None
    
    if _data_identifier == DataIdentifiersFactoryClassEnum.ActiveDiagnosticSession.value:
        
        diag_object = ActiveDiagnosticSession()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value:
        
        diag_object = VehicleManufacturerSparePartNumber()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerEcuSoftwareVersionNumber.value:
        
        diag_object = VehicleManufacturerEcuSoftwareVersionNumber()
    
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleManufacturerECUHardWareNumber.value:    
    
        diag_object = VehicleManufacturerECUHardWareNumber()
    
    if _data_identifier == DataIdentifiersFactoryClassEnum.SystemNameOrEngineType.value:
        
        diag_object = SystemNameOrEngineType()
    
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleIdentificationNumber.value:
        
        diag_object = VehicleIdentificationNumber()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.GlobalRealTime.value:
        
        diag_object = GlobalRealTime()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.TotalDistance.value:
        
        diag_object = TotalDistance()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.VehicleBatteryVoltage.value:
        
        diag_object = VehicleBatteryVoltage() 
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.UsageMode.value:
        
        diag_object = UsageMode()
        
    if _data_identifier == DataIdentifiersFactoryClassEnum.ElectricPowerLevel.value:
        
        diag_object = ElectricPowerLevel()

    if _method == DataIdentifiersFactoryMethods.request.value:
        return  diag_object.request()
    if _method == DataIdentifiersFactoryMethods.response.value:
        return  diag_object.response()
    if _method == DataIdentifiersFactoryMethods.get_did_response.value:
        return  diag_object.get_did_response()

    return None

