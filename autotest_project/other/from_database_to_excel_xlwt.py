import xlwt
from test_configparser import read_cofig
import os
import time
import psycopg2

class to_excel:
    def __init__(self):
        rc=read_cofig()
        config_params=rc.read_database()
        self.host=config_params[0]
        self.user=config_params[1]
        self.passwrod=config_params[2]
        self.database=config_params[3]
        self.port=config_params[4]
        self.excel_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"excel_dir\excel_{}.xlsx".format(time.strftime("%Y%m%d_%H%M%S"),time.localtime()))
        self.sql="select * from student_info;"

    def connect_pg(self):
        connect=psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.passwrod,
            database=self.database,
            port=self.port
        )
        cursor=connect.cursor()
        cursor.execute(self.sql)
        #获取字段名
        fields=[field[0] for field in cursor.description]
        datas=cursor.fetchall()
        cursor.close()
        connect.close()
        return fields,datas

    def write_to_excel(self,fields,datas):
        wb=xlwt.Workbook()
        sheet=wb.add_sheet("学生信息")
        for col,value in enumerate(fields):
            sheet.write(0,col,value)
        raw = 1
        for data in datas:
            for col,value in enumerate(data):
                sheet.write(raw,col,value)
            raw+=1
        wb.save(self.excel_dir)


if __name__ == '__main__':
        te=to_excel()
        (fields,datas)=te.connect_pg()
        te.write_to_excel(fields,datas)
