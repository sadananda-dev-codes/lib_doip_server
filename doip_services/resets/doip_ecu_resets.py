import struct
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices

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
print(e.request().hex())
print(e.response().hex())

e = ECUHardReset()
print(e.request().hex())
print(e.response().hex())

e = ECUKeyOnOffReset()
print(e.request().hex())
print(e.response().hex())


