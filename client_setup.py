import subprocess

from Settings import Settings
from file_backup import backup_original_file
from settings_manager import SettingsManager


def setup(game_path, username, locale, region):
    settings_path = game_path + "/Config/LeagueClientSettings.yaml"
    backup_original_file(settings_path)

    settings_manager = SettingsManager(settings_path)
    settings_manager.apply(Settings(username, locale, region))

    # Launch LoL
    #subprocess.Popen([game_path + '/LeagueClient.exe'])


# launch_with("C:\\Games\\League of Legends", "munis", "ru_RU", "RU")
# launch_with("C:\\Games\\League of Legends", "valych", "en_GB", "EUNE")
