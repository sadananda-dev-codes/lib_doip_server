import time

from src.lib_doip_server.doip_services.routine.doip_routine_control_util import (
                                    RoutineStatus,
                                    CheckMemoryRoutineEnum,
                                    CompleteAndCompatibilityCheckRoutineEnum,
                                    CheckUploadPreconditionRoutineEnum,
                                    ProgrammingPreconditionsRoutineEnum,
                                    OnDemandSelfTestRoutineEnum
                                    )

def _check_memory_routine(routine_control):
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CheckMemoryRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

def _on_demand_self_test_routine(routine_control):
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value    
    time.sleep(OnDemandSelfTestRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

def _programming_preconditions_routine(routine_control):
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(ProgrammingPreconditionsRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

def _check_upload_precondition_routine(routine_control):
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CheckUploadPreconditionRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

def _complete_and_compatibility_check_routine(routine_control):
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CompleteAndCompatibilityCheckRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value