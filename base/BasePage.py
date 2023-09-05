"""
@FileName：BasePage.py\n
@Description：基础selenium页面\n
@Author：Mr.Dc\n
@Time：2023/9/5 11:28\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver.Edge):
        self.driver = driver

    # 打开页面
    def into_testin(self, url):
        self.driver.get(url)

    # 定位元素
    def locate_element(self, args):
        return self.driver.find_element(*args)

    # 定位一组元素
    def locate_eles(self, args):
        return self.driver.find_elements(*args)

    # 从一组元素中获取值
    def gettext_from_eles(self, args):
        elements = self.locate_eles(args)
        data = []
        try:
            for ele in elements:
                data.append(ele.text)
        except Exception as e:
            e("从一组中获取元素失败")
        print(data)
        return data

    #
    def getele_from_eles(self, args, ele_name: str):
        elements = self.locate_eles(args)
        try:
            for ele in elements:
                if str.__contains__(ele.text, ele_name):
                    return ele
        except Exception as e:
            e("从一组中获取元素失败")
        return None

    # 输入值
    def input_(self, args, text):
        self.locate_element(args).send_keys(text)

    # 点击按钮
    def click_button(self, args):
        self.locate_element(args).click()
