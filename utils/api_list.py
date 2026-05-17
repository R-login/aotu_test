#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/11 15:14
#统一管理接口地址、请求头、请求类型、集中维护方便后期修改迭代
class ApiList:


    @staticmethod
    def user_list():
        """用户列表接口"""
        url = "https://jsonplaceholder.typicode.com/users"
        headers = None
        return url

    @staticmethod
    def post_list():
        """用户列表接口"""
        url = "https://jsonplaceholder.typicode.com/posts"
        headers = None
        return url

