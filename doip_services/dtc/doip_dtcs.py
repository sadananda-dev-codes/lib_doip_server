import random
from src.lib_doip_server.doip_services.dtc.doip_dtc_utils import DTC

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
@DtcWrapper(0x328511)
class AliveCounterDTC:
    pass
@DtcWrapper(0x560051)
class ChecksumDTC:
    pass
@DtcWrapper(0xEF0700)
class InvalidDTC:
    pass
@DtcWrapper(0xEF1100)
class TimeoutDTC:
    pass