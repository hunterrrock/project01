"""
=======================|
Author:76              | 
Time:2021/5/4  17:56  |
=======================|
"""
import unittest
import os
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from login import login_check
from common.handle_log import log
from common.handle_path import DATA_DIR


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'wb1.xlsx'), 'login')
    datas = excel.read_excel()

    @list_data(datas)
    def test_login(self, item):
        # 准备测试数据
        params = eval(item['params'])
        expected = eval(item['expected'])
        rows = item['case_id'] + 1
        # 请求功能函数
        res = login_check(**params)
        # 断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_excel(row=rows, column=5, value='未通过')
            log.error('用例---【{}】----执行失败'.format(item['title']))
            log.exception(e)
            raise e
        else:
            self.excel.write_excel(row=rows, column=5, value='通过')
            log.info('用例---【{}】----执行通过'.format(item['title']))
