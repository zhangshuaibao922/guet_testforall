"""
@FileName：ReadFakerData.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/1 17:05\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import os

import xlrd


class ReadFakerData:
    @staticmethod
    def read_excel_with_titles_sheet_name(path, sheet_name: str, *args):
        s = set([])
        for arg in args:
            s.add(arg)
        data = set()
        sheet = xlrd.open_workbook(path)
        by_index = sheet.sheet_by_name(sheet_name)
        col = by_index.ncols
        for i in range(col):
            if s.__contains__(by_index.cell_value(0, i)):
                data.add(i)
                s.remove(by_index.cell_value(0, i))
        arg_all = []
        for i in range(1, by_index.nrows):
            arg_list = []
            for j in data:
                arg_list.append(by_index.cell_value(i, j))
            arg_all.append(arg_list)
        print(arg_all)
        return arg_all

    @staticmethod
    def read_excel_with_titles(path, *args):
        s = set([])
        for arg in args:
            s.add(arg)
        data = set()
        sheet = xlrd.open_workbook(path)
        by_index = sheet.sheet_by_index(0)
        col = by_index.ncols
        for i in range(col):
            if s.__contains__(by_index.cell_value(0, i)):
                data.add(i)
                s.remove(by_index.cell_value(0, i))
        arg_all = []
        for i in range(1, by_index.nrows):
            arg_list = []
            for j in data:
                arg_list.append(by_index.cell_value(i, j))
            arg_all.append(arg_list)
        print(arg_all)
        return arg_all


if __name__ == '__main__':
    dir_excel = os.getcwd() + '\\test.xls'
    ReadFakerData().read_excel_with_titles(dir_excel, "name")
