#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import configparser
import os

class read_cofig:
    def __init__(self):
        self.base_dir=os.path.dirname(os.path.abspath(__file__))
        self.config_dir=os.path.join(self.base_dir,"config\config.ini")
    def read_database(self):
        config=configparser.ConfigParser()
        config.read(self.config_dir,encoding="utf-8")
        host=config.get("database","host")
        user=config.get("database","user")
        password=config.get("database","password")
        database=config.get("database","database")
        port=config.get("database","port")
        return host,user,password,database,port
