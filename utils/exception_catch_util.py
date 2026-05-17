#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/7 17:52
#装饰器异常捕获，区分UI/接口异常，报错自动打印堆栈日志，不阻塞用例
from functools import wraps
from utils.log_util import LogUtil
import traceback
import allure
def exception_catch(func):
    """ui异常捕获"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            LogUtil.error(f"用例执行错误:{func.__name__} -> {traceback.format_exc()}")
            raise
    return wrapper

def api_exception_catch(func):
    """api异常捕获"""
    @wraps(func)
    def wrapper(response, *args, **kwargs):
        try:
            return func(response, *args,**kwargs)
        except Exception as e:
            LogUtil.error(f"【断言失败】{func.__name__},失败:{str(e)}")
            with allure.step("断言失败详情"):
                allure.attach(
                    str(response.text),
                    "response",
                    allure.attachment_type.TEXT
                )
            with allure.step("错误信息"):
                allure.attach(
                    f"{str(e)}",
                    "异常信息",
                    allure.attachment_type.TEXT
                )
            raise AssertionError(f"断言失败:{str(e)}")

    return wrapper






