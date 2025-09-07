import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import VehicleIdentificationNumber

@pytest.fixture
def vehicle_identification_number():
    return VehicleIdentificationNumber()
class TestVehicleIdentificationNumber: 
    def test_response_type(self, vehicle_identification_number):
        obj_vehicle_identification_number = vehicle_identification_number
        response = obj_vehicle_identification_number.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, vehicle_identification_number):
        expected_response = b"\x62\xF1\x90\x32\x85\x32\x85\x32\x85"
        obj_vehicle_identification_number = vehicle_identification_number
        received_response = obj_vehicle_identification_number.response()
        assert expected_response == received_response
        