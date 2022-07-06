# _*_ coding:utf-8 _*_

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : log_handle.py
# @Software: PyCharm
# @time: 2022/7/5 10:45
# @description : 日志处理
import logging
import time
import os


def get_log(logger_name):
    """
    :param logger_name: 日志名称
    :return: 返回logger handle
    """
    # 创建一个logger对象
    logger = logging.getLogger(logger_name)
    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 获取本地时间，转换为设置的格式
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))

    # 设置所有日志和错误日志的存放路径
    path = os.path.dirname(os.path.abspath(__file__))
    all_log_path = os.path.join(path, 'interface_logs\\All_Logs\\')
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)

    error_log_path = os.path.join(path, 'interface_logs\\Error_Logs\\')
    if not os.path.exists(error_log_path):
        os.makedirs(error_log_path)

    # 设置日志文件名
    all_log_name = all_log_path + rq + '.log'
    error_log_name = error_log_path + rq + '.log'

    if not logger.handlers:
        # 创建一个handler写入所有日志
        fh = logging.FileHandler(all_log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 创建一个handler写入错误日志
        eh = logging.FileHandler(error_log_name, encoding='utf-8')
        eh.setLevel(logging.ERROR)
        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        all_log_formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s - %(levelname)s - %(lineno)s - %(message)s')
        # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
        error_log_formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s - %(levelname)s - %(lineno)s - %(message)s')
        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

    return logger
