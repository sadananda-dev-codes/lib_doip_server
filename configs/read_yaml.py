import os
import yaml

def _get_file_path(yaml_file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_file_path = os.path.join(base_dir, yaml_file)
    return absolute_file_path

def read_config_data(yaml_file, data={}):
    yaml_file = _get_file_path(yaml_file)
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)
        
    return data

def write_config_data(yaml_file, data):
    with open(yaml_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        
##########################################################