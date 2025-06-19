import random
from doip_services.dtc.doip_dtc_utils import DTC

available_dtc_status = (0x00, 0x50, 0x2F, 0x2E, 0x2C, 0x28)

def Dtc(dtc):
    def dtc_decorator(cls):
        if dtc not in DTC:
            print(dtc, cls)
            DTC[dtc] = cls
            cls.dtc_number = dtc
            cls.dtc_status = random.choice(available_dtc_status)
        return cls
    return dtc_decorator

@Dtc(0x3285)
class AliveCounterDTC:
    pass

@Dtc(0x560051)
class ChecksumDTC:
    pass

@Dtc(0x213456)
class InvalidDTC:
    pass

print('--------------------------')
print(DTC.get_all_dtc_codes())
print('--------------------------')
print(DTC.get_all_dtc_codes_and_status())
print('--------------------------')
print(DTC.get_dtc_status(0x3285))
print('--------------------------')
print(DTC.get_dtcs_by_status(0x2F))