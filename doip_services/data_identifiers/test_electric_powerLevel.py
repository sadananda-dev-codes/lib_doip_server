import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import ElectricPowerLevel

@pytest.fixture
def electric_power_level():
    return ElectricPowerLevel()

class TestElectricPowerLevel:
    def test_response_type(self, electric_power_level):
        obj_electric_power_level = electric_power_level
        response = obj_electric_power_level.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, electric_power_level):
        expected_response = b"\x6E\xDD\x51"
        obj_electric_power_level = electric_power_level
        received_response = obj_electric_power_level.response()
        assert expected_response == received_response
        