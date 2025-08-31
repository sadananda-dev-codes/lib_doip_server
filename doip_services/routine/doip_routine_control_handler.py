from src.lib_doip_server.doip_services.routine.doip_routine_control_util import routine_control_identifiers,RoutineControlIdentifiersFactoryMethods
from src.lib_doip_server.configs.read_yaml import *
from src.lib_doip_server.configs.doip_sessions_status import DoIPState
from src.lib_doip_server.doip_services.routine.doip_routine_control_factory import _doip_routine_identifier_factory
from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticsNRC

class RoutineControlHandler:
    service = None
    session = None
    security_service = 0x00
    response = None
    
    @classmethod
    def reset_session_details(cls):
        cls.service = None
        cls.session = None
        cls.response = None
        cls.security_service = 0x00
        

def _load_routine_identifier(_routine_id, sid=0x31):
    
    routine_identifiers = routine_control_identifiers.items()
    
    for routine_service, routine_id in routine_identifiers:    
        if _routine_id == routine_id:
            RoutineControlHandler.service = routine_service

def _is_request_out_of_range(_routine_id, sid=0x31):
    
    _load_routine_identifier(_routine_id, sid)
    
    if  RoutineControlHandler.service == None:
        return False
    else:
        return True
    
def _read_yaml_data(yaml_file='doip_routine_identifier.yaml'):
    data = read_config_data(yaml_file)
    
    RoutineControlHandler.session = data[RoutineControlHandler.service]['session']
    RoutineControlHandler.security_service = int(data[RoutineControlHandler.service]['security_service'])
    
def _check_session_supported():
    return (DoIPState.current_session in RoutineControlHandler.session)
    
def _check_security_access():
    return True if RoutineControlHandler.security_service == 0x00 else \
        (RoutineControlHandler.security_service == DoIPState.security_unlocked)

def _doip_routine_control_identifiers_handler(_rid, sid):

    RoutineControlHandler.reset_session_details()        
    
    if _is_request_out_of_range(_rid, sid):
    
        _read_yaml_data()
        
        if _check_session_supported():
            
            if  _check_security_access():
                
                RoutineControlHandler.response = _doip_routine_identifier_factory(
                                    RoutineControlHandler.service[0],
                                    RoutineControlIdentifiersFactoryMethods.response.value
                                    )
                
            else:
                RoutineControlHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SECURITY_ACCESS_DENIED.value)
                
        else:
                RoutineControlHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.SERVICE_NOT_SUPPORTED_IN_THE_ACTIVE_SESSION.value)
    else:
        RoutineControlHandler.response = DoIPState.nrc(sid, DiagnosticsNRC.REQUEST_OUT_OF_RANGE.value)

    if RoutineControlHandler.response == None:
        raise ValueError('Invalid Response')
    else:
        return RoutineControlHandler.response

'''
print(_doip_routine_control_identifiers_handler(0xf186, 0x31).hex())
print('')

print(_doip_routine_control_identifiers_handler(0xf186, 0x31).hex())
print('')

print(_doip_routine_control_identifiers_handler(0xf199, 0x22).hex())
print('')
'''


print(_doip_routine_control_identifiers_handler((0x05, 0x94, 0x76, 0x00), 0x31).hex())
print('')

print(_doip_routine_control_identifiers_handler((0x02, 0x03), 0x22).hex())
print('')