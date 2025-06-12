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

class RoutineSubfunction(IntEnum):
    START_ROUTINE = 1
    STOP_ROUTINE = 2
    ROUTINE_RESULTS = 3

class RoutineTypes(IntEnum):
    SHORT_ROUTINE = 1
    LONG_ROUTINE = 2
    CONTINEUOUS_ROUTINE = 3

class RoutineStatus(IntEnum):
    ROUTINE_NOT_STARTED = 0
    ROUTINE_CONTINUES = 1
    ROUTINE_ABORTED = 2
    ROUTINE_EXECUTED = 3


RoutineControls = {'CheckMemoryRoutine' : ('021201', 5, RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value),
                'CompleteAndCompatibilityCheckRoutine' : ('030140000100', 15, RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value),
                'CheckUploadPreconditionRoutine' : ('05947600', 8 , RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value),
                'ProgrammingPreconditionsRoutine' : ('0203',3 , RoutineTypes.SHORT_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value),
                'OnDemandSelfTestRoutine' : ('0202', 2, RoutineTypes.SHORT_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value)
                }

CheckMemoryRoutineFmt = {
                        RoutineSubfunction.START_ROUTINE.value : '5B',
                        RoutineSubfunction.STOP_ROUTINE.value : '5B',
                        RoutineSubfunction.ROUTINE_RESULTS.value : '8B'
                        }

complete_and_compatibility_checkRoutine = {}
check_upload_precondition_routine = {}
programming_preconditions_routine = {}
on_demand_self_test_routine = {}


