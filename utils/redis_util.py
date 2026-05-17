#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/9 17:31
#模拟Redis缓存工具，实现token本地缓存存取，免去重复登录获取令牌
from utils.log_util import LogUtil

class MockRedis:
    """本地模拟Redis，不用安装、不用联网"""
    data = {}

    @staticmethod
    def set(key, value, ex=None):
        MockRedis.data[key] = value
        return True

    @staticmethod
    def get(key):
        return MockRedis.data.get(key)


class RedisUtil:
    """模拟Redis工具类，用法和真实Redis完全一样！"""

    @staticmethod
    def set_key(key, value, expire=None):
        try:
            MockRedis.set(key, value)
            LogUtil.info(f"Redis存入成功: {key} = {value}")
            return True
        except Exception as e:
            LogUtil.error(f"Redis存入失败: {e}")
            return False

    @staticmethod
    def get_key(key):
        try:
            res = MockRedis.get(key)
            LogUtil.info(f"Redis读取成功: {key} = {res}")
            return res
        except Exception as e:
            LogUtil.error(f"Redis读取失败: {e}")
            return None