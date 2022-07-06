# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : data_handle.py
# @Software: PyCharm
# @time: 2022/7/6 11:09
# @description :
import re
import os

from jsonpath import jsonpath
from outputs.Logs.log_handle import get_log

logger = get_log(os.path.split(__file__)[-1])


# 提取参数
def json_extractor(obj: dict, expr: str = ".") -> object:
    """
    :param obj: json/dict数据类型
    :param expr: 表达式， .提取字典所有内容， $.test_case 提取一级字典case，$.test_case.data 提取case字典下的data
    :return: 提取的结果，未提取到返回 None
    """

    try:
        result = jsonpath(obj, expr)[0]
        logger.info(f"提取响应内容成功,提取表达式为: {expr}, 提取值为: {result}")
    except Exception as e:
        logger.exception(e)
        logger.exception(f"未提取到内容，请检查表达式是否错误！提取表达式为：{expr}, 提取数据为：{obj}")
        result = None
    return result


# str类型数据参数提取
def re_extract(obj: str, expr: str=".") ->object:
    """
    :param obj: str类型数据
    :param expr: 正则表达式
    :return: 取的结果，未提取到返回 None
    """
    try:
        result = re.findall(expr, obj)[0]
    except Exception as e:
        logger.exception(e)
        logger.exception(f"未提取到内容,请检查表达式是否错误！提取表达式为：{expr}, 提取数据为{obj}")
        result = None
    return result