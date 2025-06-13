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

class RoutineSubfunction(IntEnum):
    START_ROUTINE = 1
    STOP_ROUTINE = 2
    ROUTINE_RESULTS = 3

class RoutineTypes(IntEnum):
    SHORT_ROUTINE = 1
    LONG_ROUTINE = 2
    CONTINUOUS_ROUTINE = 3

class RoutineStatus(IntEnum):
    ROUTINE_NOT_STARTED = 0
    ROUTINE_CONTINUES = 1
    ROUTINE_ABORTED = 2
    ROUTINE_EXECUTED = 3

class RoutineResultStatus(Enum):
    ROUTINE_RESULTS_EXISTS = True
    ROUTINE_RESULTS_DOES_NOT_EXITS = False

RoutineControls = {
                'CheckMemoryRoutine' : ('021201', 5, RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value, RoutineResultStatus.ROUTINE_RESULTS_EXISTS.value),
                'CompleteAndCompatibilityCheckRoutine' : ('030140000100', 15, RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value, RoutineResultStatus.ROUTINE_RESULTS_EXISTS.value),
                'CheckUploadPreconditionRoutine' : ('05947600', 8 , RoutineTypes.LONG_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value, RoutineResultStatus.ROUTINE_RESULTS_EXISTS.value),
                'ProgrammingPreconditionsRoutine' : ('0203',3 , RoutineTypes.SHORT_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value, RoutineResultStatus.ROUTINE_RESULTS_DOES_NOT_EXITS.value),
                'OnDemandSelfTestRoutine' : ('0202', 2, RoutineTypes.SHORT_ROUTINE.value, RoutineStatus.ROUTINE_NOT_STARTED.value, RoutineResultStatus.ROUTINE_RESULTS_DOES_NOT_EXITS.value)
                }

CheckMemoryRoutineFmt = {
                        RoutineSubfunction.START_ROUTINE.value : '5B',
                        RoutineSubfunction.STOP_ROUTINE.value : '5B',
                        RoutineSubfunction.ROUTINE_RESULTS.value : '8B'
                        }

complete_and_compatibility_checkRoutine = \
    {
        RoutineSubfunction.START_ROUTINE.value: '5B',
        RoutineSubfunction.STOP_ROUTINE.value: '5B',
        RoutineSubfunction.ROUTINE_RESULTS.value: '8B'
    }

check_upload_precondition_routine = \
    {
        RoutineSubfunction.START_ROUTINE.value: '5B',
        RoutineSubfunction.STOP_ROUTINE.value: '5B',
        RoutineSubfunction.ROUTINE_RESULTS.value: '8B'
    }

programming_preconditions_routine = \
    {
        RoutineSubfunction.START_ROUTINE.value: '5B',
        RoutineSubfunction.STOP_ROUTINE.value: '5B',
        RoutineSubfunction.ROUTINE_RESULTS.value: '8B'
    }

on_demand_self_test_routine = \
    {
        RoutineSubfunction.START_ROUTINE.value: '5B',
        RoutineSubfunction.STOP_ROUTINE.value: '5B',
        RoutineSubfunction.ROUTINE_RESULTS.value: '8B'
    }

read_data_by_identifier = \
    {
        'ActiveDiagnosticSession': (0xF1, 0x86, '4B', (DiagnosticSessionStatus.ACTIVE_SESSION,)),
        'VehicleManufacturerSparePartNumber': (0xF1, 0x87, '8B', (0x31, 0x35, 0x36, 0x41, 0x48)),
        'VehicleManufacturerEcuSoftwareVersionNumber': (0xF1, 0x89, '6B', (0x34, 0x33, 0x37)),
        'VehicleManufacturerECUHardWareNumber': (0xF1, 0x91, '7B', (0x38, 0x35, 0x45, 0x39)),
        'SystemNameOrEngineType': (0xF1, 0x97, '14B', (0x48, 0x43, 0x22, 0xE4, 0xC6, 0xF7, 0x72, 0x20, 0x20, 0x20, 0x20)),
        'VehicleIdentificationNumber': (0xF1,0x90, '9B', (0x32, 0x85, 0x32, 0x85, 0x32, 0x85))
    }
