"""
=======================|
Author:76              | 
Time:2021/5/4  19:45  |
=======================|
"""
import os
from configparser import ConfigParser
from common.handle_path import CONFIG_DIR

# config = ConfigParser()
# config.read(filenames=r'D:\PythonPoject\project01\conf\config.ini', encoding='utf-8')
# res =config.get('logging','name')
# print(res)


class Config(ConfigParser):
    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')


config = Config(os.path.join(CONFIG_DIR, 'config.ini'))

if __name__ == '__main__':
    config = Config(conf_file=r'D:\PythonPoject\project01\conf\config.ini')
    res = config.get('logging', 'name')
    print(res)
