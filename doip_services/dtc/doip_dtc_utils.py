from collections import UserDict
from enum import Enum
from  src.lib_doip_server.doip_services.data_identifiers.doip_data_identifiers import (
                                                            GlobalRealTime,
                                                            TotalDistance,
                                                            VehicleBatteryVoltage,
                                                            UsageMode,
                                                            ElectricPowerLevel)

class DtcSnapShotDid(Enum):
    GlobalRealTime = GlobalRealTime()
    TotalDistance = TotalDistance()
    VehicleBatteryVoltage = VehicleBatteryVoltage()
    UsageMode = UsageMode()
    ElectricPowerLevel = ElectricPowerLevel()

def get_snap_shot_dids():
    snap_shot_dids = []
    for item in DtcSnapShotDid:
        snap_shot_dids.append(item.value.data_identifier_lsb)
        snap_shot_dids.append(item.value.data_identifier_msb)
        snap_shot_dids.extend(item.value.data_identifier_response)
    return snap_shot_dids

class DtcDict(UserDict):

    def get_all_dtc_codes_and_status(self):
        return [(key, dtc.dtc_status) for key, dtc in zip(self.keys(), self.values())]

    def get_all_dtc_codes(self):
        return list(self.keys())

    def get_all_dtc_codes_by_status(self, status):
        return [(dtc, _status.dtc_status) for dtc, _status in zip(self.keys(), self.values()) if _status.dtc_status | status ]

    def get_status_of_all_dtc(self):
        return [dtc.dtc_status for  dtc in self.values()]

    def get_dtcs_by_status(self, status, _list=[]):
        for dtc in self.values():
            if dtc.dtc_status==status:
                _list.append(dtc.dtc_number)
        return _list

    def get_dtc_status(self, dtc_number):
        for dtc in self.values():
            if dtc.dtc_number==dtc_number:
                return dtc.dtc_status
        return None

    def get_dtc_and_their_status(self):
        return [(dtc, _status.dtc_status) for dtc, _status in zip(self.keys(), self.values())]

DTC = DtcDict()
