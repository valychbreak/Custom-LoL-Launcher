import os
from unittest import TestCase

from file_backup import backup_original_file


TEST_DATA = "./test-data/"

ORIGINAL_FILE_PATH = "LeagueClientSettings.yaml"
BACKUP_FILE_PATH = "LeagueClientSettings.yaml.backup"


class TestFileBackup(TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

        if os.path.isfile(TEST_DATA + BACKUP_FILE_PATH):
            os.remove(TEST_DATA + BACKUP_FILE_PATH)

    def test_backup_original_files(self):
        backup_original_file(TEST_DATA + ORIGINAL_FILE_PATH)

        self.assertTrue(os.path.isfile(TEST_DATA + BACKUP_FILE_PATH))

    def test_backed_up_file_is_the_same_as_original(self):
        backup_original_file(TEST_DATA + ORIGINAL_FILE_PATH)

        original_content = read_file(ORIGINAL_FILE_PATH)
        backed_up_content = read_file(BACKUP_FILE_PATH)

        self.assertEqual(original_content, backed_up_content)

    def test_raises_error_when_backup_file_exists(self):
        backup_original_file(TEST_DATA + ORIGINAL_FILE_PATH)

        original_content = read_file(ORIGINAL_FILE_PATH)
        backed_up_content = read_file(BACKUP_FILE_PATH)

        self.assertEqual(original_content, backed_up_content)


def read_file(file_path):
    original = open(TEST_DATA + file_path, "r")
    original_content = original.read()
    original.close()
    return original_content
