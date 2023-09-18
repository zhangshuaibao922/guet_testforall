"""
@FileName：BaseAppPage.py\n
@Description：：基础appium页面(baseappiumpage)的二次封装，主管web自动化\n
@Author：Mr.Dc\n
@Time：2023/9/18 10:48\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import time

from appium import webdriver

from config import Config


class BaseAppPage(object):
    driver = None  # type: webdriver

    def __init__(self):
        config = Config.Config()
        # todo 将config.ini的东西读取字典化加到desired_caps中
        # dir = dict()
        # dir.setdefault(1,2)
        print(dir)
        desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.2', 'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.xunmeng.pinduoduo',
                        'appActivity': 'com.xunmeng.pinduoduo.ui.activity.MainFrameActivity', 'noReset': True,
                        'unicodeKeyboard': True, 'resetKeyboard': True}
        print(type(config.get_conf('appium_example', "desired_caps")))

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    @staticmethod
    def quit_app_driver(self=None):
        if self.driver is None:
            self.driver.close()


if __name__ == '__main__':
    print("11")
