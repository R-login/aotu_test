#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 12:23
#快速指定测试标签、执行接口/UI专项用例，便捷调试单模块功能
import pytest
import os
import shutil
import argparse

def main():
    reports_path = os.path.join(os.getcwd(), "reports")
    if os.path.exists(reports_path):
        shutil.rmtree(reports_path)
    os.makedirs(reports_path, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--mark", default="", help="标记-m，smoke/login")
    parser.add_argument("--env", default="", help="环境切换 - > test/uat/prod")
    args = parser.parse_args()
    cmd = ["--alluredir=./reports"]
    if args.mark:
        cmd.append(f"-m {args.mark}")
    if args.env:
        cmd.append(f"--env={args.env}")

    pytest.main(cmd)
    print(f'当前运行环境：{args.env}')
    print(f"当前运行标记：{args.mark if args.mark else '所有用例'}")
    print(f"执行命令：pytest {' '.join(cmd)}")
    print(f"✅报告数据已生成 ⬇️")
    print(f"allure serve ./reports")



if __name__ == '__main__':
    main()