import time
from selenium import webdriver


def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class SeleniumKey:
    def __init__(self, type_=None):
        self.driver = open_browser(type_)

    def open(self, txt):
        self.driver.get(txt)

    def locator(self, name, value):
        return self.driver.find_element(name, value)

    def click(self, name, value):
        self.locator(name, value).click()

    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    def quit(self):
        self.driver.quit()

    def close_window(self):
        self.driver.close()

    def sleep(self, txt):
        time.sleep(txt)

    def assert_text(self, name, value, expect):
        try:
            reality = self.locator(name, value).text
            assert reality == expect
            return True
        except BaseException:
            return False

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    def forword(self):
        self.driver.forward()

    def backword(self):
        self.driver.back()

    def clear(self, name, value):
        self.locator(name, value).clear()

    def submit(self, name, value):
        self.locator(name, value).submit()
