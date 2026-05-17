#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/8 15:47
import allure
import os
from page.base_page import BasePage
from utils.assert_util import Assert
from keywords.keyword_map import KEYWORD_MAPPING
#关键字执行引擎，读取流程步骤自动调度方法，支持动态替换账号密码（或舱保），实现流程化自动化

class KeywordEngine(BasePage):

    @allure.step("执行关键字步骤：{keyword}")
    def run_step(self, keyword, loc_type=None, loc_value=None, args=None):
        # 1. 中文转引擎方法名
        method_name = KEYWORD_MAPPING.get(keyword)
        if not method_name:
            raise ValueError(f"未定义关键字：{keyword}")

        # 2. 反射获取当前引擎的方法
        func = getattr(self, method_name)

        # 3. 分参数类型执行
        if method_name == "open_url":
            func(args)
        elif method_name == "input_text":
            locator = (loc_type, loc_value)
            func(locator, args)
        elif method_name == "click_elem":
            locator = (loc_type, loc_value)
            func(locator)
        elif method_name == "assert_url_contain":
            func(args)

    # ========== 以下是通用Web动作 全部封装在这一个引擎里 ==========
    def open_url(self, url):
        """打开网址"""
        self.driver.get(url)

    def input_text(self, locator, text):
        """输入文本"""
        self.input(locator, text)

    def click_elem(self, locator):
        """点击元素"""
        self.click(locator)

    def assert_url_contain(self, expected):
        """断言URL包含"""
        Assert.assert_contains(self.driver.current_url, expected)