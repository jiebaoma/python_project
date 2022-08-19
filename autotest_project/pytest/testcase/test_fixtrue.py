#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import pytest
#function对应setup方法，每条用例执行前都会执行，autouse默认是False
#class对应setup_class方法，每个类的前置条件、后置条件
#module,一个py文件中有多个类，所有类的前置条件、后置条件
#package/session（包）:多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
#scope：标记的作用域
#params:元祖、列表、元祖加字典、列表加字典
#params    request.param：固定写法
#ids：用例名字
#name：给fixture函数取别名
@pytest.fixture(scope='class',autouse=True,params=['衣服','包包','鞋子'],ids=['aa','bb','cc'],name='L')
def login(request):
    print('登录系统')
    yield request.param
    print('退出系统')

class TestCase1:
    def test01(self,L):
        print('测试用例1',L)

    def test02(self):
        print('测试用例2')

class TestCase2:
    def test03(self):
        print('测试用例3')

    def test04(self):
        print('测试用例4')

if __name__ == '__main__':
    pytest.main(['-vs','test_fixtrue.py'])