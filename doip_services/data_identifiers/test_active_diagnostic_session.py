import pytest

from lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import ActiveDiagnosticSession

@pytest.fixture
def active_diagnostic_session():
    return ActiveDiagnosticSession()

class TestActiveDiagnosticSession:
    
    @pytest.mark.order(2)
    def test_response_type(self, active_diagnostic_session):
        diag_session = active_diagnostic_session
        response = diag_session.response()
        assert isinstance(response, bytes)
        
    @pytest.mark.order(1)
    def test_response_bytes(self, active_diagnostic_session):
        expected_response = b"\x62\xF1\x86\x02"
        diag_session = active_diagnostic_session
        received_response = diag_session.response()
        assert expected_response == received_response
        
    @pytest.mark.order(3)
    def test_current_session(self, active_diagnostic_session):
        expected_response = b"\x62\xF1\x86\x02"
        from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticSessionStatus
        DiagnosticSessionStatus.ACTIVE_SESSION = 0x02
        diag_session = active_diagnostic_session
        received_response = diag_session.response()
        print(expected_response.hex())
        print(received_response.hex())
        assert expected_response == received_response
