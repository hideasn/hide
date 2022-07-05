# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : base.py
# @Software: PyCharm
# @time: 2022/6/30 18:31
# @description :
import requests


class Base:
    session = None

    @classmethod
    def get_session(cls):
        if cls.session is None:
            cls.session = requests.session()
        return cls.session



