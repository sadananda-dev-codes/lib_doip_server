from enum import IntEnum, Enum


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

class RoutineTypes(IntEnum):
    SHORT_ROUTINE = 1
    LONG_ROUTINE = 2

class RoutineStatus(IntEnum):
    ROUTINE_CONTINUES = 1
    ROUTINE_ABORTED = 2
    ROUTINE_EXECUTED = 3

class RoutineControls(Enum):
    CHECK_MEMORY_ROUTINE = ('021201', 5, RoutineTypes.LONG_ROUTINE.value)
    ON_DEMAND_SELF_TEST = ('0202', 2, RoutineTypes.SHORT_ROUTINE.value)
    PROGRAMMING_PRECONDITIONS = ('0203',3 , RoutineTypes.SHORT_ROUTINE.value)
    CHECK_UPLOAD_PRECONDITION = ('05947600', 8 , RoutineTypes.LONG_ROUTINE.value)
    COMPLETE_AND_COMPATIBILITY_CHECK = ('030140000100', 15, RoutineTypes.LONG_ROUTINE.value)


