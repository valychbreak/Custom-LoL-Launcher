from unittest import TestCase

import yaml

from Settings import Settings
from settings_manager import SettingsManager

TEST_DATA = "./test-data/"

ORIGINAL_FILE_PATH = "LeagueClientSettings.yaml"

EXPECTED_FILE_CONTENT = """install:
  globals:
    locale: en_US
    region: EUNE
  login-remember-me:
    rememberMe: true
    username: valych
"""


class TestSettingsManager(TestCase):
    def test_load(self):
        settings_manager = SettingsManager(TEST_DATA + "LeagueClientSettings.yaml")
        settings = settings_manager.load()

        self.assertEqual(Settings('valych', 'en_US', 'EUNE'), settings)

    def test_apply(self):
        initial_content = yaml.dump({'install': {'globals': {'locale': "ru_RU", 'region': 'RU'},
                                     'login-remember-me': {'rememberMe': True, 'username': 'munis'}}}, default_flow_style=False)
        settings = open(TEST_DATA + "SettingsForManager.yaml", "w")
        settings.write(initial_content)
        settings.close()

        settings_manager = SettingsManager(TEST_DATA + "SettingsForManager.yaml")
        settings_manager.apply(Settings('valych', 'en_US', 'EUNE'))

        settings_manager = SettingsManager(TEST_DATA + "SettingsForManager.yaml")
        changed_settings = settings_manager.load()

        self.assertEqual(Settings('valych', 'en_US', 'EUNE'), changed_settings)
        with open(TEST_DATA + "SettingsForManager.yaml") as actual_setting_file:
            self.assertEqual(EXPECTED_FILE_CONTENT, actual_setting_file.read())
