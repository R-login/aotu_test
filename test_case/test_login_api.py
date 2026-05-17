#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/11 14:41
#接口自动化用例，支持参数化读取各类文件，完成接口请求、断言状态码、响应字段校验、数据库结果比对
import allure
from utils.api_request_util import ApiRequet
import pytest
from utils.api_list import ApiList
from utils.assert_util import Assert
from utils.data_util import DataUtil
from utils.backend_simulator import BackendSimulator
from utils.customer_db import CustomerDb
@allure.feature("接口测试")
class TestUserApi:

    data = DataUtil.read_data("user_api.json")

    @pytest.mark.user_api
    @pytest.mark.parametrize("case",data)
    @allure.step("登录接口")
    def test_login_api(self, api_login, case):
        name = case["customername"]
        code = case["code"]
        allure.dynamic.title(f"传入客户姓名{name}")
        print("拿到token -> ", api_login)
        url = ApiList.post_list()
        response = ApiRequet.post(url=url, json=case)
        Assert.api_equal_code(response, code)
        BackendSimulator.save_customer_to_db(case)
        Assert.api_contains_key(response, "customername")
        db_data = CustomerDb.query_execute("customername", case["customername"])
        assert case["customerphone"] == db_data[0]["customerphone"]