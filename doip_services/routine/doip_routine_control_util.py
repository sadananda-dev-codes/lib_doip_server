from enum import Enum, IntEnum
from src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers_util import *
class RoutineSubfunction(IntEnum):
    START_ROUTINE = 1
    STOP_ROUTINE = 2
    RESULT_ROUTINE = 3
class RoutineTypes(IntEnum):
    SHORT_ROUTINE = 1
    LONG_ROUTINE = 2
    CONTINUOUS_ROUTINE = 3
class RoutineStatus(IntEnum):
    ROUTINE_NOT_STARTED = 0
    ROUTINE_CONTINUES = 1
    ROUTINE_ABORTED = 2
    ROUTINE_EXECUTED = 3
class CheckMemoryRoutineEnum(Enum):
    ROUTINE_ID = (0x02, 0x12, 0x01)
    REQUEST_FORMAT = '6B'
    RESPONSE_FORMAT = '11B'
    ROUTINE_RUNTIME = 5
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_STATUS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)
class CompleteAndCompatibilityCheckRoutineEnum(Enum):
    ROUTINE_ID = (0x03, 0x01, 0x40, 0x00 ,0x01, 0x00)
    REQUEST_FORMAT = '9B'
    RESPONSE_FORMAT = '12B'
    ROUTINE_RUNTIME = 15
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_STATUS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryClassEnum.VehicleManufacturerEcuSoftwareVersionNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)
class CheckUploadPreconditionRoutineEnum(Enum):
    ROUTINE_ID = (0x05, 0x94, 0x76, 0x00)
    REQUEST_FORMAT = '7B'
    RESPONSE_FORMAT = '13B'
    ROUTINE_RUNTIME = 8
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_STATUS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryClassEnum.VehicleIdentificationNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)
class ProgrammingPreconditionsRoutineEnum(Enum):
    ROUTINE_ID = (0x02, 0x03)
    REQUEST_FORMAT = '5B'
    RESPONSE_FORMAT = '6B'
    ROUTINE_RUNTIME = 3
    ROUTINE_TYPE = RoutineTypes.SHORT_ROUTINE.value
    ROUTINE_STATUS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (None,)
class OnDemandSelfTestRoutineEnum(Enum):
    ROUTINE_ID = (0x02, 0x02)
    REQUEST_FORMAT = '5B'
    RESPONSE_FORMAT = '6B'
    ROUTINE_RUNTIME = 2
    ROUTINE_TYPE = RoutineTypes.SHORT_ROUTINE.value
    ROUTINE_STATUS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (None,)
class RoutineControlFactoryClassEnum(Enum):
    CheckMemoryRoutine = 'CheckMemoryRoutine'
    OnDemandSelfTestRoutine = 'OnDemandSelfTestRoutine'
    ProgrammingPreconditionsRoutine = 'ProgrammingPreconditionsRoutine'
    CheckUploadPreconditionRoutine = 'CheckUploadPreconditionRoutine'
    CompleteAndCompatibilityCheckRoutine = 'CompleteAndCompatibilityCheckRoutine'