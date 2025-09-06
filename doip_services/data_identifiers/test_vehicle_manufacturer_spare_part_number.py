import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import VehicleManufacturerSparePartNumber

@pytest.fixture
def vehicle_manufacturer_spare_part_number():
    return VehicleManufacturerSparePartNumber()

class TestVehicleManufacturerSparePartNumber:
    def test_response_type(self, vehicle_manufacturer_spare_part_number):
        vehicle_manufacturer_number = vehicle_manufacturer_spare_part_number
        response = vehicle_manufacturer_number.response()
        assert isinstance(response, bytes)
        print(response.hex())
    
    def test_response_byte(self, vehicle_manufacturer_spare_part_number):
        vehicle_manufacturer_number = vehicle_manufacturer_spare_part_number
        response = vehicle_manufacturer_number.response()
        assert isinstance(response, bytes)
        print(response.hex())