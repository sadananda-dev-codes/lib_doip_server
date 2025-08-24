from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import (
                                                                        read_data_by_identifiers,
                                                                        write_data_by_identifiers,
                                                                        DataIdentifiersFactoryMethods                                                                       
                                                                        )
from src.lib_doip_server.configs.read_yaml import *
from src.lib_doip_server.configs.doip_sessions_status import DoIPState
from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_factory import _doip_data_identifier_factory
from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticsNRC
class DataIdentifierHandler:
    service = []
    session = []
    security_service = 0x00
    response = None
    
    @classmethod
    def reset_session_details(cls):
        cls.service.clear()
        cls.session.clear()
        cls.response = None
        cls.security_service = 0x00

def _load_data_identifier(_did, sid=0x22):
    
    data_identifiers = read_data_by_identifiers.items() if sid==0x22 else write_data_by_identifiers.values() if sid==0x2E else []
    
    for service, did in data_identifiers:
        read_did = did[0]
        read_did = (read_did << 8 | did[1])
        if _did == read_did:
            DataIdentifierHandler.service.append(service)

def _is_request_out_of_range(did, sid=0x22):
    
    _load_data_identifier(did, sid)
    
    if  DataIdentifierHandler.service == []:
        return False
    else:
        return True
    
def _read_yaml_data(yaml_file='doip_data_identifier.yaml'):
    data = read_config_data(yaml_file)
    DataIdentifierHandler.session = [x for x in data["ActiveDiagnosticSession"]["session"]]
    DataIdentifierHandler.security_service = int(data["ActiveDiagnosticSession"]["security_service"])
    
def _check_session_supported():
    return (DoIPState.current_session in DataIdentifierHandler.session)
    
def _check_security_access():
    return True if DataIdentifierHandler.security_service == 0x00 else \
        (DataIdentifierHandler.security_service == DoIPState.security_unlocked)

def _doip_data_identifiers_handler(did, sid):

    DataIdentifierHandler.reset_session_details()        
    
    if _is_request_out_of_range(did, sid):
    
        _read_yaml_data()
        
        if _check_session_supported():
            
            if  _check_security_access():
                
                response = _doip_data_identifier_factory(
                                    DataIdentifierHandler.service[0],
                                    DataIdentifiersFactoryMethods.response.value
                                    )
                
            else:
                response = DoIPState.nrc(sid, DiagnosticsNRC.SECURITY_ACCESS_DENIED.value)
                
        else:
                response = DoIPState.nrc(sid, DiagnosticsNRC.SERVICE_NOT_SUPPORTED_IN_THE_ACTIVE_SESSION.value)
    else:
        response = DoIPState.nrc(sid, DiagnosticsNRC.REQUEST_OUT_OF_RANGE.value)

    return response

print(_doip_data_identifiers_handler(0xf186, 0x22).hex())
print('')

print(_doip_data_identifiers_handler(0xf186, 0x23).hex())
print('')

print(_doip_data_identifiers_handler(0xf199, 0x22).hex())
print('')