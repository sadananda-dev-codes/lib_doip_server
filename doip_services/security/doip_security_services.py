import random
import struct
from functools import wraps
from abc import ABCMeta,  abstractmethod

from doip_services.security.doip_security_service_util import security_util , SecurityKeyEnum
from doip_services.security.doip_security_service_key import yield_keys
from doip_diagnostic_session.doip_diagnostic_layer import *

def generate_seed():
        return random.randint(1, 0xFF)
class SecurityAccessSingleton(ABCMeta):
    
    def __call__(cls, *args, **kwds):
        if not hasattr(cls, '_instance'):
            cls._instance =  super().__call__(*args, **kwds)
        return cls._instance
class SecurityService(metaclass=SecurityAccessSingleton):
    service_id = 0x27
    subfunction = 0
    
    @abstractmethod
    def request(self):     
        pass
        
    @abstractmethod
    def response(self):
        pass        

def decorate_seed(response_seed):  
    
    @wraps(response_seed)      
    def wrapper_seed(self):
    
        if security_util.NRC == DiagnosticsNRC.EXCEEDED_NUMBER_OF_ATTEMPTS.value:
            return response_seed(self)
        
        seeds = []

        for i in range(self._no_of_seeds):
            seed_value = 0 if not security_util.is_security_key_unlocked and security_util.is_seed_requested else generate_seed()
            seeds.append(seed_value)
            if sum(seeds) == 0:
                security_util.is_seed_requested = 1
            security_util.NRC = 0
        setattr(self, '_seeds', seeds)
        
        return response_seed(self)
    return wrapper_seed
class SecurityServiceLevelOneSeed(SecurityService):

    subfunction = 0x1
    _no_of_seeds = 3
    
    def request(self):     

        if security_util.NRC == DiagnosticsNRC.EXCEEDED_NUMBER_OF_ATTEMPTS.value:
            security_util.NRC = DiagnosticsNRC.REQUIRED_TIME_DELAY_HAS_NOT_EXPIRED.value
            return struct.pack('!BBB', 0x7F, self.service_id, security_util.NRC)
        else:   
            return struct.pack('!BB',self.service_id, self.subfunction)
    
    @decorate_seed
    def response(self):
        return struct.pack(
                    '!BBBBB', 
                    self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                    self.subfunction,
                    *self._seeds
                    )       
    
def decorate_key(key_request):    

    @wraps(key_request)
    def wrapper_key(self, _keys):        

        if (not security_util.is_seed_requested) and (security_util.is_security_key_unlocked):
            security_util.NRC = DiagnosticsNRC.REQUEST_SEQUENCE_ERROR.value
        else:
            key_values = 0 if security_util.is_security_key_unlocked else yield_keys(SecurityServiceLevelOneSeed()._seeds)
            setattr(self, f'_keys', key_values)
        
        return key_request(self, _keys)
        
    return wrapper_key

class SecurityServiceLevelOneKey(SecurityService):

    subfunction = 0x2
    
    def response(self):
        if security_util.NRC:
            return struct.pack(
                        '!BBB', 
                        0x7F,
                        self.service_id, 
                        security_util.NRC
                        )
        else:
            if not security_util._is_security_key_unlocked:
                security_util.unlock_security_service()
                return struct.pack(
                            '!BB',
                            self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                            self.subfunction
                            )
            else:
                self.request([])
    
    @decorate_key
    def request(self, _keys:list):   
        
        if security_util.NRC == DiagnosticsNRC.REQUEST_SEQUENCE_ERROR.value:
            return self.response()
        
        if security_util.NRC == DiagnosticsNRC.EXCEEDED_NUMBER_OF_ATTEMPTS.value:
            security_util.NRC = DiagnosticsNRC.REQUIRED_TIME_DELAY_HAS_NOT_EXPIRED.value
            security_util.start_security_timer()
            return self.response()
        
        if security_util.is_security_key_unlocked:
            security_util.NRC = DiagnosticsNRC.REQUEST_SEQUENCE_ERROR.value
            return self.response()
        
        if security_util.NRC == DiagnosticsNRC.REQUIRED_TIME_DELAY_HAS_NOT_EXPIRED.value:
            return self.response()
        
        if security_util.security_service_cur_retries >= SecurityKeyEnum.SECURITY_SERVICE_MAX_ATTEMPTS.value:   
            security_util.NRC = DiagnosticsNRC.EXCEEDED_NUMBER_OF_ATTEMPTS.value 
            return self.response()        
        
        if tuple(self._keys) == tuple(_keys):
            print(f'{_keys=} {self._keys=}')    
            security_util.is_seed_requested = 1
            security_util.NRC = 0
        else:
            security_util.security_service_cur_retries =1
            security_util.NRC = DiagnosticsNRC.INVALID_KEY.value 
        
        return self.response()
                        
sed = SecurityServiceLevelOneSeed()
ke = SecurityServiceLevelOneKey()

print('seed request', sed.request().hex())
print('seed response', sed.response().hex())
#print('key response', ke.response().hex())
print('once',ke.request([32, 85, 65]).hex())
print('twice',ke.request([32, 85, 65]).hex())
print('thrice',ke.request([32, 85, 65]).hex())
print('four',ke.request([32, 85, 65]).hex())
print('five',ke.request([32, 85, 65]).hex())
print('six',ke.request([32, 85, 65]).hex())
print('seven',ke.request([32, 85, 65]).hex())

import time 
for i in range(15):
    time.sleep(1)
    print('eight',ke.request([32, 85, 65]).hex())

time.sleep(10)
print('one last request')
print(sed.response().hex())
seeds = sed._seeds
keys = yield_keys(seeds)
print(ke.request(keys).hex())