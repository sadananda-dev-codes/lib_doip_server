from types import MappingProxyType
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
    
    def get_payload_length(self):
        self.payload_length = len(self._pack_payload())
    
    def get_payload_type(self):
        self.payload_type = doip_message_to_payload_type[self.__class__]
        return self.payload_type
    
    def _pack(self):

        return struct.pack(
                        self.__hdr__fmt__, 
                        self.protocol_version_version,
                        self.inverse_protocol_version,
                        self.payload_type,
                        self.payload_length
                        ) + self._pack_payload()
            
    
    def _unpack(self):
        struct.pack('')
            
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

    __payload_fmt__ = '!HHB'
    
    def _pack_payload(self):
        return struct.pack(self.__payload_fmt__,
                        self.source_address, 
                        self.target_address, 
                        self.ack_code)
    
    def __init__(self, source_address = DoipHeaderEnum.SOURCE_ADDRESS.value,
                target_address = DoipHeaderEnum.TARGET_ADDRESS.value,
                ack=0x00):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.source_address = source_address
        self.target_address = target_address
        self.ack_code = ack
class DiagnosticMessageNegResponse:
    
    __payload_fmt__ = '!HHB'
    
    def _pack(self):
        return struct.pack(
                        self.__payload_fmt__,
                        self.source_address,
                        self.target_address,
                        self._nrc)
    
    def __init__(self, source_address = DoipHeaderEnum.SOURCE_ADDRESS.value,
                target_address = DoipHeaderEnum.TARGET_ADDRESS.value,
                nrc=0x00):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.source_address = source_address
        self.target_address = target_address
        self._nrc = nrc
    
class EntityStatusRequest:
    __payload_fmt__ = ''
    
    def _pack_payload(self):
        return struct.pack('')
    
class EntityStatusResponse:
    class NodeType:
        DOIP_GATEWAY = 0x00 
        DOIP_NODE = 0x01
        RESERVED = 0x02
        
    def pack(self):
        if self.max_data_size is None:
            return struct.pack(
                "!BBB",
                self._node_type,
                self._max_concurrent_sockets,
                self._currently_open_sockets,
            )
        else:
            return struct.pack(
                "!BBBL",
                self._node_type,
                self._max_concurrent_sockets,
                self._currently_open_sockets,
                self._max_data_size,
            )
                    
    @property
    def node_type(self):
        return self._node_tpe
    
    @property
    def max_concurrent_sockets(self):
        return self._max_concurrent_sockets
    
    @property
    def currently_opened_sockets(self):
        return self._currently_opened_sockets
    
    @property
    def max_data_size(self):
        return self._max_data_size

    def __init__(self,
                node_type = NodeType.DOIP_NODE,
                max_concurrent_sockets = 1,
                currently_opened_sockets = 0,
                max_data_size = None
                ):
        
        self._node_tpe = node_type
        self._max_concurrent_sockets = max_concurrent_sockets
        self._currently_opened_sockets = currently_opened_sockets
        self._max_data_size = max_data_size
    
class DiagnosticPowerModeInfoRequest(DoipMessage):
    
    __payload_fmt__ = ''
    
    def _pack_payload(self):
        return struct.pack('')
    
class DiagnosticPowerModeInfoResponse(DoipMessage):
    
    __payload_fmt__ = '!B'
    
    def _pack_payload(self):
        return struct.pack('!B',self.power_mode)
    
    def __init__(self, power_mode):
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        self.power_mode = power_mode
        self.payload_type = doip_message_to_payload_type[DiagnosticPowerModeInfoResponse]
        
class AliveCheckRequest(DoipMessage):
    
    __payload_fmt__ = ''
    
    def _pack_payload(self):
        return struct.pack('')
        
class AliveCheckResponse(DoipMessage):
    
    __payload_fmt__ = '!B'
    
    def _pack_payload(self):
        
        return struct.pack(
                        '!B',
                        self.source_address
                        )
    
    def __init__(self, 
                source_address
                ):
        self.source_address = source_address
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
    
class VehicleIdentificationRequest:
    __payload_fmt__ = ''
    
    def _pack_payload(self):
        return struct.pack('')

class VehicleIdentificationResponse:
    
    __payload_fmt__ = '!HHBLL'
    
    def __init__(self,
                vin,
                logical_address,
                eid,
                gid,
                further_action_required
                ):
        self._vin = vin
        self._logical_address = logical_address
        self._eid = eid
        self._gid = gid
        self._further_action_required = further_action_required
        
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

doip_message_to_payload_type= MappingProxyType(doip_message_to_payload_type)

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