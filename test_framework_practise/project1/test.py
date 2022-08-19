#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import os,configparser

base_path=os.path.dirname(os.path.abspath("."))
project_path=os.path.join(base_path,"project1\config\config.ini")
conf=configparser.ConfigParser()
conf.read(project_path)
a=dict()
a["server_id"]=conf.get("datasource","server_ip")
a["port"]=conf.get("datasource","port")
a["user"]=conf.get("datasource","user")
a["password"]=conf.get("datasource","password")
for key,value in a.items():
    print(key+":"+value)