# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : base_request.py
# @Software: PyCharm
# @time: 2022/7/6 10:21
# @description :
import requests
import os
from requests import Response
from common_utils.allure_step import allure_step
# from common_utils.logger_handle import logger
from outputs.Logs.log_handle import get_log
from request_utils.after_handle_utils import after_extract
from request_utils.pre_handle_utils import RequestPreDataHandle

logger = get_log(os.path.split(__file__)[-1])


class BaseRequest:
    session = None

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.Session()
        return cls.session

    @classmethod
    def send_request(cls, case: dict) -> Response:
        """
        处理case数据，转换成可用数据发送请求
        :param case: 读取出来的每一行用例内容
        :return:
        """
        logger.info(f"开始执行用例：{case.get('title')}")
        req_data = RequestPreDataHandle(case).to_request_data
        res = cls.send_api(
            url=req_data["url"],
            method=req_data["method"],
            pk=req_data["pk"],
            header=req_data.get("header", None),
            data=req_data.get("data", None),
            file=req_data.get("file", None)
        )
        allure_step('请求响应数据', res.text)
        logger.info(f"请求响应数据{res.text}")
        after_extract(res, req_data.get("extract", None))

        return res

    @classmethod
    def send_api(cls, url, method, pk, header=None, data=None, file=None) -> Response:
        """
        :param url: 请求路径
        :param method: 请求方法
        :param pk: 入参关键字    params(查询参数类型，明文传输，一般在url?参数名=参数值), data(一般用于form表单类型参数) ,json
        :param header: 请求头
        :param data: 请求参数
        :param file: 文件对象
        :return: 返回res对象
        """
        session = cls.get_session()
        pk = pk.lower()
        if pk == "params":
            res = session.request(method=method, url=url, params=data, headers=header)
        elif pk == "data":
            res = session.request(method=method, url=url, data=data, files=file, headers=header)
        elif pk == "json":
            res = session.request(method=method, url=url, json=data, files=file, headers=header)
            print(res.json())
        else:
            raise ValueError("pk可选关键字为params, json, data")
        return res
