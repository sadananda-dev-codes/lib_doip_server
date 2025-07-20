from enum import IntEnum, Enum
from doip_diagnostic_session.doip_diagnostic_layer import DiagnosticSessionStatus

class DoipMsgTypes(IntEnum):
    """
        This is a Enum class which holds he integer values.
        This class has all the doip possible headers.
    """
    GenericDoIPNegativeAcknowledge = 0x0000
    VehicleIdentificationRequest = 0x0001
    VehicleIdentificationRequestWithEID = 0x0002
    VehicleIdentificationRequestWithVIN = 0x0003
    RoutingActivationRequest = 0x0005
    AliveCheckRequest = 0x0007
    DoipEntityStatusRequest = 0x4001
    DiagnosticPowerModeRequest = 0x4003
    DiagnosticMessage = 0x8001


    
