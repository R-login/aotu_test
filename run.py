#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/11 15:48
#项目统一启动入口，清理历史报告，支持指定环境、指定标签批量执行用例
import pytest
import os
import shutil



reports_path = os.path.join(os.getcwd(), "reports")
if os.path.exists(reports_path):
    shutil.rmtree(reports_path)
os.makedirs(reports_path, exist_ok=True)







if __name__ == '__main__':
    pytest.main([
        "-vs",
        "-m=user_api",
        "--alluredir=./reports"
    ])

print(f"✅ 打开报告 -> allure serve ./reports")