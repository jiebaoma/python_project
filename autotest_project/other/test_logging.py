import logging
import time

class Demologger:
    def log(self):
        logger=logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            sh=logging.StreamHandler()
            fh=logging.FileHandler(filename="./log/{}.log".format(time.strftime("%Y_%m_%d_%H_%M_%S"),time.localtime()),encoding="utf-8")
            formator=logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s ",datefmt="%Y/%m/%d %X")
            sh.setFormatter(formator)
            fh.setFormatter(formator)
            logger.addHandler(sh)
            logger.addHandler(fh)
            logger.info("info信息")
            logger.info("critical信息")

log=Demologger()
log.log()