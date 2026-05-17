#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2026/5/13 16:15
#模拟后端数据落地，接口请求成功后自动把测试数据写入数据库，避免重复插入。
from utils.mysql_util import Mysql

class BackendSimulator:

    @staticmethod
    def save_customer_to_db(case_data:dict):
        phone = case_data["customerphone"]
        exists_sql = f"SELECT 1 FROM woniusales.customer WHERE customerphone = {phone}"
        with Mysql() as db:
            result = db.query_sql(exists_sql)
            if result:
                print(f"手机号 {phone} 已存在，跳过插入")
                return

        case_key = []
        case_value = []
        parameters = [
            "customerphone",
            "creditkids",
            "creditcloth",
            "credittotal",
            "userid",
            "customername",
            "childsex",
            "childdate"
        ]
        for k,v in case_data.items():
            if k in parameters:
                case_key.append(k)
                if isinstance(v, str):
                    case_value.append(f"'{v}'")
                else:
                    case_value.append(str(v))
        with Mysql() as db:
            sql = f"""
            insert into woniusales.customer
            ({",".join(case_key)})
            values ({",".join(case_value)})
             """
            db.other_sql(sql)



