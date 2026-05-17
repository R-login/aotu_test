#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/12 14:54
#正则表达式通用工具、封装提取、匹配、替换、分割常用方法
import re
import traceback
from utils.log_util import LogUtil
class ReUtil:

    @staticmethod
    def search_one(pattern, string, flags=0):
        """匹配第一个符合规则的 Match 对象"""
        try:
            return re.search(pattern, string, flags=flags)
        except Exception as e:
            LogUtil.error(f"正则提取异常，表达式 -> {pattern}")
            LogUtil.error(f"错误信息 -> {traceback.format_exc()}")
            return None

    @staticmethod
    def search_group(pattern, string, flags=0):
        """取出单个正则对象字符串"""
        try:
            match = ReUtil.search_one(pattern, string, flags=flags)
            return match.group() if match else None
        except Exception as e:
            LogUtil.error(f"正则提取异常，表达式 -> {pattern}")
            LogUtil.error(f"错误信息 -> {traceback.format_exc()}")
            return None

    @staticmethod
    def find_all(pattern, string, flags=0):
        """匹配所有符合规则的内容，返回列表"""
        try:
            return re.findall(pattern, string, flags=flags)
        except Exception as e:
            LogUtil.error(f"正则提取异常，表达式 -> {pattern}")
            LogUtil.error(f"错误信息 -> {traceback.format_exc()}")
            return [string]

    @staticmethod
    def sub(pattern, repl, string, count=0, flags=0):
        """替换"""
        try:
            return re.sub(pattern, repl, string, count=count, flags=flags)
        except Exception as e:
            LogUtil.error(f"正则提取异常，表达式 -> {pattern}")
            LogUtil.error(f"错误信息 -> {traceback.format_exc()}")
            return None

    @staticmethod
    def split(pattern, string, maxsplit=0, flags=0):
        try:
            return re.split(pattern, string, maxsplit=maxsplit, flags=flags)
        except Exception as e:
            LogUtil.error(f"正则提取异常，表达式 -> {pattern}")
            LogUtil.error(f"错误信息 -> {traceback.format_exc()}")
            return [string]


