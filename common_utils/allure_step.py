# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : allure_step.py
# @Software: PyCharm
# @time: 2022/7/5 13:22
# @description :
import allure
import json


# allure报告动态标题
def allure_title(title):
    # allure报告中显示的用例标题
    allure.dynamic.title(title)


'''
step_title:步骤及附件名称
content: 附件内容
'''


def allure_step(step_title, content):
    with allure.step(step_title):
        allure.attach(json.dumps(content, ensure_ascii=False, indent=4), step_title, allure.attachment_type.TEXT)