import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import GlobalRealTime

@pytest.fixture
def global_real_time():
    return GlobalRealTime()
class TestGlobalRealTime:
    def test_response_type(self, global_real_time):
        obj_global_real_time = global_real_time
        response = obj_global_real_time.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, global_real_time):
        expected_response = b"\x6E\xDD\x00"
        obj_global_real_time = global_real_time
        received_response = obj_global_real_time.response()
        assert expected_response == received_response
        