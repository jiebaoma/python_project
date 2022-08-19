#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import yaml
import os
class ReadYaml:
    def read_yaml(self,file):
        with open(file,'r',encoding='utf-8') as f:
            data=yaml.load(stream=f,Loader=yaml.FullLoader)
        return data
if __name__ == '__main__':
    base_path=os.path.dirname(os.path.abspath(__file__))
    config_file=base_path+'\config\config.yaml'
    readyaml=ReadYaml()
    data=readyaml.read_yaml(config_file)
    for i in data.values():
        print(i)
        print(type(i))

