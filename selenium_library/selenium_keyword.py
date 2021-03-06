import time
from selenium import webdriver
from selenium.webdriver import ActionChains


def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


def open_headless_browser():
    try:
        chrome_less = webdriver.ChromeOptions()
        chrome_less.add_argument('--headless')
        chrome_less.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_less)
    except Exception as e:
        print(e)
        print('Opening Chrome browser')
        driver = webdriver.Chrome()
    return driver


class SeleniumKey:
    def __init__(self, type_=None, headless=False):
        if headless is True:
            self.driver = open_headless_browser()
        self.driver = open_browser(type_)

    def open(self, txt):
        """
        Input URL and open website
        :param txt: URL
        """
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

    def wait(self, txt):
        self.driver.implicitly_wait(txt)

    def assert_text(self, name, value, expect: str):
        try:
            reality = self.locator(name, value).text
            assert reality == expect
            return True
        except AssertionError:
            return False

    def assert_exit(self, name, value, expect: bool):
        try:
            reality = self.locator(name, value)
            assert reality == expect
            return True
        except AssertionError:
            return False

    def run_js_script(self, txt):
        self.driver.execute_script(txt)

    def refresh(self):
        self.driver.refresh()

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    def full_screen(self):
        self.driver.fullscreen_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def set_window_position(self, x, y):
        self.driver.set_window_position(x, y)

    def forward(self):
        self.driver.forward()

    def backward(self):
        self.driver.back()

    def clear(self, name, value):
        self.locator(name, value).clear()

    def submit(self, name, value):
        self.locator(name, value).submit()

    def right_click(self, name, value):
        ActionChains(self).context_click(self.locator(name, value)).perform()

    def double_click(self, name, value):
        ActionChains(self).double_click(self.locator(name, value)).perform()

    def scroll_top(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.run_js_script(js)

    def scroll_bottom(self):
        js = "var q=document.documentElement.scrollTop=100000"
        self.run_js_script(js)

    def scroll_to(self, x, y):
        js = "window.scrollTo({},{})".format(x, y)
        self.run_js_script(js)

    def switch_window(self, txt):
        self.driver.switch_to.window(txt)

    def switch_frame(self, txt):
        self.driver.switch_to.frame(txt)

    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def input_alert(self, txt):
        self.driver.switch_to.alert.send_keys(txt)

    def page_timeout(self, txt):
        self.driver.set_page_load_timeout(txt)

    def script_timeout(self, txt):
        self.driver.set_script_timeout(txt)

    def screenshot(self):
        pass