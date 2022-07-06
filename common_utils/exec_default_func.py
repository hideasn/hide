# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : exec_default_func.py
# @Software: PyCharm
# @time: 2022/7/5 17:34
# @description :

def exec_func(func: str) -> str:
    """
    exec 执行储存在字符串或文件中的 Python 语句,且返回结果永远为None
    :param func:
    :return:
    """
    result = exec(f"{func}")
    return str(result)
    