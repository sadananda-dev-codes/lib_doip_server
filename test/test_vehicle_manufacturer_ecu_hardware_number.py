import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import VehicleManufacturerECUHardWareNumber

@pytest.fixture
def vehicle_manufacturer_ecu_hardware_number():
    return VehicleManufacturerECUHardWareNumber()
class TestVehicleManufacturerECUHardWareNumber: 
    def test_response_type(self, vehicle_manufacturer_ecu_hardware_number):
        obj_vehicle_manufacturer_ecu_hardware_number = vehicle_manufacturer_ecu_hardware_number
        response = obj_vehicle_manufacturer_ecu_hardware_number.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, vehicle_manufacturer_ecu_hardware_number):
        expected_response = b"\x62\xF1\x91\x38\x35\x45\x39"
        obj_vehicle_manufacturer_ecu_hardware_number = vehicle_manufacturer_ecu_hardware_number
        received_response = obj_vehicle_manufacturer_ecu_hardware_number.response()
        assert expected_response == received_response
        