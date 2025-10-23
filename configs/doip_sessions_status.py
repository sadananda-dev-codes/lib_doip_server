from src.lib_doip_server.doip_diagnostic_session.doip_diagnostic_layer_utils import DiagnosticSessionStatus
class DoIPState:
    
    current_session = DiagnosticSessionStatus.ACTIVE_SESSION
    security_unlocked = 0x00
    routing_activation_requested = 0x00
    invalid_attempts = 0
    number_of_hard_resets = 0
    
    @classmethod
    def nrc(cls, sid, nrc):
        import struct
        return struct.pack('!3B', 0x7F, sid, nrc)