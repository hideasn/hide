# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : after_handle_utils.py
# @Software: PyCharm
# @time: 2022/7/6 10:59
# @description :
from requests import Response

from common_utils.data_handle import json_extractor, re_extract
from common_utils.global_vars import GLOBAL_VARS


def after_extract(response: Response, exp: str) -> None:
    """

    :param response: request响应字典
    :param exp: 需要提取的参数字典  '{"k1": "$.data"}' 或 '{"k1": "data:(.*?)$"}'
    :return:
    """
    if exp:
        if response_type(response) == "json":
            res_json = response.json()
            for k, v in exp.items():
                GLOBAL_VARS[k] = json_extractor(res_json, v)
        else:
            res_text = response.text
            for k, v in exp.items():
                GLOBAL_VARS[k] = re_extract(res_text, v)


def response_type(response: Response) -> str:
    """
    :param response: requests返回
    :return: 返回响应数据类型 json或者str
    """
    try:
        response.json()
        return "json"
    except:
        return "str"