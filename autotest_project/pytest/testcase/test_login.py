#!/usr/bin/env python
#__*__ coding='utf-8'
"""
写一个126邮箱登录的测试用例，通过yaml管理登录数据
yaml中 - 代表列表 ：代表字典
"""
import pytest
import time
from selenium import webdriver

class Testlogin:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.51zxw.net/login')
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 调用loadyaml获取数据
    #@pytest.mark.parametrize('udata',loadyaml('../data/login.yaml'))
    def test_login(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="loginStr"]').send_keys('jiebaoma@126.com')
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('320826chen')
        self.driver.find_element_by_xpath('//*[@id="pcLoginMode"]/div[4]/button').click()
        time.sleep(3)

if __name__ == '__main__':
    pytest.main()
