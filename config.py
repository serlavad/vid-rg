import os

class PATHS:
    HOME = os.path.expanduser("~")

class SQLITE:
    DB_PATH = "{}/stashapp/config/stash-go.sqlite".format(PATHS.HOME)
