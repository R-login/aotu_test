#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 14:01
#底层selenium原生操作工具，封装查找、输入、点击等基础动作

class Action:

    @staticmethod
    def find_element(driver, locator):
        return driver.find_element(*locator)

    @staticmethod
    def find_elements(driver, locator) -> list:
        return driver.find_elements(*locator)


    @staticmethod
    def click(driver, locator):
        Action.find_element(driver, locator).click()

    @staticmethod
    def send_keys(driver, locator, text):
        ele = Action.find_element(driver, locator)
        ele.clear()
        ele.send_keys(text)