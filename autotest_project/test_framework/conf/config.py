import os
from configparser import ConfigParser

_conf_dir = os.path.dirname(__file__)
_conf_file = os.path.join(_conf_dir,"config.ini")

#集成configparser，写一个将结果转成dict的方法
class MyParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k]=dict(d[k])
        return d

    #读取所有配置，以字典方式输出结果
def _get_all_conf():
    _config=MyParser()
    result={}
    if os.path.isfile(_conf_file):
        try:
            _config.read(_conf_file,encoding="utf-8")
            result=_config.as_dict()
        except OSError:
            raise ValueError("Read config file failed: %s" % OSError)
        return result

#将各配置文件读取出来，放在变量中，后续其他文件直接引用这个变量
config=_get_all_conf()
sys_cfg=config["sys"]
smtp_cfg=config["smtp"]

print(sys_cfg)
print(smtp_cfg)
print(smtp_cfg["host"])