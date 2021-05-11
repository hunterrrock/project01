"""
=======================|
Author:76              | 
Time:2021/5/4  19:39  |
=======================|
"""
import logging
import os
from common.handle_config import config
from common.handle_path import LOG_DIR


def create_log(name, level, filename, sh_level, fh_level):
    # 创建一个日志收集器
    log = logging.getLogger(name)
    # 设置日志收集器等级
    log.setLevel(level)
    # 创建日志输出渠道
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(filename, encoding='utf-8')
    # 为日志输出渠道设置等级
    s_h.setLevel(sh_level)
    f_h.setLevel(fh_level)
    # 绑定日志输出渠道到日志收集器上
    log.addHandler(s_h)
    log.addHandler(f_h)
    # 设置日志输出格式
    log_format = logging.Formatter('%(asctime)s-【%(filename)s】-->line:%(lineno)d-%(levelname)s:%(message)s')
    # 为日志输出渠道设置日志格式
    s_h.setFormatter(log_format)
    f_h.setFormatter(log_format)
    # 返回一个日志收集器
    return log


log = create_log(
    name=config.get('logging', 'name'),
    level=config.get('logging', 'level'),
    filename=os.path.join(LOG_DIR, config.get('logging', 'filename')),
    sh_level=config.get('logging', 'sh_level'),
    fh_level=config.get('logging', 'fh_level')

)
