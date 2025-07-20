import struct
from abc import abstractmethod
from enum import IntEnum

from doip_message_util import DoipHeaderEnum

class DoipMessage():
    
    __hdr__ = {
            'protocol_version_version': DoipHeaderEnum.PROTOCOL_VERSION,
            'inverse_protocol_version': DoipHeaderEnum.INVERSE_PROTOCOL_VERSION,
            'payload_type': 0, 
            'payload_length':0, 
            }
    
    @abstractmethod
    def _pack():
        pass
    
    @abstractmethod
    def _unpack():
        pass
    
    @abstractmethod
    def request():
        pass
    
    @abstractmethod
    def response():
        pass        

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
    
    def __init__(self):
        pass   
    
class RoutingActivationResponse:
    pass

class DiagnosticMessage:
    pass

class DiagnosticMessageAck:
    pass
    
class DiagnosticMessageNegResponse:
    pass    
    
class EntityStatusRequest:
    pass

class EntityStatusResponse:
    pass
    
class DiagnosticPowerModeInfoRequest:
    pass
    
class DiagnosticPowerModeInfoResponse:
    pass
    
class AliveCheckRequest:
    pass
    
class AliveCheckResponse:
    pass
    
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

routing_activation_request = RoutingActivationRequest()
routing_activation_request._pack()