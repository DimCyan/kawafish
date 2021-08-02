import time
from appium import webdriver
from yaml_driver.yaml_read import get_caps


def remote(config_path='../config/android_config.yml', port='http://127.0.0.1:4723/wd/hub'):
    desired_caps = get_caps(config_path)
    driver = webdriver.Remote(port, desired_caps)
    return driver


class AppiumKey:
    def __init__(self, port=None, config_path=None):
        self.driver = remote(port, config_path)

    def sleep(self, txt):
        time.sleep(txt)

    def locator(self, name, value):
        self.driver.find_element(name, value)

    def quit(self):
        self.driver.quit()

    def wait(self, txt):
        self.driver.implicitly_wait(txt)

    def shake(self):
        self.driver.shake()

    def close(self):
        self.driver.close()

    def close_app(self):
        self.driver.close_app()

    def swipe(self, x1, y1, x2, y2):
        self.driver.swipe(x1, y1, x2, y2)

    def home(self):
        self.driver.keyevent(3)

    def back(self):
        self.driver.keyevent(4)

    def lock(self):
        self.driver.keyevent(26)

    def unlock(self):
        self.lock()