import struct
from lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticServices

class ECUReset:

    service_id = 0x11

    @classmethod
    def request(cls) -> bytes:
        return struct.pack('!BB', cls.service_id, cls.sub_function)

    @classmethod
    def response(cls):
        return struct.pack('!BB', cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, cls.sub_function)

class ECUSoftReset(ECUReset):
    sub_function = 0x01

class ECUHardReset(ECUReset):
    sub_function = 0x02

class ECUKeyOnOffReset(ECUReset):
    sub_function = 0x03

e = ECUSoftReset()
data = e.request()
print(" ".join(f"{b:02x}" for b in data))
data = e.response()
print(" ".join(f"{b:02x}" for b in data))

e = ECUHardReset()
data = e.request()
print(" ".join(f"{b:02x}" for b in data))
data = e.response()
print(" ".join(f"{b:02x}" for b in data))

e = ECUKeyOnOffReset()
data = e.request()
print(" ".join(f"{b:02x}" for b in data))
data = e.response()
print(" ".join(f"{b:02x}" for b in data))
