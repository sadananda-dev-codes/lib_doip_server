def _doip_data_identifier_factory(routine_control , _method):

    match data_identifier_class:
        case DataIdentifiersFactoryClassEnum.VehicleManufacturerSparePartNumber.value:
            if _method == DataIdentifiersFactoryMethods.request.value:
                return  VehicleManufacturerSparePartNumber().request()
            if _method == DataIdentifiersFactoryMethods.response.value:
                return  VehicleManufacturerSparePartNumber().response()
            if _method == DataIdentifiersFactoryMethods.get_did_response.value:
                return  VehicleManufacturerSparePartNumber().get_did_response()
