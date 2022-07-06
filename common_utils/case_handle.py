# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : case_handle.py
# @Software: PyCharm
# @time: 2022/7/6 11:24
# @description :
import os

from common_utils.excel_handle import ReadExcel
from common_utils.global_vars import CaseType
from common_utils.yaml_handle import basic_yaml_data, YamlHandle
from common_utils.api_path import data_path
from common_utils.gen_case import gen_case


def get_case_data():
    case_type = basic_yaml_data["case"]
    # 读取excel
    if case_type == CaseType.EXCEL.value:
        cases = []
        for file in [excel for excel in os.listdir(data_path) if os.path.splitext(excel)[1] == ".xlsx"]:
            data = ReadExcel(data_path + file).read_excel()
            name = os.path.splitext(file)[0]
            class_name = name.split("_")[0].title() + name.split("_")[1].title()
            gen_case(name, data, class_name)
            cases.extend(data)

    elif case_type == CaseType.YAML.value:
        cases = []
        for yaml_file in [yaml for yaml in os.listdir(data_path) if os.path.splitext(yaml)[1] in [".yaml", "yml"]]:
            data = YamlHandle(data_path + yaml_file).read_yaml()
            name = os.path.splitext(yaml_file)[0]
            class_name = name.split("_")[0].title() + name.split("_")[1].title()
            gen_case(name, data, class_name)
            cases.extend(data)
        return cases
    else:
        cases = []
        for file in [excel for excel in os.listdir(data_path) if os.path.splitext(excel)[1] in [".yaml", "yml", "xlsx"]]:
            if os.path.splitext(file)[1] == ".xlsx":
                data = ReadExcel(data_path + file).read_excel()
                name = os.path.splitext(file)[0]
                cases.extend(data)
            else:
                data = YamlHandle(data_path + file).read_yaml()
                name = os.path.splitext(file)[0]
                cases.extend(data)

            class_name = name.split("_")[0].title() + name.split("_")[1].title()
            gen_case(name, data, class_name)
        return cases
