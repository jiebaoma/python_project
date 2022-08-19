#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import os
import configparser

dir_path=os.path.dirname(os.path.abspath(__file__))
config_file=dir_path+'\config\config.ini'

config=configparser.ConfigParser()
config.read(config_file,encoding='utf-8')
username=config.get('user_info','username')
passwrod=config.get("user_info","password")
print("username:%s,password:%s"%(username,passwrod))
print("username:{},password:{}".format(username,passwrod))