#!/usr/bin/env python
#__*__ coding:utf-8 __*__

from api_key.api import ApiDemo
import unittest
from ddt import ddt,file_data
from config import read_config


@ddt
class CaseDemo(unittest.TestCase):
    #赋值行为的封装
    """
            url=self.url+'/api/addcart'
        headers={
            'token':self.token
        }
        data={
            'openid':self.openid,
            'userid':self.userid,
            'productid':8888
            'cartid':self.cartid
        }
        dict1:value
        dict2:
        dict3:
            dict3.1:value3.1
            dict3.2:value3.2
            dict3.3:
    """
    def assignment(self,kwargs):
        for key,value in kwargs.items():
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    #getattr() 函数用于返回一个对象属性值
                    kwargs[key]=getattr(self,key)
        return kwargs


    @classmethod
    def setUpClass(cls):
        cls.ad=ApiDemo()
        cls.token=None
        cls.openid=None
        cls.userid=None
        cls.cartid=None
        cls.url=read_config.read_conf('../config/conf_interface.ini','DEFAULTS','url')
    @file_data('../data/user.yaml')
    #将ymal中获取到的data值传入
    def test_01_login(self,data,txt):
        #请求准备的数据
        url=self.url+'/api/login'
        #模拟请求的下发，并接收响应
        res=self.ad.do_post(url=url,json=data)
        #全局变量赋值，需要加上类名
        #CaseDemo.token=self.ad.get_text(res.text,'token')
        token=self.ad.get_text(res.text,'token')
        print(token)
        if token:
            CaseDemo.token=token
        #解析响应结果，判断本次接口的请求是否成功
        #断言校验本次测试是否成功：将实际结果与预期与结果进行对比，校验本次的测试是否正确
        self.assertEqual(txt,res.json()['msg'],'断言失败')
    #获取个人信息接口
    def test_02_getinfo(self):
        url=self.url+'/api/getuserinfo'
        headers={
            'token':self.token
        }
        #调用只需要使用self即可，如果需要赋值等需要使用类名
        res=self.ad.do_get(url=url,headers=headers)
        CaseDemo.userid=self.ad.get_text(res.text,'userid')
        CaseDemo.openid=self.ad.get_text(res.text,'openid')

    #添加购物车
    def test_03_addcart(self):
        url=self.url+'/api/addcart'
        headers={
            'token':self.token
        }
        data={
            'openid':self.openid,
            'userid':self.userid,
            'productid':8888
        }
        res=self.ad.do_post(url=url,headers=headers,json=data)
        CaseDemo.cartid=self.ad.get_text(res.text,'cartid')

    #下订单
    @file_data('../data/order.yaml')
    def test_04_order(self,**kwargs):
        # url=self.url+kwargs['path']
        # headers=kwargs['headers']
        # headers['token']=self.token
        # data=kwargs['data']
        # data['openid']=self.openid
        # data['userid']=self.userid
        # data['cartid']=self.cartid
        #数据准备
        value=self.assignment(kwargs)
        res=self.ad.do_post(url=self.url+value['path'],headers=value['headers'],json=value['data'])
        print(res.text)
        #响应结果处理
        result=self.ad.get_text(res.text,'result')
        self.assertEqual(value['result'],result,'断言失败')
if __name__ == '__main__':
    unittest.main()


