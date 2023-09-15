"""
@FileName：errhandler.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/5 17:01\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import time


def err_handler(func):
    """
    @err_hadler是个注解
    :return:
    """

    def wrapper(*args):
        start = time.clock()
        print(func)
        # noinspection PyBroadException
        try:
            func(*args)  # 对包裹的函数进行处理
        except BaseException as e:
            print("get", e)
            if isinstance(e, Exception):  # 判断抛出的错误是不是自定义的错误，使用继承
                print("继承")
                return
            else:
                print("模板不对")
                return

        else:
            print("无异常")
        end = time.clock()
        print('used:', end - start)

    return wrapper
