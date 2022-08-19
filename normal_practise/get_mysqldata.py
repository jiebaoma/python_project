#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import MySQLdb
import xlwt
from time import strftime

class Get_mysqldata(object):
    def __init__(self):
        self.host="localhost"
        self.port=3306
        self.user="root"
        self.passwd="123456"
        self.database="test"
        self.charset="utf8"
        self.file_name="学生信息表"+strftime("%Y%m%d%H%M%S")+".xls"
        self.raw=1
    def connect_database(self,sql):
        db=MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.database,charset=self.charset)
        cursor=db.cursor()
        cursor.execute(sql)
        datas=cursor.fetchall()
        fields=[field[0] for field in cursor.description]
        cursor.close()
        db.close()
        return datas,fields
    def write_excel(self,datas,fields):
        workbook=xlwt.Workbook(encoding="utf-8")
        sheet=workbook.add_sheet("学生信息表")
        for col,field in enumerate(fields):
            sheet.write(0,col,field)
        for data in datas:
            for col,field in enumerate(data):
                sheet.write(self.raw,col,field)
            self.raw+=1
        workbook.save(self.file_name)
if __name__ == "__main__":
    getdata=Get_mysqldata()
    sql="select * from student_info"
    #获取getdata.connect_database中的return值
    (datas,fields)=getdata.connect_database(sql)
    getdata.write_excel(datas,fields)


