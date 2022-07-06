# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : assert_util.py
# @Software: PyCharm
# @time: 2022/7/6 13:58
# @description : 断言封装
import os

from requests import Response

from common_utils.allure_step import allure_step
from common_utils.data_handle import json_extractor, re_extract
from outputs.Logs.log_handle import get_log
from request_utils.after_handle_utils import response_type

logger = get_log(os.path.split(__file__)[-1])


# def assert_result(response: Response, expected: str) -> None:
#     """
#     断言封装
#     :param response: 实际响应对象
#     :param expected: 预取结果，从excel/yaml读取，或者手动传入
#     :return: None
#     """
#     if expected is None:
#         logger.info("当前无用例断言")
#         return
#
#     if isinstance(expected, str):
#         expect_dict = eval(expected)
#     else:
#         expect_dict = expected
#     index = 0
#     for k, v in expect_dict.items():
#         # 获取需要断言的实际结果部分
#         for _k, _v in v.items():
#             if _k == "http_code":
#                 actual = response.status_code
#             else:
#                 if response_type(response) == "json":
#                     actual = json_extractor(response.json(), _k)
#                 else:
#                     actual = re_extract(response.text, _k)
#                 index += 1
#                 logger.info(f"第{index}个断言数据, 实际结果: {actual} | 预期结果: {_v} 断言方式: {k}")
#                 allure_step(f"第{index}个断言数据", f"实际结果: {actual} == 预期结果: {v}")
#                 try:
#                     if k == "eq":  # 等于
#                         assert actual == _v
#                     elif k == "in":  # 包含
#                         assert _v in actual
#                     elif k == "gt":  # 判断大于, 值应为数值型
#                         assert actual > _v
#                     elif k == "lt":  # 判断小于，值应为数值型
#                         assert actual < _v
#                     elif k == "not":  # 不等于，非
#                         assert actual != _v
#                     else:
#                         logger.exception(f"判断关键字: {k} 错误")
#                 except AssertionError:
#                     raise AssertionError(f"第{index}个断言失败！断言方式: {k}, 实际结果: {actual} || 预期结果: {_v}")


def assert_result(response: Response, expected: str) -> None:
    """ 断言方法
    :param response: 实际响应对象
    :param expected: 预期响应内容，从excel中或者yaml读取、或者手动传入
    return None
    """
    if expected is None:
        logger.info("当前用例无断言！")
        return

    if isinstance(expected, str):
        expect_dict = eval(expected)
    else:
        expect_dict = expected
    index = 0
    for k, v in expect_dict.items():
        # 获取需要断言的实际结果部分
        for _k, _v in v.items():
            if _k == "http_code":
                actual = response.status_code
            else:
                if response_type(response) == "json":
                    actual = json_extractor(response.json(), _k)
                else:
                    actual = re_extract(response.text, _k)
            index += 1
            logger.info(f'第{index}个断言数据,实际结果:{actual} | 预期结果:{_v} 断言方式：{k}')
            allure_step(f'第{index}个断言数据', f'实际结果:{actual} = 预期结果:{v}')
            try:
                if k == "eq":  # 相等
                    assert actual == _v
                elif k == "in":  # 包含关系
                    assert _v in actual
                elif k == "gt":  # 判断大于，值应该为数值型
                    assert actual > _v
                elif k == "lt":  # 判断小于，值应该为数值型
                    assert actual < _v
                elif k == "not":  # 不等于，非
                    assert actual != _v
                else:
                    logger.exception(f"判断关键字: {k} 错误！")
            except AssertionError:
                raise AssertionError(f'第{index}个断言失败 -|- 断言方式：{k} 实际结果:{actual} || 预期结果: {_v}')