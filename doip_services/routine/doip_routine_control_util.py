from enum import Enum, IntEnum
from doip_services.data_identifiers.doip_data_identifiers_util import *

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

class CheckMemoryRoutine(Enum):
    ROUTINE_ID = (0x02, 0x12, 0x01)
    REQUEST_FORMAT = 5
    RESPONSE_FORMAT = ''
    ROUTINE_RUNTIME = ''
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_RESULTS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryEnum.VehicleManufacturerSparePartNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)

class CompleteAndCompatibilityCheckRoutine(Enum):
    ROUTINE_ID = (0x03, 0x01, 0x40, 0x00 ,0x01, 0x00)
    REQUEST_FORMAT = 15
    RESPONSE_FORMAT = ''
    ROUTINE_RUNTIME = ''
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_RESULTS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryEnum.VehicleManufacturerEcuSoftwareVersionNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)

class CheckUploadPreconditionRoutine(Enum):
    ROUTINE_ID = (0x05, 0x94, 0x76, 0x00)
    REQUEST_FORMAT = 15
    RESPONSE_FORMAT = ''
    ROUTINE_RUNTIME = ''
    ROUTINE_TYPE = RoutineTypes.LONG_ROUTINE.value
    ROUTINE_RESULTS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = (DataIdentifiersFactoryEnum.VehicleIdentificationNumber.value,
                                    DataIdentifiersFactoryMethods.get_did_response.value)

class ProgrammingPreconditionsRoutine(Enum):
    ROUTINE_ID = (0x02, 0x03)
    REQUEST_FORMAT = 8
    RESPONSE_FORMAT = ''
    ROUTINE_RUNTIME = ''
    ROUTINE_TYPE = RoutineTypes.SHORT_ROUTINE.value
    ROUTINE_RESULTS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = ()

class OnDemandSelfTestRoutine(Enum):
    ROUTINE_ID = (0x02, 0x02)
    REQUEST_FORMAT = 2
    RESPONSE_FORMAT = ''
    ROUTINE_RUNTIME = ''
    ROUTINE_TYPE = RoutineTypes.SHORT_ROUTINE.value
    ROUTINE_RESULTS = RoutineStatus.ROUTINE_NOT_STARTED.value
    ROUTINE_RESULTS_RESPONSE_DID = ()


