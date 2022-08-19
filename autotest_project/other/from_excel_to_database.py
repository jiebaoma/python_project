#!/usr/bin/env python
#__*__ coding:utf-8 __*__

from test_configparser import read_cofig
import psycopg2
import xlrd


class to_database:
    def __init__(self):
        rc = read_cofig()
        database_config = rc.read_database()
        self.host = database_config[0]
        self.port = database_config[4]
        self.user = database_config[1]
        self.password = database_config[2]
        self.database = database_config[3]
        self.sql = 'INSERT INTO student_info (stu_name, stu_no, stu_age, stu_score) VALUES (%s,%s,%s,%s);'
        self.file="./excel_dir/学生信息_20220731_002945.xlsx"

    def insert_to_pg(self,col_list):
        connect=psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        try:
            cursor=connect.cursor()
            cursor.execute(self.sql,col_list)
            connect.commit()
            cursor.close()
            connect.close()
        except Exception as e:
            connect.rollback()
            print(e)


    def read_excel(self):
        # #dataframe:表格型数据类型，通过索引读取数据
        # a = pd.read_excel("./excel_dir/学生信息_20220731_002945.xlsx", sheet_name="学生信息")
        # #通过索引方式读出每行的值，返回类型为列表
        # for i in a.index:
        #     print(type(a.loc[i].values))
        #     #self.insert_to_pg(a.loc[i].values)
        file=xlrd.open_workbook(self.file)
        sheet=file.sheet_by_index(0)
        rows=sheet.nrows
        for i in range(1,rows):
            stu_name=sheet.cell_value(i,0)
            stu_no=sheet.cell_value(i,1)
            stu_age=sheet.cell_value(i,2)
            stu_score=sheet.cell_value(i,3)
            col_list=(stu_name,stu_no,stu_age,stu_score)
            self.insert_to_pg(col_list)



if __name__ == '__main__':
    td=to_database()
    td.read_excel()
