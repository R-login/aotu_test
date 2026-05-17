#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/13 16:39
#业务专属数据库查询方法，根据指定字段查询业务表数据，用于接口结果库表校验
from utils.mysql_util import Mysql

class CustomerDb:


    @staticmethod
    def query_execute(case_data_key,case_data_value):
        """查询 woniusales.customer 这张表"""
        if isinstance(case_data_value, str):
            case_data_value = f"'{case_data_value}'"
        sql = f"""
        select *
        from woniusales.customer
        where {case_data_key} = {case_data_value}
        """
        with Mysql() as db:
            fetchall = db.query_sql(sql)
        return fetchall


