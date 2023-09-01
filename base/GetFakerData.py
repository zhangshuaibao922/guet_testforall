"""
@FileName：GetFakerData.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/1 15:59\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import yaml
from faker import Faker


class GetFakerData:
    faker = None
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
    def write_faker_data_to_excel(data: list, addr=None, ):
        print(type(data))
        if addr is None:
            raise Exception("addr can not be none")
        with open(addr, encoding="utf-8", mode='a+') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    @staticmethod
    def static_method():
        print("this is the GetFakerData's static method")


if __name__ == '__main__':
    # GetFakerData().static_method()
    print(GetFakerData('zh_cn').get_faker_users_dict(4))
    users = GetFakerData('zh_cn').get_faker_users_dict(4)
    GetFakerData.write_faker_data_to_excel(users, "D:\\pythonfile\\SaasTestv1.0.1\\\extract.yaml")
    print(GetFakerData('').get_faker_users())
