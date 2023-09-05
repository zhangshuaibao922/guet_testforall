"""
@FileName：GetFakerData.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/1 15:59\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import os
from xlutils.copy import copy
import yaml
from faker import Faker
import xlrd


class GetFakerData:
    faker = None
    __name="dc"
    ''''
    faker data is a packet support users to create faker datas to test your
    project, our group create this object to help developer get lots of datas
    and translate them to different form 
    from my point of view , l am glad to show the possible example to you

    '''

    def __init__(self, *args):
        if args is not None:
            self.faker = Faker(args)
        else:
            self.faker = Faker(locale='zh_CN')

    # it is just a simple example,you can use dict type or list type
    ''''
    as you use get_faker_users_dict()
    return  [{'name': '张彬', 'phone': '13863071236'}] type is dict
    '''

    def get_faker_users_dict(self, num=1):
        uer_list = []
        user = {"name": self.faker.name(),
                "phone": self.faker.phone_number()}
        # print(type(user))
        if num == 1:
            return user
        for i in range(num):
            user = {"name": self.faker.name(),
                    "phone": self.faker.phone_number()}
            uer_list.append(user)
        return uer_list

    ''''
    as you use get_faker_users()
    return  [['谢晶', '13090997767']] type is list
    '''

    def get_faker_users(self, num=1):
        uer_list = []
        user = [self.faker.name(),
                self.faker.phone_number()]
        # print(type(user))
        if num == 1:
            return user
        for i in range(num):
            user = [self.faker.name(),
                    self.faker.phone_number()]
            uer_list.append(user)
        return uer_list

    @staticmethod
    def write_faker_data_to_yaml(data: list, addr=None):
        print(type(data))
        if addr is None:
            raise Exception("addr can not be none")
        with open(addr, encoding="utf-8", mode='a+') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    @staticmethod
    def write_faker_data_to_excel(data: list, addr=None):
        """写入excel"""
        index = len(data)  # 获取需要写入数据的行数
        workbook = xlrd.open_workbook(addr)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        for i in range(0, index):
            for j in range(0, len(data[i])):
                new_worksheet.write(i + 1, j, data[i][j])  # 从第一行开始写
                new_worksheet.write(i + rows_old - 1, j, data[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
        new_workbook.save(addr)  # 保存工作簿
        # print("xls格式表格【覆盖数据前%s行】写入数据成功！" % index)

    @staticmethod
    def static_method():
        print("this is the GetFakerData's static method")


if __name__ == '__main__':
    # GetFakerData().static_method()
    print(os.getcwd())
    dir_excel = os.getcwd() + "\\test.xls"
    dir_yaml = os.getcwd() + "\\test.yaml"

    users = GetFakerData('zh_cn').get_faker_users(4)

    print(users)
    GetFakerData().write_faker_data_to_excel(users, dir_excel)
    GetFakerData.write_faker_data_to_yaml(GetFakerData('zh_cn').get_faker_users_dict(4), dir_yaml)
    print(GetFakerData('').get_faker_users())
