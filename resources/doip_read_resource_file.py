class ResourceReader:

    def load_resource_configuration(self,
                            resource_config_file_path):
        pass

    def is_file_path_valid(self):
        return True
class JsonFileReader(ResourceReader):
    pass
class YamlResourceReader(ResourceReader):
    pass
