import logging
from logging import handlers
import time
import os


class Demo_logger:
    def __init__(self):
        #self.log_path=os.path.join(os.path.abspath(os.path.join(os.getcwd(),"..")),"log\log_{}.log".format(time.strftime("%Y%m%d_%H%M%S")))
        self.log_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")),"log\log.log")
    def basic_logger(self):
        logger=logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        formator=logging.Formatter(fmt="[%(asctime)s]-[%(filename)s]-[%(levelname)s]:[%(message)s]-",datefmt="%Y%m%d %X")
        fh=handlers.TimedRotatingFileHandler(filename=self.log_path,when="D",backupCount=7)
        #fh=logging.FileHandler(filename=self.log_path,encoding="utf-8")
        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        fh.setLevel(logging.DEBUG)
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(sh)
        logger.addHandler(fh)
        sh.close()
        fh.close()
        return logger

if __name__ == '__main__':
    a=Demo_logger()
    logger=a.basic_logger()
    logger.critical("haha")