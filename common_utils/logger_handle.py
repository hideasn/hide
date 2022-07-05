# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : logger_handle.py
# @Software: PyCharm
# @time: 2022/7/5 11:05
# @description :
import logging
import os

from common_utils.yaml_handle import yaml_data
from common_utils.api_path import log_path

'''
封装思路：

首先分析一下，logging中哪些数据可以作为参数？比如日志器名称、日志等级、日志文件路径、输出格式，可以将这些放到__init__方法里，作为参数。
其次，要判断日志文件是否存在，存在就将日志输出到日志文件中。
最后，logging模块已经封装好了Logger类，可以直接继承，减少代码量。
'''


class LoggerHandle(logging.Logger):

    def __init__(self, name="root", level="DEBUG", file=None, format=None):
        # 设置日志收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志输出格式
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置日志处理器，输出到文件
        if file:
            file_handler = logging.FileHandler(file, encoding="utf-8")
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        # 设置StreamHandler，输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


# 从yaml文件读取配置
logger = LoggerHandle(
    name=yaml_data["logger"]["name"],
    level=yaml_data["logger"]["level"],
    file=log_path + os.sep + "my_log.txt",
    format=yaml_data["logger"]["format"]
)
