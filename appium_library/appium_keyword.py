import time
from appium import webdriver
from yaml_driver.yaml_read import get_caps


def remote(config_path, port='http://127.0.0.1:4723/wd/hub'):
    desired_caps = get_caps(config_path)
    driver = webdriver.Remote(port, desired_caps)
    return driver


class AppiumKey:
    def __init__(self, port, config_path):
        self.driver = remote(port, config_path)

    def sleep(self, txt):
        time.sleep(txt)

    def locator(self, name, value):
        self.driver.find_element(name, value)

    def quit(self):
        self.driver.quit()
