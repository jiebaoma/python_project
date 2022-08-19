#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import unittest
#类名需要继承unittest.TestCase
class UnitDemo(unittest.TestCase):
    # def setUp(self):
    #     print('前置条件')
    # def tearDown(self):
    #     print('后置条件')
    @classmethod
    def setUpClass(cls):
        print('class前置条件')
    @classmethod
    def tearDownClass(cls):
        print('class后置条件')
    #测试用例以函数的形式存在，名称以test开头
    def test_01(self):
        print('测试用例1')
        self.login()
    def test_02(self):
        print('测试用例2')
    #普通函数：封装逻辑代码，以便于在测试用例中进行调用
    def login(self):
        print('登录用例')
if __name__ == '__main__':
    unittest.main()