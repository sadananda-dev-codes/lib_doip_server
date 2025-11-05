from enum import Enum

class DoipSessionResetEnum(Enum):
    SID = (0x11,)
    SUBFUNCTIONS = (
                0x01,
                0x02,
                0x03
            )
    REQUEST_FORMAT = '2B'
        
ecu_reset_dict = {
    "DoipSessionReset" : DoipSessionResetEnum
}