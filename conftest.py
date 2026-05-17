#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 11:44
#全局公共夹具、封装浏览器驱动、环境读取、接口登录拿token、实现用例失败自动截图和日志挂载
import configparser
from selenium import webdriver
import pytest
import allure
import os
from utils.api_request_util import ApiRequet
from utils.redis_util import RedisUtil,MockRedis



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    print("前置")
    yield driver
    print("后置")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    失败截图
    :param item: 单个用例
    :param call: 执行阶段
    :return:
    """

    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get("driver")
    if driver:
        if rep.when == "call" and rep.failed:
            with allure.step("用例失败截图"):
                allure.attach(
                    driver.get_screenshot_as_png(),
                    "失败截图",
                    allure.attachment_type.PNG
                )
            with allure.step(f"错误日志"):
                log_dir = os.path.join(os.path.dirname(__file__), "log_dir")
                log_files = sorted(os.listdir(log_dir), reverse=True)
                if log_files:
                    last_log = os.path.join(log_dir, log_files[0])
                    with open(last_log, "r", encoding="utf-8") as f:
                        log_txt = f.read()
                allure.attach(log_txt, "报错日志", allure.attachment_type.TEXT)
    print("makereport")

def pytest_addoption(parser):
    """
    增加自定义参数 --env
    :param parser:
    :return:
    """
    parser.addoption(
        "--env",
        default="uat",
        help="环境切换 - > test/uat/prod"
    )
    print(pytest_addoption)

@pytest.fixture(scope="session")
def env(request):
    """
    取出--env参数当前值
    :param request:
    :return:
    """
    env_name = request.config.getoption("--env")
    print(f"当前运行环境 -> {env_name}")
    print(env)
    return env_name

@pytest.fixture(scope="session")
def config(env):
    """
    拿到env当前值，读取congig.ini
    :param env:
    :return:
    """
    config_ini_path = os.path.join(os.getcwd(), "config/config.ini")
    cp = configparser.ConfigParser()
    cp.read(config_ini_path, encoding="utf-8")
    print(config)
    return cp[env]

@pytest.fixture(scope="session")
def api_login(config):
    login_url = config["login_url"]
    data = eval(config["data"])
    response = ApiRequet.post(login_url,json=data).json()
    token = response["token"]
    RedisUtil.set_key("token", token, expire=3600)
    print("接口登录成功，token =", token)
    yield token
    print(MockRedis.data["token"])


