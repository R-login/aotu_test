#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/8 15:48
#关键字驱动用例、参数化读取用例数据，参数化读取csv步骤数据，无代码编写即可完成自动化流程
import os
import allure
import pytest
import pandas as pd
from utils.data_util import DataUtil
from keywords.keyword_engine import KeywordEngine

@allure.feature("登录-企业版关键字驱动")
class TestLoginKey:
    case_list = DataUtil.read_data("login_data.xlsx")

    @pytest.mark.parametrize("case", case_list)
    @allure.severity("blocker")
    @pytest.mark.login_key
    def test_login_flow(self, driver, config, case):
        username = case["username"]
        pwd = case["passwd"]  # ✅ 修复这里
        allure.dynamic.title(f"关键字登录：{username}")

        # 读取CSV流程（放到方法内，不提前加载报错）
        flow_path = os.path.join(os.path.dirname(__file__), "../data/keyword_flow.csv")
        keyword_flow = pd.read_csv(flow_path, encoding="utf-8").to_dict("records")


        engine = KeywordEngine(driver)

        for step in keyword_flow:
            kw = step["keyword"]
            loc_t = step["loc_type"]
            loc_v = step["loc_value"]
            args = step["args"]

            # ======================
            # 注入账号密码
            # ======================
            if kw == "输入文本" and loc_v == "user-name":
                args = username
            if kw == "输入文本" and loc_v == "password":
                args = pwd

            engine.run_step(kw, loc_t, loc_v, args)