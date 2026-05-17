#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/13 12:01
#MySQL数据库连接工具，实现查询、增删改操作，支持上下文自动开关连接
import pymysql
from pymysql.cursors import DictCursor
class Mysql:

    def __enter__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            port=3306,
            charset="utf8mb4",
            cursorclass=DictCursor
        )
        self.cursor = self.conn.cursor()
        return self

    def query_sql(self,sql):
        """查询sql，返回结果"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def other_sql(self,sql):
        """执行增删改，返回修改的行数"""
        self.cursor.execute(sql)
        self.conn.commit()
        rowcount = self.cursor.rowcount
        print(f"执行SQL成功，影响行数：{rowcount}")
        return self.cursor.rowcount

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


