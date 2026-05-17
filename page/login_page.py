#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 13:50
from page.base_page import BasePage
from selenium.webdriver.common.by import By
#登录页元素定位与业务操作封装，分离元素定位与业务，遵循PO模式设计
class LoginPage(BasePage):
    username_loc = (By.CSS_SELECTOR,"#user-name")
    password_loc = (By.CSS_SELECTOR,"#password")
    submit_loc = (By.CSS_SELECTOR,"#login-button")

    def username_input(self, text):
        self.input(self.username_loc, text)

    def password_input(self, text):
        self.input(self.password_loc, text)

    def submit_click(self):
        self.click(self.submit_loc)

