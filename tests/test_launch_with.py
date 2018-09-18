import os
from unittest import TestCase

from Settings import Settings
from client_setup import setup
from settings_manager import SettingsManager

GAME_PATH = './test-data/launcher-data'
TEST_DATA = "./test-data/launcher-data/Config/"

ORIGINAL_FILE_PATH = "LeagueClientSettings.yaml"
BACKUP_FILE_PATH = "LeagueClientSettings.yaml.backup"


class TestLaunchWith(TestCase):

    def setUp(self):
        if os.path.isfile(TEST_DATA + BACKUP_FILE_PATH):
            os.remove(TEST_DATA + ORIGINAL_FILE_PATH)
            os.rename(TEST_DATA + BACKUP_FILE_PATH, TEST_DATA + ORIGINAL_FILE_PATH)

    def test_launch_with(self):
        setup(os.path.abspath(GAME_PATH), 'valych', 'en_GB', 'EUNE')

        self.assertTrue(os.path.isfile(TEST_DATA + BACKUP_FILE_PATH))

        settings_manager = SettingsManager(TEST_DATA + ORIGINAL_FILE_PATH)
        actual_settings = settings_manager.load()
        self.assertEqual(Settings('valych', 'en_GB', 'EUNE'), actual_settings)

        backup_settings_manager = SettingsManager(TEST_DATA + BACKUP_FILE_PATH)
        backup_settings = backup_settings_manager.load()
        self.assertEqual(Settings('munis', 'ru_RU', 'RU'), backup_settings)
