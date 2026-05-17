#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/14 17:25
#对接钉钉机器人，自动化测试执行完成后推送测试结果消息，适配Jenkins持续集成
import requests
import json

# 替换成你自己的webhook
ding_url = "https://oapi.dingtalk.com/robot/send?access_token=2bbdfd7c38f5ca2b847849584c5f675c769421ef932603020cb65b2be2944f6c"

def send_notice(status):
    content = f"""
【Jenkins自动化测试结果】
执行状态：{status}
执行时间：自动获取
项目路径：本地pytest项目
查看构建日志：自行打开Jenkins
    """
    body = {
        "msgtype": "text",
        "text": {"content": content}
    }
    response = requests.post(ding_url, json=body)
    print("响应状态码：", response.status_code)
    print("响应内容：", response.text)

if __name__ == "__main__":
    # 测试先传成功
    send_notice("✅ 测试用例全部执行完成")