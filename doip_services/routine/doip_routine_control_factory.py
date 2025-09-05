from src.lib_doip_server.doip_services.routine.doip_routine_control_util import *
from src.lib_doip_server.doip_services.routine.doip_routine_control_services import (
                                                                                CheckMemoryRoutine,
                                                                                OnDemandSelfTestRoutine,
                                                                                ProgrammingPreconditionsRoutine,
                                                                                CheckUploadPreconditionRoutine,
                                                                                CompleteAndCompatibilityCheckRoutine
                                                                                )

def _doip_routine_identifier_factory(_data_identifier, _method):
    
    
    print(_data_identifier, _method)
    
    diag_object = None
    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckMemoryRoutine.value:
        diag_object = CheckMemoryRoutine()

    if _data_identifier == RoutineControlFactoryClassEnum.OnDemandSelfTestRoutine.value:
        diag_object =  OnDemandSelfTestRoutine()
    
    if _data_identifier == RoutineControlFactoryClassEnum.ProgrammingPreconditionsRoutine.value:    
        diag_object = ProgrammingPreconditionsRoutine()
    
    if _data_identifier == RoutineControlFactoryClassEnum.CheckUploadPreconditionRoutine.value:
        diag_object = CheckUploadPreconditionRoutine()
    
    if _data_identifier == RoutineControlFactoryClassEnum.CompleteAndCompatibilityCheckRoutine.value:
        diag_object = CompleteAndCompatibilityCheckRoutine()
    
    if diag_object is None:
        return None
    else:
        if _method == RoutineControlIdentifiersFactoryMethods.start.value:
            return diag_object.start()
        if _method == RoutineControlIdentifiersFactoryMethods.request.value:
            return  diag_object.request()
        if _method == RoutineControlIdentifiersFactoryMethods.response.value:
            return  diag_object.response()
        if _method == RoutineControlIdentifiersFactoryMethods.stop.value:
            return  diag_object.stop()

