import struct
from abc import abstractmethod
from enum import IntEnum

from doip_message_util import DoipHeaderEnum

class DoipMessage:
    
    __hdr__ = {
            'protocol_version_version': DoipHeaderEnum.PROTOCOL_VERSION.value,
            'inverse_protocol_version': DoipHeaderEnum.INVERSE_PROTOCOL_VERSION.value,
            'payload_type': 0, 
            'payload_length':0, 
            }
    
    __hdr__fmt__ = '!BBHI'
    
    @abstractmethod
    def _pack_payload(self):
        pass
    
    @abstractmethod
    def _pack(self):
        pass
            
    @abstractmethod
    def _unpack(self):
        pass
    
    def request(self):
        return self._pack()
    
    def response(self):
        return self._pack()        

    def __init__(self):
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)

class RoutingActivationRequest:
    
    _fields = ["source_address", "activation_type", "reserved", "vm_specific"]
    
    class ActivationType(IntEnum):
        """See Table 47 - Routing activation request activation types"""

        Default = 0x00
        DiagnosticRequiredByRegulation = 0x01
        CentralSecurity = 0xE1
    
    def _pack(self):
        print(doip_message_to_payload_type[RoutingActivationRequest])
        self._fields
        return struct.pack('!BBB', )
    
    def _unpack(self):
        return 
    
    def request(self):
        return        
    
class RoutingActivationResponse:
    pass

class DiagnosticMessage:
    pass

class DiagnosticMessageAck(DoipMessage):
    
    def _pack_payload(self):
        return struct.pack('!HHB', self.source_address, 
                        self.target_address, 
                        self.ack_code, )
        
    def _pack(self):
        self.payload_type = doip_message_to_payload_type[DiagnosticMessageAck]
        payload_bytes =  self._pack_payload()
        self.payload_length = len(payload_bytes)
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length
                        ) + payload_bytes
    
    def response(self):
        return self._pack()
    
    def __init__(self, source_address = DoipHeaderEnum.SOURCE_ADDRESS.value,
                target_address = DoipHeaderEnum.TARGET_ADDRESS.value,
                ack=0x00):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.source_address = source_address
        self.target_address = target_address
        self.ack_code = ack
class DiagnosticMessageNegResponse:
    pass    
    
class EntityStatusRequest:
    def _pack_payload(self):
        return struct.pack('')
    
    def _pack(self):
        self.payload_type = doip_message_to_payload_type[DiagnosticPowerModeInfoRequest]
        payload_bytes =  self._pack_payload()
        self.payload_length = len(payload_bytes)
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length
                        ) + payload_bytes
    
    def request(self):
        return self._pack()    
    
class EntityStatusResponse:
    pass
    
class DiagnosticPowerModeInfoRequest(DoipMessage):
    
    def _pack_payload(self):
        return struct.pack('')
    
    def _pack(self):
        self.payload_type = doip_message_to_payload_type[DiagnosticPowerModeInfoRequest]
        payload_bytes =  self._pack_payload()
        self.payload_length = len(payload_bytes)
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length
                        ) + payload_bytes
    
    def request(self):
        return self._pack()    
class DiagnosticPowerModeInfoResponse(DoipMessage):
    
    def _pack_payload(self):
        return struct.pack('!B',self.power_mode)
    
    def _pack(self):
        self.payload_type = doip_message_to_payload_type[DiagnosticPowerModeInfoResponse]
        payload_bytes =  self._pack_payload()
        self.payload_length = len(payload_bytes)
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length                    
                        ) + payload_bytes
                        
    def response(self):
        return self._pack()    
    
    def __init__(self, power_mode):
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        self.power_mode = power_mode
    
class AliveCheckRequest(DoipMessage):
    
    def _pack_payload(self):
        return struct.pack('')
    
    def _pack(self):
        self.payload_type = doip_message_to_payload_type[AliveCheckRequest]
        payload_bytes =  self._pack_payload()
        self.payload_length = len(payload_bytes)
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length                    
                        ) + payload_bytes
                        
    def request(self):
        return self._pack() 
        
class AliveCheckResponse(DoipMessage):
    
    def _pack_payload(self):
        
        return struct.pack('!BBBL', self.node_tpe,
                    self.max_concurrent_sockets,
                    self.currently_opened_sockets,
                    self.max_data_size)
    
    def _pack(self):
        
        self.payload_type = doip_message_to_payload_type[AliveCheckResponse]
        payload_bytes =  self._pack_payload()
        
        print(self.payload_length, payload_bytes)
        
        self.payload_length = len(payload_bytes)
        
        return struct.pack(
                        self.__hdr__fmt__, self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length                    
                        ) + payload_bytes
                        
    def response(self):
        return self._pack()
    
    def __init__(self, 
                node_tpe, 
                max_concurrent_sockets,
                currently_opened_sockets,
                max_data_size):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.node_tpe = node_tpe
        self.max_concurrent_sockets = max_concurrent_sockets
        self.currently_opened_sockets = currently_opened_sockets
        self.max_data_size = max_data_size
    
class VehicleIdentificationRequest:
    pass

class VehicleIdentificationResponse:
    pass
    
class VehicleIdentificationRequestWithVin:
    pass
    
class VehicleIdentificationRequestWithEid:
    pass

doip_message_to_payload_type = {
    RoutingActivationRequest: 0x0005,
    RoutingActivationResponse: 0x0006,
    DiagnosticMessage: 0x8001,
    DiagnosticMessageAck: 0x8002,
    DiagnosticPowerModeInfoRequest: 0x4003,
    DiagnosticPowerModeInfoResponse: 0x4004,
    AliveCheckRequest: 0x0007,
    AliveCheckResponse: 0x0008,
    VehicleIdentificationRequest: 0x0001,
    VehicleIdentificationRequestWithEid: 0x0002,
    VehicleIdentificationRequestWithVin: 0x0003,
    VehicleIdentificationResponse: 0x0004
    
    }

doip_payload_type_to_message = {
    payload_type : payload_message for payload_message, payload_type in doip_message_to_payload_type.items()
}

#routing_activation_request = RoutingActivationRequest()
#routing_activation_request._pack()

dpm = DiagnosticPowerModeInfoRequest()
print(dpm.request().hex())

dpm = DiagnosticPowerModeInfoResponse(0x01)
print(dpm.request().hex())

alive_check_request = AliveCheckRequest()
print(alive_check_request.request().hex())

alive_check_response = AliveCheckResponse(0x11, 0x22, 0x33, 0x44)
print(alive_check_response.response().hex())

diaack = DiagnosticMessageAck()
print(diaack.response().hex())