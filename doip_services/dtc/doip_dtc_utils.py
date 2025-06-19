from collections import UserDict

class DtcDict(UserDict):

    def get_all_dtc_codes_and_status(self):
        return [(key, dtc.dtc_status) for key, dtc in zip(self.keys(), self.values())]

    def get_all_dtc_codes(self):
        return list(self.keys())

    def get_status_of_all_dtc(self):
        return [dtc.dtc_status for  dtc in self.values()]

    def get_dtc_codes_by_snapshot_id(self, snapshot_id):
        return

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

DTC = DtcDict()
