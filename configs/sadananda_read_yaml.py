import yaml

DATA_IDENTIFIER = 'doip_data_identifier.yaml'

def read_config_data(yaml_file):
    data = {}
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    return data

def write_config_data(yaml_file, data):
    with open(yaml_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        
##########################################################
