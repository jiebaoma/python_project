#!/usr/bin/env python
#__*__ coding:utf-8 __*__

"""
生成测试报告：allure，好看但是需要配置环境
1、安装allure-pytest  pip install allure-pytest  生成测试数据
2、下载allure压缩包，解压在某个目录
3、配置环境，放到path目录下
"""
import pytest
import os

#alluredir生成测试数据，数据文件夹自动创建
#生成测试报告
#allure generate执行测试数据  -o生成测试报告，文件夹reports
if __name__ == '__main__':
    pytest.main(['./testcase/test_login.py','--alluredir','./allure-result'])
    os.system('allure generate ./allure-result -o ./reports --clean')