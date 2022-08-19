#!/usr/bin/env python
#__*__ coding:utf-8 __*__

"""
requests.get():url是接口地址  params用来传参
request.post()：url是接口地址  data用来传参(字符串)，json用来传参（字典）
    data和json传参：主要通过Content-Type来区分
    Content-Type：作用是服务器要求传入报文的内容类型
    Content-Type:application/json
    Content-Type:application-www-form-urlencoded
    Content-Type:text/plain
request.delete()
request.put()
res.json（）：返回的字典格式数据
res.text()：返回的字符串格式数据
res.content：返回的bytes字节类型数据
res.status_code：返回状态码
res.reason：返回状态信息
res.cookies：返回cookie信息
res.headers：返回响应头
res.url：返回地址
"""
import requests
res=requests.get(url='http://39.98.138.157:5000/api/getweather',params='1')
print(res.json())

# res1=requests.post(url='http://39.98.138.157:5000/api/login',json={"password":"123456","username":"admin"})
# print(res1.text)
url='http://39.98.138.157:5000/api/login'
data={"password":"123456","username":"admin"}
res1=requests.post(url=url,json=data)
print(res1.text)

#取登录接口的token
token=res1.json()['token']
#接口关联:基于上面的登录接口拿到token用于测个人信息接口
url_userinfo='http://39.98.138.157:5000/api/getuserinfo'
headers={"token":token}
res3=requests.get(url=url_userinfo,headers=headers)
print(res3.json())

#二次封装
class HttpClient:
    def __init__(self):
        self.session=requests.session()
    #封装请求  post delete get put
    #接口地址
    #接口参数
    #参数类型  表单   json
    #请求头  数据类型设置    **kwargs
    def send_request(self,method,url,param_type,data,**kwargs):
        #请求方式、参数类型转成大写
        method=method.upper()
        param_type=param_type.upper()
        if 'GET'==method:
            response=self.session.request(method=method,url=url,params=data,**kwargs)
        elif 'POST'==method:
            #判断参数类型是json还是data
            if 'FORM'==param_type:
                response =self.session.request(method=method,url=url,data=data,**kwargs)
            else:
                response =self.session.request(method=method,url=url,json=data,**kwargs)
        elif 'DELETE'==method:
            if 'FORM' == param_type:
                response =self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'PUT'==method:
            if 'FORM' == param_type:
                response =self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                self.session.request(method=method, url=url, json=data, **kwargs)

        else:
            print("请检查请求")
        return response
    def close_session(self):
        self.session.close()