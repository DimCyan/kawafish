import time
from appium import webdriver


def remote(config):
    driver = webdriver.Remote(config)
    return driver


class AppiumKey:
    def __init__(self, config):
        self.driver = remote(config)