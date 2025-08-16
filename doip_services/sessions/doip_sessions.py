import struct
from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer import DiagnosticLayerEnum, DiagnosticServices, DiagnosticSessionStatus

class DiagnosticSession:

    service_id = DiagnosticServices.SESSION.value
    sub_function = 0x01

    @classmethod
    def request(cls) -> bytes:
        return struct.pack(
                        '!BBHH',
                        cls.service_id,
                        cls.sub_function,
                        DiagnosticLayerEnum.P2_SERVER_INIT.value,
                        DiagnosticLayerEnum.P2_EXTENDED_SERVER_INIT.value
                        )

    @classmethod
    def response(cls)->bytes:
        return struct.pack(
                        '!BBHH',
                        cls.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                        cls.sub_function,
                        DiagnosticLayerEnum.P2_SERVER_INIT.value,
                        DiagnosticLayerEnum.P2_EXTENDED_SERVER_INIT.value
                        )

    @classmethod
    def is_active_session(cls):
        return cls.sub_function == DiagnosticSessionStatus.ACTIVE_SESSION

class DefaultSession(DiagnosticSession):
    sub_function = 0x1

class ProgrammingSession(DiagnosticSession):
    sub_function = 0x2

class ExtendedSession(DiagnosticSession):
    sub_function = 0x3

d = DefaultSession()

data = d.request()
print(" ".join(f"{b:02x}" for b in data))

data = d.response()
print(" ".join(f"{b:02x}" for b in data))

print(d.is_active_session())

p = ProgrammingSession()

data = p.request()
print(" ".join(f"{b:02x}" for b in data))

data = p.response()
print(" ".join(f"{b:02x}" for b in data))

print(p.is_active_session())

e = ExtendedSession()

data = e.request()
print(" ".join(f"{b:02x}" for b in data))

data = e.response()
print(" ".join(f"{b:02x}" for b in data))
print(e.is_active_session())