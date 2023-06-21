from selenium import webdriver

from config import PATHS


def configure_driver():
    path = "{}/.mozilla/firefox/rh31pjxc.rg".format(PATHS.HOME)
    options = webdriver.FirefoxOptions()
    options.profile = webdriver.FirefoxProfile(path)
    return webdriver.Firefox(options)
