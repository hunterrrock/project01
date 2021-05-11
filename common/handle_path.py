"""
=======================|
Author:76              | 
Time:2021/5/6  22:38  |
=======================|

此模块专门用来处理项目中的绝对路径

"""
import os

# 项目的根目录路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例数据所在目录的路径
DATA_DIR = os.path.join(BASE_DIR, 'datas')

# 配置文件所在目录的路径

CONFIG_DIR = os.path.join(BASE_DIR, 'conf')

# 日志文件所在目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 用例模块所在目录
CASES_DIR = os.path.join(BASE_DIR, 'testcase')
