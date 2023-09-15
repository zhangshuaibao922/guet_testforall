"""
@FileName：test.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/5 17:02\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import base
from errhandler.handler import err_handler


@err_handler
def teget():
    if 1 > 2:
        pass
    else:
        raise base.err.DataError("ggggg")


if __name__ == '__main__':
    teget()
