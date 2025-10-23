import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import TotalDistance

@pytest.fixture
def total_distance():
    return TotalDistance()
class TestTotalDistance: 
    def test_response_type(self, total_distance):
        obj_total_distance = total_distance
        response = obj_total_distance.response()
        assert isinstance(response, bytes)
    
    def test_response_byte(self, total_distance):
        expected_response = b"\x6E\xDD\x32"
        obj_total_distance = total_distance
        received_response = obj_total_distance.response()
        assert expected_response == received_response
        