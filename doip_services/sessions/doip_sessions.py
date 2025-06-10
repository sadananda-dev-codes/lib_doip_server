import struct
from dataclasses import dataclass
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticLayerEnum

@dataclass
class DiagSessionResponse:
    sub_function: int
    nrc: int
    service_id: int = 0x50
    keep_alive: int = 0x32
    timeout: int = 0x1388
    negative_response = 0x7F

    def to_bytes(self) -> bytes:
        if not self.nrc:
            return struct.pack(
                            '!BBHH',
                               self.service_id + DiagnosticLayerEnum.POSITIVE_RESPONSE_CODE ,
                               self.sub_function,
                               self.keep_alive,
                               self.timeout
                            )
        else:
            return struct.pack(
                        '!BBB',
                               self.negative_response,
                               self.service_id,
                               self.nrc
                                )

class DiagnosticSession:

    def __init__(self,
                 *,
                 sub_function: int = 0,
                 nrc: int = 0):
        self.response = DiagSessionResponse(
            sub_function=sub_function,
            nrc = nrc
        )

    def response(self) -> bytes:
        return self.response.to_bytes()