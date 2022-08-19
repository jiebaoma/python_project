
#导入封装的日志记录模块
from log_function import Logger

#创建日志记录对象
log = Logger();

#输出日志
log.info("日志模块消息!");
log.debug("日志模块调试消息!");
log.error("日志模块错误消息!");
