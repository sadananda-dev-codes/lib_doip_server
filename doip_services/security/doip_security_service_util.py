from enum import IntEnum
import threading
import time
class SecurityKeyEnum(IntEnum):
    SECURITY_SERVICE_LEVEL_ONE = 1
    SECURITY_SERVICE_LEVEL_ELEVEN = 11
    SECURITY_SERVICE_MAX_ATTEMPTS = 4
    SECURITY_SERVICE_REQUIRED_TIME_DELAY = 10
    
class SecurityServiceUtils:
        
    _initialize = True
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if SecurityServiceUtils._initialize:
            self._is_security_key_unlocked = 0
            self._security_service_cur_retries = 0
            self._NRC = 0
            self._task = None
            self._is_seed_requested = 0
            self._is_timer_delay_expired_on = 0
            SecurityServiceUtils._initialize = False
    
    @property
    def is_seed_requested(self):
        return self._is_seed_requested
    
    @property
    def is_security_key_unlocked(self):
        return self._is_security_key_unlocked
    
    @property
    def is_security_service_supported(self):
        return self._is_security_service_supported
    
    @property
    def security_service_cur_retries(self):
        return self._security_service_cur_retries
    
    @property
    def NRC(self):
        return self._NRC
    
    @property
    def is_timer_delay_expired(self):
        return self._is_timer_delay_expired
    
    @security_service_cur_retries.setter
    def security_service_cur_retries(self, value=1):
        self._security_service_cur_retries += value
    
    @is_seed_requested.setter
    def is_seed_requested(self, value):
        self._is_seed_requested = value
    
    @NRC.setter
    def NRC(self, nrc):
        self._NRC = nrc
    
    @is_timer_delay_expired.setter
    def is_timer_delay_expired(self, value):
        self._is_timer_delay_expired = value
        
    def start_security_timer(self):
        worker = TimedWorkerThread(SecurityKeyEnum.SECURITY_SERVICE_REQUIRED_TIME_DELAY.value)
        worker.start()
            
    def lock_security_service(self):
        self._is_security_key_unlocked = 0
        
    def unlock_security_service(self):
        self._is_security_key_unlocked = 1
        
    def update_retr(self):
        self._security_service_cur_retries += 1
        
    def is_max_attempt_reached(self):
        return self._security_service_cur_retries >= SecurityKeyEnum.SECURITY_SERVICE_MAX_ATTEMPTS.value
    
    def reset_security_service_cur_retries(self):
        self._security_service_cur_retries = 0
class TimedWorkerThread(threading.Thread):
    def __init__(self, duration=10):
        super().__init__()
        self.duration = duration
        security_util._is_timer_delay_expired_on = 1
        self.daemon = True

    def run(self):
        time.sleep(self.duration)
        security_util._is_timer_delay_expired_on = 0
        security_util._is_seed_requested = 0
        security_util._is_security_key_unlocked = 0
        security_util.NRC = 0 
        security_util.reset_security_service_cur_retries()
        print('sadananda timer has ended')

    def get_status(self):
        return self._status

security_util = SecurityServiceUtils()

