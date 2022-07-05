# -*- coding: utf-8 -*-

# @version: v1.0
# @author : Hide
# @Project : hide
# @File : yaml_handle.py
# @Software: PyCharm
# @time: 2022/7/5 10:45
# @description : 读写yaml文件
import yaml


class YamlHandle:

    def __init__(self, filename):
        self.filename = filename

    '''
    读取
    '''
    def read_yaml(self, encoding="utf-8"):
        # 读取yaml数据
        with open(self.filename, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    '''
    写入
    '''
    def write_yaml(self, data, encoding="utf-8"):
        with open(self.filename, encoding=encoding, mode="w") as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


yaml_data = YamlHandle("../config/config.yaml").read_yaml()
basic_yaml_data = YamlHandle("../config/basic_config.yaml").read_yaml()

if __name__ == '__main__':
    read_yaml = YamlHandle("../config/config.yaml").read_yaml()
    print(type(read_yaml))
    print(read_yaml)
