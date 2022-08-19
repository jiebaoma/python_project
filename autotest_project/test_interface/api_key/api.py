'''
接口的关键字驱动封装，是目前业内主流的接口框架的设计模式
将常用的请求方法进行函数封装，以便于后续的可复用和易于维护的性质
'''
import requests
import json
import jsonpath

class ApiDemo:
    #POST
    def do_post(self,url,data=None,headers=None,**kwargs):
        return requests.post(url=url,data=data,headers=headers,**kwargs)

    #GET
    def do_get(self,url,params=None,headers=None,**kwargs):
        return requests.get(url=url,params=params,headers=headers,**kwargs)

    #获取指定文本信息，用于解析接口的返回数据
    def get_text(self,res,key):
        if res is not None:
            try:
                #转成json格式
                txt=json.loads(res)
                #解析json，获取指定内容
                value=jsonpath.jsonpath(txt,'$..{0}'.format(key))
                #jsonpath获取成功返回list，获取失败返回FALSE
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None
