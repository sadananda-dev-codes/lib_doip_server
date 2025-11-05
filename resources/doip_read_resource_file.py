import yaml
from pprint import pprint

# Path to your YAML file
YAML_PATH = "doip_diagnostics_services_resource.yaml"  # change this to your actual file path

with open(YAML_PATH, 'r') as file:
    uds_data = yaml.safe_load(file)

# Display the data structure nicely
#pprint(uds_data)

'''
for sid in uds_data.values():
    print(sid)
    print('')
    print(sid[0]['service-id'])
    print(type(sid[0]['service-id']))
'''
'''
class JsonFileReader(ResourceReader):
    pass
class YamlResourceReader(ResourceReader):
    pass
'''
class SingletonSessions(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

def build_sessions_factory(read=False, file_name="doip_diagnostics_services_resource.yaml"):

    def build_session_outer(fun):

        def build_session_inner(request, sid_requested, uds_data=None):
            
            service_details = None
            
            if not read:
                with open(file_name, 'r') as file:
                    service_details = yaml.safe_load(file)
            
            for sid in service_details.values():
                if sid_requested in sid[0]['service-id'].keys():
                    uds_data = sid[0]

            return fun(request, sid_requested, uds_data)
            
        return build_session_inner
    
    return build_session_outer
class UdsSession(metaclass=SingletonSessions):
    
    def __init__(self):
        self.service_name = None
        self.service_id = None
        self.sessions_supported = {}
        self.subfunctions_supported = {}
        self.security_access = {}
        self.security_level = {}
        
    def update_service_id(self, id):
        self.service_id = id
        
    def update_service_name(self, name):
        self.name = name
            
    def update_sessions_supported(self, sessions):
        self.sessions_supported = sessions
    
    def update_subfunctions(self, subfunctions):
        self.subfunctions_supported = subfunctions
    
    def update_security_access(self, security_access):
        self.security_access = security_access
    
    def update_security_level(self, security_level):
        self.security_level = security_level
        
    def is_session_supported(self, _key):
        return _key in self.sessions_supported.keys()
    
    def is_security_access_required(self, _key):
        return self.security_access[_key] == 'YES'
    
    def is_subfunction_supported(self, _key):
        return _key in self.subfunctions_supported.keys()
    
    def get_security_level_required_to_unlock(self, _key):
        return self.security_level[_key]                           
class DiagnosticSessions(UdsSession):
    service_id = 0x10
    sub_function_byte_len = 1
class ReadDataByIdentifier(UdsSession):
    service_id = 0x22
    sub_function_byte_len = (2,)
class WriteDataByIdentifier(UdsSession):
    service_id = 0x2E
    sub_function_byte_len = (2,)
class SecurityAccessRequest(UdsSession):
    service_id = 0x27
    sub_function_byte_len = (1,)
class EcuReset(UdsSession):
    service_id = 0x11
    sub_function_byte_len = (1,)
class RoutineControl(UdsSession):
    service_id = 0x31

sessions = {
    
        0x10: DiagnosticSessions(),
        0x11: EcuReset(), 
        0x22: ReadDataByIdentifier(),
        0x2E: WriteDataByIdentifier(), 
        0x27: SecurityAccessRequest()
    }
    
@build_sessions_factory(read=False)
def UdsServiceParser(request, sid, uds_data=None):
    
    def session_details(
                        diagnostic_request_value,
                        diagnostic_request_field
                    ):
            
            yield diagnostic_request_value if diagnostic_request_value in uds_data[diagnostic_request_field].keys() else None
    
    return session_details
    
    
'''
    # check service in services
    session_details['service-id']   = sid if sid in uds_data['service-id'].keys() else False 
    
    # check sub function in services
    session_details['sub-functions']   = 0x01 if 0x01 in uds_data['sub-functions'].keys() else False 
    
    # check session supported
    session_details['security-access-required']   = 0x01 if 0x01 in uds_data['security-access-required'].keys() else False 

    # check security service required
    session_details['session-supported']   = 0x01 if 0x01 in uds_data['session-supported'].keys() else False 
    
    # check security service un locked
    session_details['security-level']   = 0x01 if 0x01 in uds_data['security-level'].keys() else False 
'''


session_details = {
                'service-id': None,
                'sub-functions': None,
                'session-supported': None,
                'security-access-required': None,
                'security-level': None
            }

sadananda = UdsServiceParser('0x10 01', 0x10)

for val in session_details.keys():
    session_details[val] = sadananda(val)

print('')
print(session_details)