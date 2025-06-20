import struct
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticLayerEnum, DiagnosticServices, DiagnosticSessionStatus

class DiagnosticSession:

    def __init__(self):
        self.service_id = DiagnosticServices.SESSION.value
        self.sub_function = getattr(self, '_session_id',None)

    def request(self) -> bytes:
        return struct.pack(
                            '!BBHH',
                               self.service_id,
                               self.sub_function,
                               DiagnosticLayerEnum.P2_SERVER_INIT.value,
                               DiagnosticLayerEnum.P2_EXTENDED_SERVER_INIT.value
                            )

    def response(self)->bytes:
        return struct.pack(
                        '!BBHH',
                            self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value,
                                self.sub_function,
                                DiagnosticLayerEnum.P2_SERVER_INIT.value,
                                DiagnosticLayerEnum.P2_EXTENDED_SERVER_INIT.value
                                )

    def is_active_session(self):
        return self.sub_function == DiagnosticSessionStatus.ACTIVE_SESSION

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