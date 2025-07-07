import struct
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices
import random
from abc import abstractmethod
class SecurityService:
    service_id = 0x27
    subfunction_seed = 0x00
    subfunction_key = 0x00
    seed_range = (1,0xFF)
    
    def request(self , _request):
        if _request == self.subfunction_seed:
            return self._request_seed()
        
        if _request == self.subfunction_key:
            return self._request_key()
        
    def response(self , _response):
        if _response == self.subfunction_seed:
            self._generate_seed()
            return self._response_seed()
        
        if _response == self.subfunction_key:
            return self._unlock_key()
    
    def _request_seed(self) -> bytes:
        return struct.pack('!BB', self.service_id, self.sub_function)
    
    def _unlock_key(self) -> bytes:
        return struct.pack(
                        '!BB',
                        self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                        self.sub_function
                        )
    
    @abstractmethod
    def _send_key(self) -> bytes:
        pass
    
    @abstractmethod
    def _response_seed(self) -> bytes:
        pass
    
    @abstractmethod
    def _generate_seed(self):
        pass
    
class SecurityServiceLevelOne(SecurityService):
    
    def __init__(self):
        self._seed1 = 0
        self._seed2 = 0
        self._seed3 = 0
        self._key1 = 0
        self._key2 = 0
        self._key3 = 0

    def response_seed(self) -> bytes:
        return struct.pack(
                    '!BBBBB', 
                    self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                    self.sub_function
                    self._seed1,
                    self._seed2,
                    self._seed3
                    )
    
    def generate_seed(self):
        self._seed1 = random.randint(*self.seed_range)
        self._seed2 = random.randint(*self.seed_range)
        self._seed3 = random.randint(*self.seed_range)    
        
    def _send_key(self) -> bytes:
        pass
    
    def _response_key(self) -> bytes:
        pass
        
class SecurityServiceLevelEleven(SecurityService):

    def __init__(self):
        self._seed_1 = 0
        self._seed_2 = 0
        self._seed_3 = 0
        self._seed_4 = 0
        self._key_1 = 0
        self._key_2 = 0
        self._key_3 = 0
        self._key_4 = 0
        self.subfunction_request_seed = 0x03
        self.subfunction_request_unlock_key = 0x04
        
    def _request_seed(cls) -> bytes:
        return struct.pack('!BB', cls.service_id, cls.sub_function)
    
    def _response_seed(cls):
        return struct.pack('!BB', cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function)

    def generate_seed(self):
        self._seed1 = random.randint(*self.seed_range)
        self._seed2 = random.randint(*self.seed_range)
        self._seed3 = random.randint(*self.seed_range)
        self._seed4 = random.randint(*self.seed_range)
        
    def _send_key(self) -> bytes:
        pass
    
    def _response_key(self) -> bytes:
        pass