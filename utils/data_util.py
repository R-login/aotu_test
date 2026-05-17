#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/4 15:39
#通用数据读取工具，支持Excel/CSV/JSON/YAML四种测试数据格式，统一返回列表嵌套字典
import json
import yaml
import pandas as pd
import os
from typing import List,Dict


class DataUtil :

    @staticmethod
    def list_excell():
        aotu_path = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(aotu_path, "data")
        logindata_path = os.path.join(data_path, "login_data.xlsx")
        data = pd.read_excel(logindata_path, engine="openpyxl")
        data = data.dropna(axis=0, how="all")
        return data.values.tolist()

    @staticmethod
    def read_data(file_name:str) -> List[Dict]:
        """
        支持excel/csv/json/yaml后缀的文件读取
        :param file_name: 文件名
        :return: 列表嵌套字典形式的数据
        """
        aotu_path = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(aotu_path, "data")
        file_path = os.path.join(data_path, file_name)
        suffix = file_name.split(".")[-1]
        if suffix == "csv":
            data = pd.read_csv(file_path, encoding="utf-8")
            return data.to_dict("records")

        elif suffix == "xlsx" or suffix == "xls":
            data = pd.read_excel(file_path, engine="openpyxl")
            data = data.dropna(axis=0, how="all")
            return data.to_dict("records")

        elif suffix == "json":
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data

        elif suffix == "yaml":
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            return data if isinstance(data, list) else [data]

        else:
            raise ValueError("文件格式不支持")


print(DataUtil.read_data("login.csv"))