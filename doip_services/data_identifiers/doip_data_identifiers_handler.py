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
    service = None
    session = []
    security_service = 0x00
    response = None
    conditions = None
    sequence = None
    
    @classmethod
    def reset_session_details(cls):
        cls.service = None
        cls.session.clear()
        cls.response = None
        cls.security_service = 0x00
        cls.conditions = None
        cls.sequence = None
        

def _load_data_identifier(_did, sid=0x22):
    
    data_identifiers = read_data_by_identifiers.items() if sid==0x22 else write_data_by_identifiers.items() if sid==0x2E else []
    
    for service, did in data_identifiers:
        read_did = did[0]
        read_did = (read_did << 8 | did[1])
        if _did == read_did:
            DataIdentifierHandler.service = service
    
def _read_yaml_data(yaml_file='doip_data_identifier.yaml'):
    
    data = read_config_data(yaml_file)
    DataIdentifierHandler.session = [x for x in data[DataIdentifierHandler.service]["session"]]
    DataIdentifierHandler.security_service = int(data[DataIdentifierHandler.service]["security_service"])
    DataIdentifierHandler.conditions = int(data[DataIdentifierHandler.service]["conditions"])
    DataIdentifierHandler.sequence = int(data[DataIdentifierHandler.service]["sequence"])

def _nrc_31_request_out_of_range(did, sid=0x22):
    
    if  DataIdentifierHandler.service == None:
        return False
    else:
        return True
    
def _nrc_7F_check_session_supported():
    return (DoIPState.current_session in DataIdentifierHandler.session)
    
def _nrc_33_check_security_access():
    return True if DataIdentifierHandler.security_service == 0x00 else \
        (DataIdentifierHandler.security_service == DoIPState.security_unlocked)

def _nrc_22_conditions_not_correct():
    return DataIdentifierHandler.conditions == 0x00
    
def _nrc_24_incorrect_sequence():
    return DataIdentifierHandler.conditions == 0x00

def _doip_data_identifiers_handler(did, sid):

    DataIdentifierHandler.reset_session_details()        
    _load_data_identifier(did, sid)
    
    if _nrc_31_request_out_of_range(did, sid):
        
        _read_yaml_data()
        
        if _nrc_7F_check_session_supported():
            
            if  _nrc_33_check_security_access():
                
                if _nrc_22_conditions_not_correct():
                    
                    if _nrc_24_incorrect_sequence():
                        
                        DataIdentifierHandler.response = _doip_data_identifier_factory(
                                    DataIdentifierHandler.service,
                                    DataIdentifiersFactoryMethods.response.value
                                    )
                    else:
                        DataIdentifierHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SECURITY_ACCESS_DENIED.value)        
                else:
                    DataIdentifierHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SECURITY_ACCESS_DENIED.value)
            else:
                DataIdentifierHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SECURITY_ACCESS_DENIED.value)
        else:
                DataIdentifierHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SERVICE_NOT_SUPPORTED_IN_THE_ACTIVE_SESSION.value)
    else:
        DataIdentifierHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.REQUEST_OUT_OF_RANGE.value)

    if DataIdentifierHandler.response == None:
        raise ValueError('Invalid Response')
    else:
        return DataIdentifierHandler.response

print(_doip_data_identifiers_handler(0xf186, 0x22).hex())
print('')

print(_doip_data_identifiers_handler(0xf186, 0x23).hex())
print('')

print(_doip_data_identifiers_handler(0xf199, 0x22).hex())
print('')

print(_doip_data_identifiers_handler(0xf190, 0x22).hex())
print('')

print('Sadananda Maharaj')
print(_doip_data_identifiers_handler(0xDD00, 0x2E).hex())
print('')

print(_doip_data_identifiers_handler(0xDD32, 0x2E).hex())
print('')

print(_doip_data_identifiers_handler(0xDD85, 0x2E).hex())
print('')

print(_doip_data_identifiers_handler(0xDD56, 0x2E).hex())
print('')

print(_doip_data_identifiers_handler(0xDD51, 0x2E).hex())
print('')