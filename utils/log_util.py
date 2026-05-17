#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/5 19:12
#全局日志工具、控制台+本地文件双输出，自动清理过期日志，统一日志级别与格式
import logging
import os
from datetime import datetime
class LogUtil:
    log = None

    @classmethod
    def get_log(cls):
       if cls.log is not None:
           return cls.log

       cls.log = logging.getLogger("log")
       cls.log.setLevel(logging.INFO)
       cls.log.propagate = False

       fmt = logging.Formatter(
           "%(asctime)s | %(levelname)s | %(message)s",
           "%Y-%m-%d %H:%M:%S"
       )
       console = logging.StreamHandler()
       console.setFormatter(fmt)
       cls.log.addHandler(console)

       aotu_path = os.path.dirname(os.path.dirname(__file__))
       log_dir = os.path.join(aotu_path, "log_dir")
       os.makedirs(log_dir, exist_ok=True)
       files = os.listdir(log_dir)
       files.sort(key=lambda x: os.path.getmtime(os.path.join(log_dir, x)))
       if len(files) >= 10:
           try:
               for old_file in files[0:-10]:
                   old_file_path = os.path.join(log_dir, old_file)
                   os.remove(old_file_path)
           except:
               pass



       log_file = os.path.join(
           log_dir, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
       )

       file_handle = logging.FileHandler(log_file, encoding="utf-8")
       file_handle.setFormatter(fmt)
       cls.log.addHandler(file_handle)

       return cls.log

    @classmethod
    def info(cls,msg):
        cls.get_log().info(msg)

    @classmethod
    def error(cls,msg):
        cls.get_log().error(msg)


