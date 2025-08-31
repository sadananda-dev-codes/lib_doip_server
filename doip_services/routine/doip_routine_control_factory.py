from src.lib_doip_server.doip_services.routine.doip_routine_control_util import *
from src.lib_doip_server.doip_services.routine.doip_routine_control_services import (
                                                                                CheckMemoryRoutine,
                                                                                OnDemandSelfTestRoutine,
                                                                                ProgrammingPreconditionsRoutine,
                                                                                CheckUploadPreconditionRoutine,
                                                                                CompleteAndCompatibilityCheckRoutine
                                                                                )

def _doip_routine_identifier_factory(_data_identifier, _method):
    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckMemoryRoutine.value:
        if _method == DataIdentifiersFactoryMethods.request.value:
            return  CheckMemoryRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return  CheckMemoryRoutine().response()

    if _data_identifier == RoutineControlFactoryClassEnum.OnDemandSelfTestRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return OnDemandSelfTestRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return OnDemandSelfTestRoutine().response()
        
    
    if _data_identifier == RoutineControlFactoryClassEnum.ProgrammingPreconditionsRoutine.value:    
    
        if _method == DataIdentifiersFactoryMethods.request.value:
            return ProgrammingPreconditionsRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return ProgrammingPreconditionsRoutine().response()
    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckUploadPreconditionRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return CheckUploadPreconditionRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return CheckUploadPreconditionRoutine().response()
    
    if _data_identifier == RoutineControlFactoryClassEnum.CompleteAndCompatibilityCheckRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return CompleteAndCompatibilityCheckRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return CompleteAndCompatibilityCheckRoutine().response()

    return None

