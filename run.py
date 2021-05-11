"""
=======================|
Author:76              | 
Time:2021/5/4  20:14  |
=======================|
"""
import unittest
from unittestreport import TestRunner
from common.handle_path import CASES_DIR,REPORT_DIR

suite = unittest.defaultTestLoader.discover(CASES_DIR)
runner = TestRunner(suite, filename="report.html",
                    report_dir=REPORT_DIR,
                    title='测试报告',
                    tester='yan',
                    desc="yan的测试报告")
runner.run()
