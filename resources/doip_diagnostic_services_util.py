class DiagnosticServicesUtil:


    __sessions = {}
    __routines = {}
    __data_identifiers = {}
    __routines = {}
    __security_access = {}
    __ecu_resets = {}

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, '_instance'):
            cls._instance = super(DiagnosticServicesUtil, cls).__new__(cls)
        return cls._instance

    def load_yaml_configuration(self):
        pass

    def get_diagnostic_sessions(self):
        pass
    
    def get_diagnostic_session_subfunctions(self):
        pass