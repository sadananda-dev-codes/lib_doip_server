import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import UsageMode

@pytest.fixture
def usage_mode():
    return UsageMode()
class TestTotalDistance: 
    def test_response_type(self, usage_mode):
        obj_usage_mode = usage_mode
        response = obj_usage_mode.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, usage_mode):
        expected_response = b"\x6E\xDD\x56"
        obj_usage_mode = usage_mode
        received_response = obj_usage_mode.response()
        assert expected_response == received_response
        