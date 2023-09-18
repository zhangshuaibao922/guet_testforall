"""
@FileName：HomePage.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/18 11:14\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""

from appium import webdriver

from base.BaseAppPage import BaseAppPage


class HomePage(BaseAppPage):

    def __init__(self):
        super().__init__()

    def getdriver(self):
        id_class = 'resourceId("com.xunmeng.pinduoduo:id/pdd").className("android.widget.TextView")'
        self.driver.find_element_by_android_uiautomator(id_class)
        self.driver.find_element_by_android_uiautomator(id_class).click()


if __name__ == '__main__':
    page = BaseAppPage()
    page.__init__()
    page.get_window_size()
