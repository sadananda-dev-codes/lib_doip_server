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
    print('STARTED ROUTINE: Check Memory')
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CheckMemoryRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value
    print('STOPPED ROUTINE: Check Memory')
    print('')

def _on_demand_self_test_routine(routine_control):
    print('STARTED ROUTINE: ON DEMAND SELF TEST')
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value    
    time.sleep(OnDemandSelfTestRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value
    print('STOPPED ROUTINE: ON DEMAND SELF TEST')
    print('')

def _programming_preconditions_routine(routine_control):
    print('STARTED ROUTINE: PROGRAMMING PRE-CONDITION')
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(ProgrammingPreconditionsRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value
    print('STOPPED ROUTINE: PROGRAMMING PRE-CONDITION')
    print('')

def _check_upload_precondition_routine(routine_control):
    print('STARTED ROUTINE: CHECK UPLOAD PRECONDITION')
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CheckUploadPreconditionRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value
    print('STOPPED ROUTINE: CHECK UPLOAD PRECONDITION')
    print('')

def _complete_and_compatibility_check_routine(routine_control):
    print('STARTED ROUTINE: COMPLETE AND COMPATIBILITY')
    routine_control.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    time.sleep(CompleteAndCompatibilityCheckRoutineEnum.ROUTINE_RUNTIME.value)
    routine_control.routine_status = RoutineStatus.ROUTINE_EXECUTED.value
    print('STOPPED ROUTINE: COMPLETE AND COMPATIBILITY')
    print('')