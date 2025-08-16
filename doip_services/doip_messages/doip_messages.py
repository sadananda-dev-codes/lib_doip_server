from types import MappingProxyType
import struct
from abc import abstractmethod
from enum import IntEnum

from doip_message_util import DoipHeaderEnum

class DoipMessage:
    
    __hdr__ = {
            'protocol_version_version': DoipHeaderEnum.PROTOCOL_VERSION.value,
            'inverse_protocol_version': DoipHeaderEnum.INVERSE_PROTOCOL_VERSION.value,
            '_payload_type': 0, 
            '_payload_length':0, 
        }
    
    __hdr__fmt__ = '!BBHI'
    
    @abstractmethod
    def _pack_payload(self):
        pass
    
    @property
    def payload_length(self):
        return self._payload_length
    
    @property
    def payload_type(self):
        return self._payload_type
        
    @payload_length.setter
    def payload_length(self, _payload_length):
        self._payload_length = _payload_length
        return self._payload_length
    
    @payload_type.setter
    def payload_type(self, _payload_type):
        self._pack_type = _payload_type
    
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
            
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 


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
        return struct.pack(
                        self.__payload_fmt__,
                        self.source_address, 
                        self.target_address, 
                        self.ack_code
                        )
    
    def __init__(
                self, 
                source_address = DoipHeaderEnum.SOURCE_ADDRESS.value,
                target_address = DoipHeaderEnum.TARGET_ADDRESS.value,
                ack=0x00
                ):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.source_address = source_address
        self.target_address = target_address
        self.ack_code = ack
        
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
class DiagnosticMessageNegResponse:
    
    __payload_fmt__ = '!HHB'
    
    def _pack(self):
        return struct.pack(
                    
                        self.__payload_fmt__,
                        self.source_address,
                        self.target_address,
                        self._nrc
                    )
    
    def __init__(
            self, source_address = DoipHeaderEnum.SOURCE_ADDRESS.value,
            target_address = DoipHeaderEnum.TARGET_ADDRESS.value,
            nrc=0x00
            ):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self.source_address = source_address
        self.target_address = target_address
        self._nrc = nrc
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
    
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

    def __init__(
                self,
                node_type = NodeType.DOIP_NODE,
                max_concurrent_sockets = 1,
                currently_opened_sockets = 0,
                max_data_size = None
                ):
        
        self._node_tpe = node_type
        self._max_concurrent_sockets = max_concurrent_sockets
        self._currently_opened_sockets = currently_opened_sockets
        self._max_data_size = max_data_size
        
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
    
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
        
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
        
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
                source_address = DoipHeaderEnum.SOURCE_ADDRESS.value
                ):
        self.source_address = source_address
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
            
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
    
class VehicleIdentificationRequest(DoipMessage):
    __payload_fmt__ = ''
    
    def _pack_payload(self):
        return struct.pack('')
class VehicleIdentificationResponse(DoipMessage):
    
    __payload_fmt__ = '!17BH6B6BBB'
    
    def _pack_payload(self):
            return struct.pack(
                self.__payload_fmt__,
                *self._vin,
                self._logical_address,
                *self._eid,
                *self._gid,
                self._further_action_required,
                self._sync_status,
            )    
    
    @property
    def vin(self):
        return self._vin
    
    @property
    def logical_address(self):
        return self._logical_address
    
    @property
    def eid(self):
        return self._eid
    
    @property
    def gid(self):
        return self._gid
    
    @property
    def sync_status(self):
        return self._sync_status
    
    @property
    def further_action_required(self):
        return self._further_action_required
    
    def __init__(
                self,
                vin = DoipHeaderEnum.VIN.value,
                logical_address = DoipHeaderEnum.TARGET_ADDRESS.value,
                eid = DoipHeaderEnum.EID.value,
                gid = DoipHeaderEnum.GID.value,
                further_action_required = 0x00,
                sync_status = 0x00
                ):
        
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
        
        self._vin = vin
        self._logical_address = logical_address
        self._eid = eid
        self._gid = gid
        self._further_action_required = further_action_required
        self._sync_status = sync_status
        
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 
        
class VehicleIdentificationRequestWithVin(DoipMessage):
    
    __hdr__fmt__ = '!BBHI'

    def _pack_payload(self):
        return struct.pack('17B',*self.vin)
    
    @property
    def vin(self):
        return self._vin
    
    @vin.setter
    def vin(self, value):
        if isinstance(value, (bytes, bytearray)):
            if len(value) != 17:
                raise ValueError("VIN must be exactly 17 bytes")
            self._vin = list(value)
        elif isinstance(value, list) and len(value) == 17:
            self._vin = value
        else:
            raise ValueError("VIN must be a list of 17 bytes or a bytes object")
    
    def __init__(self, vin=DoipHeaderEnum.VIN.value):
        
        self._vin = vin
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
            
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 

class VehicleIdentificationRequestWithEid(DoipMessage):
    
    __hdr__fmt__ = '!BBHI'
    
    def _pack_payload(self):
        return struct.pack('!6B', *self.eid)

    @property
    def eid(self):
        return self._eid
    
    @eid.setter
    def eid(self, value):
        if isinstance(value, (bytes, bytearray)):
            if len(value) != 17:
                raise ValueError("EID must be exactly 17 bytes")
            self._eid = list(value)
        elif isinstance(value, list) and len(value) == 17:
            self._eid = value
        else:
            raise ValueError("EID must be a list of 17 bytes or a bytes object")
    
    def __init__(self, eid=DoipHeaderEnum.EID.value):
        self._eid = eid
    
        for attrs, value in self.__hdr__.items():
            setattr(self, attrs, value)
            
        self._payload_length  = len(self._pack_payload())
        self._payload_type = self.payload_type = doip_message_to_payload_type[self.__class__] 

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
byte_data = bytes.fromhex(dpm.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

dpm = DiagnosticPowerModeInfoResponse(0x01)
byte_data = bytes.fromhex(dpm.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

alive_check_request = AliveCheckRequest()
byte_data = bytes.fromhex(alive_check_request.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

alive_check_response = AliveCheckResponse(0x11)
byte_data = bytes.fromhex(alive_check_response.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

diaack = DiagnosticMessageAck()
byte_data = bytes.fromhex(diaack.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

res = VehicleIdentificationResponse()
byte_data = bytes.fromhex(res.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

vvin = VehicleIdentificationRequestWithVin()
byte_data = bytes.fromhex(vvin.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))

veid = VehicleIdentificationRequestWithEid()
byte_data = bytes.fromhex(veid.request().hex())
print(' '.join(f'{b:02x}' for b in byte_data))