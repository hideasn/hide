# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : test_log_demo.py
# @Software: PyCharm
# @time: 2022/7/5 11:23
# @description :
from common_utils.logger_handle import logger


def test_log():
    i = "asd"
    logger.info('*'* 12)


if __name__ == '__main__':
    test_log()