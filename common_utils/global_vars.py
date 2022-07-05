# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : global_vars.py
# @Software: PyCharm
# @time: 2022/7/4 11:31
# @description : 全局变量参数
from enum import Enum

# 定义一个全局变量，用于接口关联参数存储
GLOBAL_VARS = {}


# EXCEL 表头
class CaseEnum(Enum):
    CASE_ID = 1         # 用例编号
    CASE_FEATURE = 2    # 模块
    CASE_TITLE = 3      # 用例标题
    API_PATH = 4        # 接口地址
    API_HEADER = 5      # 请求头
    API_METHOD = 6      # 请求方式
    API_PK = 7          # 入参关键字
    API_DATA = 8        # 请求数据
    API_FILE = 9        # 文件上传
    API_EXTRACT = 10    # 参数提取
    API_EXPECTED = 11   # 预期结果
    API_EXEC = 12       # 是否执行


class CaseType(Enum):
    EXCEL = 1           # excel文件
    YAML = 2            # yaml文件
    ALL = 0


