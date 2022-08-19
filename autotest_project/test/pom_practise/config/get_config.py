from configparser import ConfigParser

class MyParser(ConfigParser):
    def as_dict(self):
        d=dict(self._sections)
        for k in d:
            d[k]=dict(d[k])
        return d

def get_all_config():
    config=MyParser()
    result={}
    config.read("config.ini",encoding="utf-8")
    result=config.as_dict()
    return result

config=get_all_config()
print(config["base"])
print(config)
print(config["base"]["url"])