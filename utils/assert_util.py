#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 15:32
#封装UI与接口全套断言方法、集成allure步骤与附件，统一断言失败格式
import allure
from utils.exception_catch_util import api_exception_catch
class Assert:

    @staticmethod
    def assert_equal(actual, expected):
        """相等断言"""
        with allure.step("相等断言"):
            allure.attach(str(actual), "实际结果")
            allure.attach(str(expected), "预期结果")
            assert actual == expected, f"断言失败,实际结果 -> {actual}与预期结果 -> {expected}不一致"

    @staticmethod
    def assert_not_equal(actual, expected):
        """不想等断言"""
        with allure.step("不相等断言"):
            allure.attach(str(actual), "实际结果")
            allure.attach(str(expected), "预期结果")
            assert actual != expected, f"断言失败,实际结果 -> {actual}与预期结果 -> {expected}一致"

    @staticmethod
    def assert_contains(actual, expected):
        """包含断言"""
        with allure.step("包含断言"):
            allure.attach(str(actual), "实际结果")
            allure.attach(str(expected), "预期结果")
            assert expected in actual, f"断言失败,{expected}不在{actual}中"

    @staticmethod
    def assert_not_contains(actual, expected):
        """不包含断言"""
        with allure.step("不包含断言"):
            allure.attach(str(actual), "实际结果")
            allure.attach(str(expected), "预期结果")
            assert expected not in  actual, f"断言失败,{expected}在{actual}中"

    @staticmethod
    @api_exception_catch
    def api_equal_code(response, expected):
        """断言状态码"""
        with allure.step("断言状态码"):
            actual = response.status_code
            str_json = response.json()
            allure.attach(str(str_json), "response")
            allure.attach(str(actual), "实际结果")
            allure.attach(str(expected), "预期结果")
            assert actual == expected , f"断言失败，实际状态码{actual}不等于预期状态码{expected}"

    @staticmethod
    @api_exception_catch
    def api_contains_key(response, key):
        """断言返回结果包含某个key"""
        with allure.step(f"断言response包含{key}"):
            dict_json = response.json()
            allure.attach(str(dict_json), "response")
            allure.attach(str(dict_json), "实际结果")
            allure.attach(str(key), "预期结果")
            assert key in dict_json, f"断言失败，key:{key}不在response{dict_json}中"







