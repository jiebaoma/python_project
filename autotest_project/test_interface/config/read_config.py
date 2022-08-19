#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import configparser

def read_conf(path,selector,option):
    conf=configparser.ConfigParser()
    conf.read(path)
    return conf.get(selector,option)
