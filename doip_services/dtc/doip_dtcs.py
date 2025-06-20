import random
from doip_services.dtc.doip_dtc_utils import DTC

available_dtc_status = (0x00, 0x50, 0x2F, 0x2E, 0x2C, 0x28)

def DtcWrapper(dtc):
    def dtc_decorator(cls):
        if dtc not in DTC:
            print(dtc, cls)
            DTC[dtc] = cls
            cls.dtc_number = dtc
            cls.dtc_status = random.choice(available_dtc_status)
        return cls
    return dtc_decorator

@DtcWrapper(0x3285)
class AliveCounterDTC:
    pass

@DtcWrapper(0x560051)
class ChecksumDTC:
    pass

@DtcWrapper(0x213456)
class InvalidDTC:
    pass

print(f'{AliveCounterDTC.dtc_status =} \n {ChecksumDTC.dtc_status=} \n {InvalidDTC.dtc_status=}\n')

print('--------------------------')
print(DTC.get_all_dtc_codes())
print('--------------------------')
print(DTC.get_all_dtc_codes_and_status())
print('--------------------------')
print(DTC.get_dtc_status(0x3285))
print('--------------------------')
print(DTC.get_dtcs_by_status(0x2F))
print('--------------------------')
print(DTC.get_all_dtc_codes_by_status(0x2F))