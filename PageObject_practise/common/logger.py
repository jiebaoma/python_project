#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import logging
from logging import handlers
import os
from time import strftime

class Logger(logging.Logger):
    log_path=os.path.dirname(os.path.abspath("."))
    log_name=log_path+"\\log_"+strftime("%Y-%m%-%d-%H_%M_%S")+".log"
    def __init__(self):
        super(Logger, self).__init__(self)
        fh=handlers.TimedRotatingFileHandler(self.log_name,"D",1,10)
        fh.setLevel(logging.DEBUG)
        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        formatter=logging.Formatter("[%(asctime)s]-[%(filename)s]-[line:%(lineno)d] --[%(levelname)s]:%(message)s")
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.addHandler(sh)
        self.addHandler(fh)
        sh.close()
        fh.close()

