# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : gen_case.py
# @Software: PyCharm
# @time: 2022/7/6 13:25
# @description :
import os
from string import Template
from common_utils.api_path import auto_gen_case_path

case_template = """
import pytest
import allure
from common_utils.allure_step import allure_title
from common_utils.assert_util import assert_result
from request_utils.base_request import BaseRequest


@pytest.fixture(params=${case_data})
def data(request):
    return request.param


class ${class_name}:
    
    def ${case_title}(self, data):
        allure_title(data["title"])
        allure.dynamic.feature(data["feature"])
        response = BaseRequest.send_request(data)
        assert_result(response, data["validate"])

"""


def gen_case(name, case_data, class_name):
    if not os.path.exists(auto_gen_case_path):
        os.makedirs(auto_gen_case_path)
    my_case = Template(case_template).safe_substitute(
        {
            "case_data": case_data,
            "case_title": name,
            "class_name": class_name
        }
    )
    with open(auto_gen_case_path + name + ".py", "w", encoding="utf-8") as f:
        f.write(my_case)