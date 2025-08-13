from src.lib_doip_server.utils_constants.doip_utils import InstantiationNotAllowedError

class DiagnosticSessionLayer:

    def __init__(self):
        raise InstantiationNotAllowedError(DiagnosticSessionLayer)

    @classmethod
    def init(cls):
        cls.__s3_server_time = 5000
        cls.__active_session = 1
        cls.__security_state = False

    @classmethod
    def reset_s3_server_time(cls):
        cls.__s3_server_time = 0

    @classmethod
    

    @classmethod
    def get_s3_server_time(cls):
        return cls.__s3_server_time

    @classmethod
    def set_s3_server_time(cls,
                           _s3_server_time):
        if cls.__s3_server_time != _s3_server_time:
            cls.__s3_server_time = _s3_server_time

    @classmethod
    def get_active_session(cls):
        return cls.__active_session

    @classmethod
    def set_active_session(cls,
                           _active_session=1):
        if cls.__active_session != _active_session:
            cls.__active_session = _active_session

    @classmethod
    def enable_security_key(cls):
        cls.__security_state = True

    @classmethod
    def disable_security_key(cls):
        cls.__security_state = False

    @classmethod
    def is_security_key_unlocked(cls):
        return True if cls.__security_state else False

