#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/12 12:25
#全局token获取工具，优先读取缓存，无缓存再调用登录接口获取token，再将新token存入Redis并返回
from utils.redis_util import RedisUtil
from utils.api_request_util import ApiRequet
from utils.configparser_util import ConfigParser

class TokenUtil:

    TOKEN_KEY = "token"

    @staticmethod
    def get_token():
        data = ConfigParser.configparser("prod", "data", "config.ini")
        url = ConfigParser.configparser("prod", "login_url", "config.ini")
        token = RedisUtil.get_key(TokenUtil.TOKEN_KEY)
        if not token:
            response = ApiRequet.post(url, json=data)
            new_token = response.json()["token"]
            RedisUtil.set_key(TokenUtil.TOKEN_KEY , new_token)
            return new_token
        return token


