#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import pymysql
import xlrd

class Get_and_write_exceldata(object):
    file_name="学生信息_20200311092309.xls"
    sql="insert into student_info (stu_id,name,age,score) values (%s,%s,%s,%s)"
    def get_exceldata(self):
        #打开一个excel对象
        file=xlrd.open_workbook(self.file_name)
        #通过下标获取第一个sheet页的对象
        sheet=file.sheet_by_index(0)
        #sheet=file.sheet_by_name("学生信息")
        #获取行数
        row_num=sheet.nrows
        #获取列数
        col_num=sheet.ncols
        #遍历每一行，获取每行中的列值
        for i in range(1,row_num):
            stu_id=sheet.cell_value(i,0)
            name=sheet.cell_value(i,1)
            age=sheet.cell_value(i,2)
            score=sheet.cell_value(i,3)
            all=(stu_id,name,age,score)
            self.write_to_mysql(all)
    def write_to_mysql(self,col_list):
        db=pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="test",charset="utf8")
        cursor=db.cursor()
        try:
            cursor.execute(self.sql,col_list)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
if __name__ == "__main__":
    o=Get_and_write_exceldata()
    o.get_exceldata()

