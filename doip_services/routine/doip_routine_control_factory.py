from src.lib_doip_server.doip_services.routine.doip_routine_control_util import *
from src.lib_doip_server.doip_services.routine.doip_routine_control_services import (
                                                                                CheckMemoryRoutine,
                                                                                OnDemandSelfTestRoutine,
                                                                                ProgrammingPreconditionsRoutine,
                                                                                CheckUploadPreconditionRoutine,
                                                                                CompleteAndCompatibilityCheckRoutine
                                                                                )

def _doip_data_identifier_factory(
                                _data_identifier,
                                _method
                                ):
    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckMemoryRoutine.value:
        if _method == DataIdentifiersFactoryMethods.request.value:
            return  CheckMemoryRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return  CheckMemoryRoutine().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return  CheckMemoryRoutine().get_did_response()

    if _data_identifier == RoutineControlFactoryClassEnum.OnDemandSelfTestRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return OnDemandSelfTestRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return OnDemandSelfTestRoutine().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return OnDemandSelfTestRoutine().get_did_response()

    
    if _data_identifier == RoutineControlFactoryClassEnum.ProgrammingPreconditionsRoutine.value:    
    
        if _method == DataIdentifiersFactoryMethods.request.value:
            return ProgrammingPreconditionsRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return ProgrammingPreconditionsRoutine().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return ProgrammingPreconditionsRoutine().get_did_response()

    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckUploadPreconditionRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return CheckUploadPreconditionRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return CheckUploadPreconditionRoutine().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return CheckUploadPreconditionRoutine().get_did_response()

    
    if _data_identifier == RoutineControlFactoryClassEnum.CompleteAndCompatibilityCheckRoutine.value:
        
        if _method == DataIdentifiersFactoryMethods.request.value:
            return CompleteAndCompatibilityCheckRoutine().request()
        if _method == DataIdentifiersFactoryMethods.response.value:
            return CompleteAndCompatibilityCheckRoutine().response()
        if _method == DataIdentifiersFactoryMethods.get_did_response.value:
            return CompleteAndCompatibilityCheckRoutine().get_did_response()

    return None

