import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import SystemNameOrEngineType

@pytest.fixture
def system_name_or_engine_type():
    return SystemNameOrEngineType()
class TestSystemNameOrEngineType: 
    def test_response_type(self, system_name_or_engine_type):
        obj_system_name_or_engine_type = system_name_or_engine_type
        response = obj_system_name_or_engine_type.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, system_name_or_engine_type):
        expected_response = b"\x62\xF1\x97\x48\x43\x22\xE4\xC6\xF7\x72\x20\x20\x20\x20"
        obj_system_name_or_engine_type = system_name_or_engine_type
        received_response = obj_system_name_or_engine_type.response()
        assert expected_response == received_response
        