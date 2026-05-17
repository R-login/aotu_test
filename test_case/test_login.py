#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 12:35
#传统PO模式登录UI用例，支持读取Excel、json、yaml、csv
# 格式传参执行用例，执行测试步骤，断言关键字段值和类型、和数据库双重断言，添加allure全流程报告
import time

import allure
import pytest
from page.login_page import LoginPage
from utils.assert_util import Assert
from utils.data_util import DataUtil
from utils.log_util import LogUtil
from utils.exception_catch_util import exception_catch

@allure.feature("登录测试")
class TestLogin:

   data = DataUtil.read_data("login_data.xlsx")


   @allure.severity("blocker")
   @allure.description("不同的账号密码登录")
   @allure.tag("登录功能")
   @allure.story("首页登录")
   @allure.step("断言列表")
   @pytest.mark.parametrize("case", data)
   @pytest.mark.login
   def test_login(self, driver, config, case):
       username = case["username"]
       passwd = case["passwd"]
       allure.dynamic.title(f"登录测试：\n账号：{username}\n"
                            f"密码：{passwd}")
       login = LoginPage(driver)
       login.username_input(username)
       login.password_input(passwd)
       login.submit_click()
       print(config["tag"])
       Assert.assert_contains(driver.current_url, "inventory.html")


