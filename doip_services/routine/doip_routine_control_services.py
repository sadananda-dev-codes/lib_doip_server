from doip_routine_control_util import *
import struct
from doip_services.data_identifiers.doip_data_identifier_factory import _doip_data_identifier_factory
from  doip_diagnostic_session.doip_diagnostic_layer import DiagnosticServices

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
                           routine_name = attr,
                           value = 0):
                    if value < 0:  # Example validation
                        raise ValueError(f"{name} cannot be negative")
                    setattr(self, routine_name, value)

                return property(getter, setter)

            setattr(new_cls, attr_name, make_property(attr_name, attr))

        return new_cls

class RoutineControlService(metaclass=RoutineControlMeta):
    service_id = 0x31
    sub_function = 0x01

    def __init__(self):

        for routine_attrs, default in zip(RoutineControlService.__routine_control_attrs__,
                                             self._routine_attribute_values):
            setattr(self, f'_{routine_attrs}', default.value)

    def _request(self):
        return  struct.pack(self.request_fmt, self.service_id, self.sub_function, *self.routine_id, self.routine_type | self.routine_status)

    def start(self)-> bytes:
        self.sub_function = RoutineSubfunction.START_ROUTINE.value
        return self._request()

    def stop(self):
        self.sub_function = RoutineSubfunction.STOP_ROUTINE.value
        return self._request()

    def result(self):
        self.sub_function = RoutineSubfunction.RESULT_ROUTINE.value
        return self._request()

    def response(self):

        if self.sub_function == RoutineSubfunction.RESULT_ROUTINE.value and \
                self.routine_type == RoutineTypes.LONG_ROUTINE.value:
                    _routine_response_data = _doip_data_identifier_factory(*self.routine_result)
                    return  struct.pack(self.response_fmt, self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, self.sub_function, *self.routine_id, self.routine_type | self.routine_status, *_routine_response_data)
        else:
            return  struct.pack(self.request_fmt, self.service_id + DiagnosticServices.POSITIVE_RESPONSE_CODE.value, self.sub_function, *self.routine_id, self.routine_type | self.routine_status)

    def __str__(self):
        return f'{self.__class__.__name__}\n\t{hex(self.service_id)=}\n\t{self.sub_function=}\n\t{self.routine_id=}\n\t{self.routine_type=}\n\t{self.routine_status=} '

class CheckMemoryRoutine(RoutineControlService):
    _routine_attribute_values = CheckMemoryRoutineEnum
    pass

class OnDemandSelfTestRoutine(RoutineControlService):
    _routine_attribute_values = OnDemandSelfTestRoutineEnum
    pass

class ProgrammingPreconditionsRoutine(RoutineControlService):
    _routine_attribute_values = ProgrammingPreconditionsRoutineEnum
    pass

class CheckUploadPreconditionRoutine(RoutineControlService):
    _routine_attribute_values = CheckUploadPreconditionRoutineEnum
    pass

class CompleteAndCompatibilityCheckRoutine(RoutineControlService):
    _routine_attribute_values = CompleteAndCompatibilityCheckRoutineEnum
    pass

'''
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
'''



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