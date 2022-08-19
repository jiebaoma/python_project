#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#
# import os
# import logging
# import time
#
# class Log_moudle(object):
#     def __init__(self):
#         #1.创建logger
#         self.logger=logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         #2.创建handler
#         #构建日志
#         self.base_path=os.getcwd()
#         self.log_name=os.path.join(self.base_path,"logs/"+time.strftime("%Y%m%d%H%M%S")+".log")
#         #创建写入文件的handler
#         self.fh=logging.FileHandler(self.log_name,"a")
#         #创建控制台handler
#         self.sh=logging.StreamHandler()
#         #3.设置日志输出格式
#         self.formater=logging.Formatter("%(asctime)s - %(filename)s [line:%(lineno)d] --%(levelname)s:%(message)s")
#         self.fh.setFormatter(self.formater)
#         self.sh.setFormatter(self.formater)
#         #4.将logger添加到handler
#         self.logger.addHandler(self.fh)
#         self.logger.addHandler(self.sh)


import logging.handlers
import time

class Logger(logging.Logger):
    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        # 日志文件名
        if filename is None:
            filename = './logs/'+time.strftime('%Y%m%d')+'.log'
        self.filename = filename

        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30,encoding='utf-8')
        #fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)
