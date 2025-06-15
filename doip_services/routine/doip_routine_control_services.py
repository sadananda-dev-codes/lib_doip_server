from doip_routine_control_util import *
import struct
from doip_services.data_identifiers.doip_data_identifier_factory import _doip_data_identifier_factory
from  doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices
from doip_routine_functions import *
import asyncio

class RoutineControlMeta(type):

    __routine_control_attrs__ = ('routine_id',
                                 'request_fmt',
                                 'response_fmt',
                                 'routine_run_time',
                                 'routine_type',
                                 'routine_status',
                                 'routine_result'
                                 )

    def __new__(cls, name, bases, dct):

        new_cls = super().__new__(cls, name, bases, dct)

        for attr_name in cls.__routine_control_attrs__:
            attr = f'_{attr_name}'
            def make_property(attr_name, attr):

                def getter(self):
                    return getattr(self, attr)

                def setter(self,
                           value = 0):
                    if value < 0:  # Example validation
                        raise ValueError(f"{name} cannot be negative")
                    setattr(self, attr, value)

                return property(getter, setter)

            setattr(new_cls, attr_name, make_property(attr_name, attr))

        return new_cls

class RoutineControlService(metaclass=RoutineControlMeta):
    service_id = 0x31
    sub_function = 0x01
    task = None

    def __init__(self):

        for routine_attrs, default in zip(RoutineControlService.__routine_control_attrs__,
                                             self._routine_attribute_values):
            setattr(self, f'_{routine_attrs}', default.value)

    def _request(self):
        return  struct.pack(self.request_fmt, self.service_id, self.sub_function, *self.routine_id, self.routine_type | self.routine_status)

    def start(self)-> bytes:
        self.sub_function = RoutineSubfunction.START_ROUTINE.value
        self.start_routine()
        return self._request()

    def stop(self):
        self.sub_function = RoutineSubfunction.STOP_ROUTINE.value
        self.task.cancel()
        self.routine_status = RoutineStatus.ROUTINE_ABORTED.value
        return self._request()

    def result(self):
        self.sub_function = RoutineSubfunction.RESULT_ROUTINE.value
        return self._request()

    def  start_routine(self):
        asyncio.run(self._routine_control_handler())

    async def _routine_control_handler(self):
        loop = asyncio.get_running_loop()
        self.task = loop.create_task(_check_memory_routine(self))
        await asyncio.sleep(1)

    def response(self):

        if self.sub_function == RoutineSubfunction.RESULT_ROUTINE.value and \
                self.routine_type == RoutineTypes.LONG_ROUTINE.value:
                    _routine_response_data = _doip_data_identifier_factory(*self.routine_result)
                    return  struct.pack(self.response_fmt, self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, self.sub_function, *self.routine_id, self.routine_type | self.routine_status, *_routine_response_data)
        else:
            return  struct.pack(self.request_fmt, self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, self.sub_function, *self.routine_id, self.routine_type | self.routine_status)

    def __str__(self):
        return f'{self.__class__.__name__}\n\t{self.service_id = }\n\t{self.sub_function = }\n\t{self.routine_id = }\n\t{self.routine_type = }\n\t{self.routine_status = } '

class CheckMemoryRoutine(RoutineControlService):
    _routine_attribute_values = CheckMemoryRoutineEnum
    _sub_routine = _check_memory_routine
    pass

class OnDemandSelfTestRoutine(RoutineControlService):
    _routine_attribute_values = OnDemandSelfTestRoutineEnum
    _sub_routine = _on_demand_self_test_routine
    pass

class ProgrammingPreconditionsRoutine(RoutineControlService):
    _routine_attribute_values = ProgrammingPreconditionsRoutineEnum
    _sub_routine = _programming_preconditions_routine
    pass

class CheckUploadPreconditionRoutine(RoutineControlService):
    _routine_attribute_values = CheckUploadPreconditionRoutineEnum
    _sub_routine = _check_upload_precondition_routine
    pass

class CompleteAndCompatibilityCheckRoutine(RoutineControlService):
    _routine_attribute_values = CompleteAndCompatibilityCheckRoutineEnum
    _sub_routine = _complete_and_compatibility_check_routine
    pass

sadananda = CheckMemoryRoutine()
print(sadananda.start().hex())
print(sadananda.response().hex())
print(sadananda.stop().hex())
print(sadananda.response().hex())
print(sadananda.result().hex())
print(sadananda.response().hex())

print('-----------------------------------------')

sadananda = CompleteAndCompatibilityCheckRoutine()
print(sadananda.start().hex())
print(sadananda.response().hex())
print(sadananda.stop().hex())
print(sadananda.response().hex())
print(sadananda.result().hex())
print(sadananda.response().hex())
print('')
print('-----------------------------------------')

sadananda = CheckUploadPreconditionRoutine()
print('')
print(sadananda.start().hex())
print(sadananda.response().hex())
print(sadananda.stop().hex())
print(sadananda.response().hex())
print(sadananda.result().hex())
print(sadananda.response().hex())
print('')

print('-----------------------------------------')

sadananda = OnDemandSelfTestRoutine()
print(sadananda)
print('')
print(sadananda.start().hex())
print(sadananda.response().hex())
print(sadananda.stop().hex())
print(sadananda.response().hex())
print(sadananda.result().hex())
print(sadananda.response().hex())
print('')

print('-----------------------------------------')

sadananda = ProgrammingPreconditionsRoutine()
print(sadananda)
print('')
print(sadananda.start().hex())
print(sadananda.response().hex())
print(sadananda.stop().hex())
print(sadananda.response().hex())
print(sadananda.result().hex())
print(sadananda.response().hex())
print('')
