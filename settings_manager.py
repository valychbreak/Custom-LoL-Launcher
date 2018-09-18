import yaml

from Settings import Settings


def get_login(settings_dict):
    return settings_dict['install']['login-remember-me']


def get_globals(settings_dict):
    return settings_dict['install']['globals']


class SettingsManager:
    def __init__(self, settings_file_path) -> None:
        self.settings_file_path = settings_file_path

    def load(self) -> Settings:
        settings_file = open(self.settings_file_path, "r")
        settings_dict = yaml.load(settings_file)
        settings_file.close()

        globals_dict = get_globals(settings_dict)
        login_dict = get_login(settings_dict)
        return Settings(login_dict['username'], globals_dict['locale'], globals_dict['region'])

    def apply(self, new_settings: Settings):
        with open(self.settings_file_path, "r") as settings_file:
            settings_dict = yaml.load(settings_file)

        self.populate_new_changes(settings_dict, new_settings)

        with open(self.settings_file_path, "w") as settings_file:
            settings_file.write(yaml.dump(settings_dict, default_flow_style=False))

    def populate_new_changes(self, settings_dict, new_settings):
        globals_settings = get_globals(settings_dict)
        login_settings = get_login(settings_dict)

        if new_settings.username is not None and login_settings['username'] != new_settings.username:
            login_settings['username'] = new_settings.username
        if new_settings.locale is not None and globals_settings['locale'] != new_settings.locale:
            globals_settings['locale'] = new_settings.locale
        if new_settings.region is not None and globals_settings['region'] != new_settings.region:
            globals_settings['region'] = new_settings.region
