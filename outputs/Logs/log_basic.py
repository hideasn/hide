# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : log_basic.py
# @Software: PyCharm
# @time: 2022/7/5 9:42
# @description :
import logging


class LogBasic:

    def __init__(self):
        logging.debug("DEBUG")
        logging.info("info")
        # logging默认日志级别是warning 所以只会输出warning以及warning以上的级别日志
        # 输出内容格式说明：日志级别: 日志器名称:日志内容， 如果未自定义日志器名称，默认是root。
        logging.warning("warning-test")
        logging.error("error-test")
        logging.critical("critical-test")


def get_log(name):
    # 自定义日志收集器
    logger = logging.getLogger(name)
    # 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
    logger.setLevel(logging.DEBUG)

    # 设置日志格式
    fmt = logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')

    # 设置日志处理器 输出到文件
    file_handler = logging.FileHandler("./my_log.txt")
    # 设置日志处理器级别
    file_handler.setLevel(logging.DEBUG)
    # 日志处理器按照指定日志格式输出日志
    file_handler.setFormatter(fmt)

    # 日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)

    # 收集器和处理器对接，指定输出渠道
    # 日志输出到文件 (如果没有设置，不会输出日志到文件)
    logger.addHandler(file_handler)
    logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    # log_basic = LogBasic()
    log = get_log("hide")
    log.debug('自定义的debug日志')
    log.info('自定义的info日志')
    log.warning('自定义的warning日志')
    log.error('自定义的error日志')
    log.critical('自定义的critical日志')

