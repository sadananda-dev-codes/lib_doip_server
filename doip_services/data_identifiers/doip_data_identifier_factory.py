from doip_services.routine.doip_routine_control_util import CompleteAndCompatibilityCheck
from doip_services.data_identifiers.doip_data_identifiers import *

def _doip_data_identifier_factory(data_identifier_class , _method):

    match data_identifier[0]:
        case CompleteAndCompatibilityCheck.ROUTINE_RESULTS_RESPONSE_DIDS.value:
            return  VehicleManufacturerSparePartNumber().get_did_response()


