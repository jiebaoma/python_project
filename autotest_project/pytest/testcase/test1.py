#!/usr/bin/env python
#__*__ coding:utf-8 __*__
"""
1、conftest.py在用例同目录下
2、conftest名字不能改
3、不需要导入，自动查找fixture
"""

import pytest

class TestCase1:
    def test5(self):
        print('测试用例5')
    def test6(self):
        print('测试用例6')
