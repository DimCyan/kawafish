import os
import subprocess


class ADB(object):
    def __init__(self):
        v = subprocess.run(['adb', 'version'],
                           capture_output=True).stdout.decode('UTF-8').split('\n')
        try:
            while '' in v:
                v.remove('')
            print(f'ADB IS {v[2]}')
        except Exception as e:
            print(e)

    @classmethod
    def tap(cls, x, y):
        """
        Click on the simulation by using adb shell
        :param x: x location
        :param y: y location
        :return:
        """
        os.system(f'adb shell input tap {x} {y}')

    @classmethod
    def clear_app_data(cls, packages_name):
        """
        Clear the app data by using adb shell
        :param packages_name: app package name
        :return:
        """
        os.system(f'adb shell pm clear {packages_name}')

    @classmethod
    def data_disable(cls):
        os.system('adb shell svc data disable')

    @classmethod
    def data_enable(cls):
        os.system('adb shell svc data enable')

    @classmethod
    def screen_orientation_rotation(cls, i):
        """
        :param i: 0 or 1 or 2 or 3
        :return:
        """
        if i == 0 or i == 1 or i == 2 or i == 3:
            os.system(
                f'adb shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:{i}')
        else:
            raise Exception(f"Error value: {i}")

    @classmethod
    def send_keys(cls, text):
        """
        send keys by using adb shell(support input chinese text),please install ADBKeyBoard.apk and set it as android
        keyboard before using this method download -> https://github.com/senzhk/ADBKeyBoard
        :param text: str
        :return:
        """
        os.system(
            f"adb shell am broadcast -a ADB_INPUT_TEXT --es msg '{text}'")

    @classmethod
    def swipe(cls, x1, y1, x2, y2, time):
        """
        swipe method by using adb
        :param x1: x1 location
        :param y1: y1 location
        :param x2: x2 location
        :param y2: y2 location
        :param time: swipe duration time(ms)
        :return:
        """
        os.system(f'adb shell input swipe {x1} {y1} {x2} {y2} {time}')


if __name__ == '__main__':
    a = ADB()