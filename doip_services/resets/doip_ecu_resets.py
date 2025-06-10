import struct
from dataclasses import dataclass
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticLayerEnum

@dataclass
class ECUResetResponse:
    sub_function: int
    service_id: int = 0x11

    def to_bytes(self) -> bytes:
        return struct.pack('!BB', self.service_id + DiagnosticLayerEnum.POSITIVE_RESPONSE_CODE, self.sub_function)

class ECUReset:

    def __init__(self,
                 *,
                 sub_function: int):
        self.response = ECUResetResponse(
            sub_function=sub_function
        )

    def response(self) -> bytes:
        return self.response.to_bytes()