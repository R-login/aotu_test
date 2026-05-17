#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/1 16:53
#ini文件读取配置封装，统一读取环境配置信息
import configparser
import os
class ConfigParser:

    @staticmethod
    def configparser(section, key, path):
        ini_path = os.path.join(os.path.dirname(os.getcwd()), path)
        cp = configparser.ConfigParser()
        cp.read(ini_path, encoding="utf-8")
        return cp.get(section, key)
