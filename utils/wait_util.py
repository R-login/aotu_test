#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 13:51
#现实等待封装、统一元素可见、可点击，存在三种等待方式，提升脚本稳定性
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:

    @staticmethod

    def wait_presence(driver, locator):
        WebDriverWait(driver, timeout=10).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_visibility(driver, locator):
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_clickable(driver, locator):
        WebDriverWait(driver, timeout=10).until(
            EC.element_to_be_clickable(locator)
        )
