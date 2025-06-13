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

read_data_by_identifier = \
    {
        'ActiveDiagnosticSession': (0xF1, 0x86, '4B', (DiagnosticSessionStatus.ACTIVE_SESSION,)),
        'VehicleManufacturerSparePartNumber': (0xF1, 0x87, '8B', (0x31, 0x35, 0x36, 0x41, 0x48)),
        'VehicleManufacturerEcuSoftwareVersionNumber': (0xF1, 0x89, '6B', (0x34, 0x33, 0x37)),
        'VehicleManufacturerECUHardWareNumber': (0xF1, 0x91, '7B', (0x38, 0x35, 0x45, 0x39)),
        'SystemNameOrEngineType': (0xF1, 0x97, '14B', (0x48, 0x43, 0x22, 0xE4, 0xC6, 0xF7, 0x72, 0x20, 0x20, 0x20, 0x20)),
        'VehicleIdentificationNumber': (0xF1,0x90, '9B', (0x32, 0x85, 0x32, 0x85, 0x32, 0x85))
    }
