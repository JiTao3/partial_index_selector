
import yaml

class ConfigParse:
    def __init__(self, config_filepath) -> None:
        self.config_filepath = config_filepath
        self.conf = None
        self.read()

    def read(self):
        with open(self.config_filepath, 'r', encoding='utf-8') as f:
            file_data = f.read()
            self.conf = yaml.load(file_data, Loader=yaml.FullLoader)


    def parse(self):
        pass