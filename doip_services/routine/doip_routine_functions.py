import asyncio
from doip_routine_control_util import RoutineStatus

__all__ = ['_check_memory_routine',
           '_on_demand_self_test_routine',
           '_programming_preconditions_routine',
           '_check_upload_precondition_routine',
           '_complete_and_compatibility_check_routine'
           ]

async def _check_memory_routine(routine_control):
    routine_control.task.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    routine_control.task.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

async def _on_demand_self_test_routine(routine_control):

    try:
        routine_control.task.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
        routine_control.task.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

async def _programming_preconditions_routine(routine_control):

    try:
        routine_control.task.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
        await asyncio.sleep(3)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    routine_control.task.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

async def _check_upload_precondition_routine(routine_control):

    try:
        routine_control.task.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
        await asyncio.sleep(8)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    routine_control.task.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

async def _complete_and_compatibility_check_routine(routine_control):
    try:
        routine_control.task.routine_status = RoutineStatus.ROUTINE_CONTINUES.value
        await asyncio.sleep(15)
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    routine_control.task.routine_status = RoutineStatus.ROUTINE_EXECUTED.value

