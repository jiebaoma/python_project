#专门取yaml文件数据

import yaml

def loadyaml(file):
    stream=open(file,'r')
    data=yaml.load(stream,yaml.FullLoader)
    return data