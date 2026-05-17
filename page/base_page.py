#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 13:50
#页面基类，调度工具类，封装元素等待、点击、输入、等通用方法，统一异常捕获，所有页面统一继承
from utils.action_util import Action
from utils.wait_util import Wait
from utils.exception_catch_util import exception_catch
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @exception_catch
    def click(self, locator):
        Wait.wait_clickable(self.driver, locator)
        Action.click(self.driver, locator)

    @exception_catch
    def input(self, locator, text):
        Wait.wait_visibility(self.driver, locator)
        Action.send_keys(self.driver, locator, text)

    @exception_catch
    def find_element_presence(self, locator):
        Wait.wait_presence(self.driver, locator)
        return Action.find_element(self.driver, locator)

    @exception_catch
    def find_element_visibility(self, locator):
        Wait.wait_visibility(self.driver, locator)
        return Action.find_element(self.driver, locator)