import os
import json

class AppConfiguration:
    CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.json')

    @staticmethod
    def get_app_configuration():
        try:
            config_data = AppConfiguration.read_file("config.json")
        except FileNotFoundError:
            config_file_path = AppConfiguration.CONFIG_FILE_PATH
            config_data = AppConfiguration.read_file(config_file_path)
        return config_data

    @staticmethod
    def get_common_info():
        config_data = AppConfiguration.get_app_configuration()
        config_common_data = config_data["common info"]
        return config_common_data

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            file_data = json.load(f)
        return file_data