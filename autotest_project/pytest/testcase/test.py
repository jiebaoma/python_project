#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import pytest

class Testcase:
    # def setup(self):
    #     print('111')
    def setup_class(self):
        print('111')
    def teardown_class(self):
        print('222')
    @pytest.mark.run(order=2)
    def testcase_01(self):
        print('第一条用例')
    @pytest.mark.run(order=1)
    def testcase_02(self):
        print('第二条用例')

if __name__ == '__main__':
    pytest.main()