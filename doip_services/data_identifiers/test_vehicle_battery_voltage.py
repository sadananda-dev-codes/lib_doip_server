import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import VehicleBatteryVoltage

@pytest.fixture
def vehicle_battery_voltage():
    return VehicleBatteryVoltage()
class TestVehicleBatteryVoltage: 
    def test_response_type(self, vehicle_battery_voltage):
        obj_vehicle_battery_voltage = vehicle_battery_voltage
        response = obj_vehicle_battery_voltage.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, vehicle_battery_voltage):
        expected_response = b"\x6E\xDD\x85"
        obj_vehicle_battery_voltage = vehicle_battery_voltage
        received_response = obj_vehicle_battery_voltage.response()
        assert expected_response == received_response
        