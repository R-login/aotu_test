#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/9 16:11
#统一封装get、post请求方法、简化接口调用、配套日志打印信息
import requests
from utils.log_util import LogUtil
import json

class ApiRequet:

    @staticmethod
    def get(url, headers=None, params=None):
        full_url = url
        LogUtil.info(f"【get请求】 -> {full_url}")
        response = requests.get(url, headers=headers, params=params)
        return response


    @staticmethod
    def post(url, headers=None, json=None):
        full_url = url
        LogUtil.info(f"【POST请求】 -> {full_url}")
        response = requests.post(full_url, headers=headers, json=json)
        return response




