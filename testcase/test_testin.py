"""
@FileName：test_testin.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/5 11:36\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
from time import sleep
import allure
import pytest

from base.ReadFakerData import read_excel_with_titles
from po.login import LoginPage
from selenium import webdriver


@pytest.fixture(scope="class", autouse=False, params=["mysql", "redis"])
def set():
    print("baserequest start")
    yield
    print("关闭数据链接")


@allure.epic("登录接口")
@allure.feature("登录模块")
class TestTestIn:

    # 打开浏览器
    def setup(self) -> None:
        self.driver = webdriver.Edge('D:\\pythonfile\\webdriver\\MicrosoftWebDriver.exe')

    # 关闭浏览器
    def teardown(self) -> None:
        sleep(1)
        self.driver.close()

    '''利用excel导入登录测试数据'''

    @allure.story("登录接口")
    @pytest.mark.parametrize(["username", "password"],
                             read_excel_with_titles('D:\\pythonfile\\SaasTestv1.0.1\\data\\data.xlsx', 'username',
                                             'password'))
    def test_01_login(self, username, password, set):
        '''测试登录模块'''
        lp = LoginPage(self.driver)
        lp.testin_login(username, password)
    # @pytest.mark.smoke
    # def test_01_select_huawei(self):
    #     """测试选取华为手机"""
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_05_huawei_list()

    # def test_02_select_iphone_12(self):
    #     '''测试根据品牌选择手机'''
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_01_iphone()
    #
    # def test_03_select_androi_sys(self):
    #     '''测试根据安卓系统选择手机'''
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_02_android()
    #
    # def test_04_select_online_time(self):
    #     '''测试根据上市时间来选择手机'''
    #     lp = LoginPage(self.driver)
    #     lp.testin_login()
    #     ps = SelectPage(self.driver)
    #     ps.testin_select_03_onlin_time()
