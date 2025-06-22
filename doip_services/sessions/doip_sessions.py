import struct
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticLayerEnum, DiagnosticServices, DiagnosticSessionStatus

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
    _session_id = 0x1

class ProgrammingSession(DiagnosticSession):
    _session_id = 0x2

class ExtendedSession(DiagnosticSession):
    _session_id = 0x3

d = DefaultSession()
print(d.request().hex())
print(d.response().hex())
print(d.is_active_session())

p = ProgrammingSession()
print(p.request().hex())
print(p.response().hex())
print(p.is_active_session())

e = ExtendedSession()
print(e.request().hex())
print(e.response().hex())
print(e.is_active_session())