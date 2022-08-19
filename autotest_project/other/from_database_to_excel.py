#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import pandas as pd
import psycopg2
from test_configparser import read_cofig
import os
import time


class to_excel:
        def __init__(self):
            rc=read_cofig()
            database_config=rc.read_database()
            self.host=database_config[0]
            self.port=database_config[4]
            self.user=database_config[1]
            self.password=database_config[2]
            self.database=database_config[3]
            self.base_dir=os.path.dirname(os.path.abspath(__file__))
            self.excel_name=u"excel_dir\学生信息_{}.xlsx".format(time.strftime("%Y%m%d %H_%M_%S"),time.localtime())
            self.excel_dir=os.path.join(self.base_dir,self.excel_name)

        def write_to_excel(self,data):
            data_new=pd.DataFrame(data,columns=("学生姓名","学生工号","学生年龄","学生成绩"))
            data_new.to_excel(self.excel_dir,sheet_name="学生信息",index=False,encoding="utf-8")

        def connect_pg15(self,sql):
            connect=psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor=connect.cursor()
            cursor.execute(sql)
            datas=cursor.fetchall()
            print(datas)
            self.write_to_excel(datas)
            cursor.close()
            connect.close()





if __name__ == '__main__':
    te = to_excel()
    sql = "select * from student_info"
    te.connect_pg15(sql)


