import logging

import time


class DemoLog:
    def log(self):
        #创建一个日志器
        logger=logging.getLogger("logger")
        #设置日志输出最低等级，低于当前等级会忽略
        logger.setLevel(logging.DEBUG)
        #判断是否存在处理器，如果不加判断的话会重复输出日志结果
        if not logger.handlers:
            #创建处理器：控制台输出
            sh=logging.StreamHandler()
            #文件处理器
            fh=logging.FileHandler(filename="log/{}.log".format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())),encoding="utf-8")
            formator=logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",datefmt="%Y/%m/%d %X")
            sh.setFormatter(formator)
            fh.setFormatter(formator)
            logger.addHandler(fh)
            logger.addHandler(sh)
            return logger

        # logger.debug("debug信息")
        # logger.error("error信息")
        # logger.info("info信息")
        # logger.warning("warning信息")
        # logger.critical("critical信息")

    def sum(self,a,b):
        try:
            sum=a+b
        #记录日志
            self.log().info("正确地计算出{}+{}之和".format(a,b))
            return sum
        except Exception as error:
            self.log().error("{}+{}之和计算错误:{}".format(a,b,error))

    def test(self):
        sum1=self.sum(3,4)
        sum2=self.sum("a",1)
        print(sum1,sum2)

a=DemoLog()
a.test()