"""
=======================|
Author:76              | 
Time:2021/5/4  20:24  |
=======================|
"""
import unittest
import os
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from register import register
from common.handle_log import log
from common.handle_path import DATA_DIR


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'wb1.xlsx'), 'register')
    datas = excel.read_excel()

    @list_data(datas)
    def test_register(self, item):
        # 准备测试数据
        params = eval(item['params'])
        expected = eval(item['expected'])
        rows = item['case_id'] + 1
        # 请求函数
        res = register(**params)
        # 断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_excel(row=rows, column=5, value='未通过')
            log.error('用例---【{}】---执行失败'.format(item['title']))
            log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=rows, column=5, value='通过')
            log.error('用例---【{}】---执行成功'.format(item['title']))
