# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : api_path.py
# @Software: PyCharm
# @time: 2022/7/4 12:51
# @description : 路径封装
import os
from os.path import dirname, abspath

# 根路径
root_path = dirname(dirname(abspath(__file__)))

# 用例数据路径
data_path = root_path + os.sep + "data" + os.sep

# 用例执行路径
case_path = root_path + os.sep + "test_case" + os.sep

# 生成报告路径
auto_gen_case_path = root_path + os.sep + "outputs\generate_case" + os.sep

# 日志输出路径
log_path = root_path + os.sep + "outputs\Logs" + os.sep

# config路径
config_path = root_path + os.sep + "config" + os.sep


if __name__ == '__main__':
    print(auto_gen_case_path)