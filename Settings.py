
class Settings(object):
    def __init__(self, username, locale, region) -> None:
        self.username = username
        self.locale = locale
        self.region = region

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Settings):
            return self.username == o.username and self.locale == o.locale and self.region == o.region
        return False

    def __str__(self) -> str:
        return "Settings({}, {}, {})".format(self.username, self.locale, self.region)

    def __repr__(self) -> str:
        return self.__str__()


