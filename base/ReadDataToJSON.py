# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 19:35
# @Author  : Zhangshuaibao
# @File    : test
"""
封装读取http请求配置方法
"""
import yaml
import json


class ReadDataToJSON:
    def __init__(self, path):
        """

        :param path:
        """
        self.stream = open(path, encoding="utf8")
        self.data = yaml.safe_load(self.stream)

    def read_yaml_body(self, type):
        """
        读取body数据
        :param configuration: 配置类型:body url method...
        :return: json数据
        """
        return json.dumps(self.data[type])

    # TODO 目前尚未做到支持excel表哥