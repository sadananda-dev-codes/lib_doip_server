import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import VehicleManufacturerEcuSoftwareVersionNumber

@pytest.fixture
def vehicle_manufacturer_ecu_number():
    return VehicleManufacturerEcuSoftwareVersionNumber()

class TestVehicleManufacturerEcuSoftwareVersionNumber:
    def test_response_type(self, vehicle_manufacturer_ecu_number):
        obj_vehicle_manufacturer_ecu_number = vehicle_manufacturer_ecu_number
        response = obj_vehicle_manufacturer_ecu_number.response()
        assert isinstance(response, bytes)

    def test_response_bytes(self, vehicle_manufacturer_ecu_number):
        obj_vehicle_manufacturer_ecu_number = vehicle_manufacturer_ecu_number
        response = obj_vehicle_manufacturer_ecu_number.response()
        print(response)
        assert isinstance(response, bytes)
        print(response.hex())
        