# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : test_demo.py
# @Software: PyCharm
# @time: 2022/7/6 13:58
# @description :
import allure
import pytest

from common_utils.allure_step import allure_title
from common_utils.assert_util import assert_result
from request_utils.base_request import BaseRequest
from common_utils.excel_handle import ReadExcel
from common_utils.api_path import data_path
from common_utils.global_vars import GLOBAL_VARS


@allure.feature("登录")
class TestLogin:


    '''
    @allure.severity 用例等级
    allure对用例的等级划分成五个等级:
        blocker　 阻塞缺陷（功能未实现，无法下一步）
        critical　　严重缺陷（功能点缺失）
        normal　　 一般缺陷（边界情况，格式错误）
        minor　 次要缺陷（界面错误与ui需求不符）
        trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
    '''
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('data', ReadExcel(data_path + "test_case.xlsx").read_excel())
    def test_login(self, data):
        allure_title("正常登录")
        print(data)
        # data = {
        #     "title": "正常登录",
        #     "url": "bank/api/login",
        #     "method": "post",
        #     "pk": "data",
        #     "data": {"password": "123456", "userName": "king"}
        # }
        #
        # expected = {
        #     'eq': {'$.code': '0', '$.message': 'success'}
        # }
        expected = data["validate"]
        # 发送请求
        response = BaseRequest.send_request(data)
        print(response)
        print(GLOBAL_VARS)
        # 断言操作
        assert_result(response, expected)
