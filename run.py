# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : run.py
# @Software: PyCharm
# @time: 2022/7/6 13:49
# @description :
import os
import shutil
import pytest

from common_utils.api_path import auto_gen_case_path
from common_utils.case_handle import get_case_data


def run():
    # 生成case在执行
    if os.path.exists(auto_gen_case_path):
        shutil.rmtree(auto_gen_case_path)

    get_case_data()  #

    if os.path.exists('outputs/reports/'):
        shutil.rmtree(path='outputs/reports/')

    # 本地调式执行
    pytest.main(args=['-s', '--alluredir=outputs/reports'])
    # 自动以服务形式打开报告
    # os.system('allure serve outputs/reports')

    # 本地生成报告
    os.system('allure generate outputs/reports -o outputs/html --clean')
    shutil.rmtree(auto_gen_case_path)


if __name__ == '__main__':
    run()