from utils_constants.doip_constants import  RoutineControls, RoutineSubfunction, CheckMemoryRoutineFmt
import struct

class RoutineControlMeta(type):

    __routine_control_attrs__ = ('routine_id',
                                 'routine_run_time',
                                 'routine_type',
                                 'routine_status',
                                 'has_routine_results'
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

        routine_control = f'{self.__class__.__name__}'

        routine_ctrl_default_values = RoutineControls[routine_control]
        for routine_attrs, attr_value in zip(CheckMemoryRoutine.__routine_control_attrs__,
                                             routine_ctrl_default_values):

            if isinstance(attr_value, str):
                attr_value = bytes.fromhex(attr_value)

            setattr(self, f'_{routine_attrs}', attr_value)

    def request(self,
                sub_function)-> bytes:
        self.sub_function = sub_function
        return  struct.pack('5B', self.service_id, self.sub_function, *self.routine_id)

    def response(self,
                 nrc=None):

        if not nrc:
            return struct.pack('3B', self.service_id, nrc)

        if  self.has_routine_results and self.sub_function == RoutineSubfunction.ROUTINE_RESULTS.value:
                return struct.pack(CheckMemoryRoutineFmt[self.sub_function],
                               self.service_id + 0x40,
                                   self.sub_function,
                                   *self.routine_id,
                                   self.routine_type | self.routine_status,
                                   *self.get_routine_results()
                                  )
        else:
                return struct.pack(CheckMemoryRoutineFmt[self.sub_function],
                                   self.service_id,
                               self.sub_function,
                                   *self.routine_id,
                                   self.routine_type | self.routine_status)

class CheckMemoryRoutine(RoutineControlService):

    @staticmethod
    def get_routine_results(self):
        return (32, 85)

class OnDemandSelfTestRoutine(RoutineControlService):
    pass

class ProgrammingPreconditionsRoutine(RoutineControlService):
    pass

class CheckUploadPreconditionRoutine(RoutineControlService):
    pass

class CompleteAndCompatibilityCheckRoutine(RoutineControlService):
    pass

sadananda = CheckMemoryRoutine()
print('')
print('routine id',sadananda.routine_id.hex())
print('routine_run_time',sadananda.routine_run_time)
print('routine_type',sadananda.routine_type)
print('routine_status',sadananda.routine_status)
print('-----------------------------------------')

print(sadananda.request(0x01).hex())
print(sadananda.request(0x02).hex())
print(sadananda.request(0x03).hex())

print('sadananda response')
print(sadananda.response(1).hex())
print(sadananda.response(2).hex())
print(sadananda.response(3).hex())


'''
sadananda = CompleteAndCompatibilityCheckRoutine()
print('')
print('routine id',sadananda.routine_id.hex())
print('routine_run_time',sadananda.routine_run_time)
print('routine_type',sadananda.routine_type)
print('routine_status',sadananda.routine_status)
print('-----------------------------------------')

sadananda = CheckUploadPreconditionRoutine()
print('')
print('routine id',sadananda.routine_id.hex())
print('routine_run_time',sadananda.routine_run_time)
print('routine_type',sadananda.routine_type)
print('routine_status',sadananda.routine_status)

print('-----------------------------------------')

sadananda = OnDemandSelfTestRoutine()
print('')
print('routine id',sadananda.routine_id.hex())
print('routine_run_time',sadananda.routine_run_time)
print('routine_type',sadananda.routine_type)
print('routine_status',sadananda.routine_status)

print('-----------------------------------------')
'''