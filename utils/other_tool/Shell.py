# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 17:58
# @Author  : Zhangshuaibao
# @File    : Shell

"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
