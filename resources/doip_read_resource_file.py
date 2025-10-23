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

def build_sessions_factory(read=False, sid=0x00, file_name="doip_diagnostics_services_resource.yaml"):

    def build_session_outer(fun):

        def build_session_inner(self):
            
            uds_data = None
            
            if not read:
                with open(YAML_PATH, 'r') as file:
                    uds_data = yaml.safe_load(file)
                    
            fun(sid, uds_data[sid])
            
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
    

class UdsSrviceBuilder:

    ## TODO
    
    @staticmethod
    def build_service():
        pass
    # expose to decorator
    
    # check service in services
    
    # check sub function in services
    
    # check session supported
    
    # check security service required
    
    # check security service un locked
    

e = EcuReset().update_service_details()
f = SecurityAccessRequest().update_service_details()
g = ReadDataByIdentifier().update_service_details()

print(f'{e=} {f=} {g=}')