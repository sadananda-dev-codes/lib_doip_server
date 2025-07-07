from dataclasses import dataclass
from typing import ClassVar
from enum import IntEnum

class SecurityKey(IntEnum):
    SECURITY_SERVICE_LOCKED = 0
    SECURITY_SERVICE_LEVEL_ONE = 1
    SECURITY_SERVICE_LEVEL_ELEVEN = 11
    
@dataclass
class SecurityServiceUtils:
    
    is_security_key_unlocked = 0
    is_security_service_supported = SecurityKey.SECURITY_SERVICE_LOCKED
    
    security_service_timer:ClassVar[int] = 10
    security_service_max_retries:ClassVar[int] = 2
    
    @property
    def is_security_key_unlocked(self):
        return self._is_security_key_unlocked
    
    @property
    def is_security_service_supported(self):
        return self._is_security_service_supported
    
    def lock_security_service(self):
        self.is_security_key_unlocked = SecurityKey.SECURITY_SERVICE_LOCKED
        
    def unlock_security_service(self, security_service_unlock_level):
        self.is_security_key_unlocked = security_service_unlock_level
    