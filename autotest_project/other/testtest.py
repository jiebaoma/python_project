import logging
import time
import os

class TestLog:
    def test_log(self):
        log_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"log\log_{}.log".format(time.strftime("%Y%m%d_%H%M%S"),time.localtime()))
        logger=logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            sh=logging.StreamHandler()
            fh=logging.FileHandler(filename=log_dir,encoding="utf-8")
            formator=logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s %(lineno)s",datefmt="%Y%m%d %X")
            sh.setFormatter(formator)
            fh.setFormatter(formator)
            logger.addHandler(sh)
            logger.addHandler(fh)
            logger.info("info信息")
            return logger

if __name__ == '__main__':
    testlog=TestLog()
    logger=testlog.test_log()
    logger.warning("信息")
