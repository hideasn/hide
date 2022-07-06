# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : pre_handle_utils.py
# @Software: PyCharm
# @time: 2022/7/5 13:35
# @description :
import json
import re
import os

from common_utils.global_vars import GLOBAL_VARS
from common_utils.yaml_handle import basic_yaml_data
from string import Template
# from common_utils.logger_handle import logger
from outputs.Logs.log_handle import get_log
from common_utils.allure_step import allure_step
from common_utils.exec_default_func import exec_func

logger = get_log(os.path.split(__file__)[-1])


def pre_expr_handle(content):
    """

    :param content: 原始的字符串
    :return content: 替换表达式后的字符串
    """
    if content is None:
        return None
    if len(content) != 0:
        logger.info(f"开始进行字符串替换：替换字符串为： {content}")
        content = Template(str(content)).safe_substitute(GLOBAL_VARS)
        for func in re.findall("\\${(.*?)}", content):
            try:
                content = content.replace("${%s}" % func, exec_func(func))
            except Exception as e:
                logger.exception(e)
        logger.info(f"字符串替换完成：替换字符串后为：{content}")

        return content


# 将"[1,2,3]" 或者"{'k':'v'}" -> [1,2,3], {'k':'v'}
def str_to_python(content) -> object:
    if content is None:
        return None

    if isinstance(content, str) and len(content) > 0:
        return eval(content)
    else:
        return content


class RequestPreDataHandle:

    def __init__(self, request_data):
        self.request_data = request_data
        self.host = basic_yaml_data["host"]      # {'host': 'http://localhost:8080/', 'case': 1}
        print(self.host)

    def _url_handle(self):
        url = str(pre_expr_handle(self.request_data.get("url", "")))
        logger.info(f"处理请求前url: {url}")
        host = self.host
        if url.lower().startswith("http"):
            self.request_data["url"] = url
        else:
            if host.endswith("/") or url.startswith("/"):
                self.request_data["url"] = host+url
            else:
                self.request_data["url"] = host + "/" + url
        allure_step("请求地址", self.request_data["url"])
        logger.info(f"处理请求后url : {self.request_data['url']}")

    def _header_handle(self):
        allure_step("请求头处理", self.request_data.get("header", None))
        if self.request_data.get("header", None):
            logger.info(f"处理请求前头: {self.request_data.get('header', None)}")
            self.request_data["header"] = str_to_python(pre_expr_handle(self.request_data.get("header", None)))
            logger.info(f"处理请求后头: {self.request_data['header']}")

    def _data_handle(self):
        allure_step("请求data", self.request_data.get("data", None))
        if self.request_data.get("data", None):
            logger.info(f"处理请求前data：{self.request_data.get('data', None)}")
            self.request_data["data"] = str_to_python(pre_expr_handle(self.request_data.get("data", None)))
            logger.info(f"处理请求后data: {self.request_data['data']}")

    def _file_handle(self):
        """
        格式：接口中文件参数的名称： “文件地址路径：/["文件地址1", "文件地址2"]”
        :return:
        """
        files = self.request_data.get("file", None)
        allure_step("请求files", files)
        logger.info(f"处理请求前files: {files}")

        if files is None:
            return None

        if files != "" and files is not None:
            files = eval(files)
            for k, v in files.items():
                # 多文件上传
                if isinstance(v, list):
                    files = []
                    for path in v:
                        files.append((k, open(path, "rb")))
                else:
                    # 单文件上传
                    files = {k: open(v, "rb")}

        self.request_data["files"] =files
        logger.info(f"处理请求后files: {self.request_data['files']}")

    def _extract_handle(self):
        allure_step("请求后置提取参数", self.request_data.get("extract", None))
        if self.request_data.get("extract", None):
            logger.info(f"处理请求后置提取参数： {self.request_data.get('extract', None)}")
            self.request_data["extract"] = str_to_python(self.request_data.get("extract", None))
            logger.info(f"处理请求后置提取参数： {self.request_data['extract']}")

    def _validate_handle(self):
        allure_step("请求预期结果", self.request_data.get("validate", None))
        if self.request_data.get("validate", None):
            logger.info(f"预期结果处理前： {self.request_data.get('validate', None)}")
            self.request_data["validate"] = str_to_python(self.request_data.get('validate', None))
            logger.info(f"预期结果处理后： {self.request_data['validate']}")

    @property
    def to_request_data(self):
        self._url_handle()
        self._header_handle()
        self._data_handle()
        self._file_handle()
        self._validate_handle()
        self._extract_handle()

        return self.request_data



if __name__ == '__main__':
    # RequestPreDataHandle()
    loads = json.loads("{'name': 'hide'}")
    print(loads)
