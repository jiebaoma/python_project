"""
LoiginPage类：专门用于实现登录页面对象的文件
主要内容包含：
    1、核心的页面元素
        账号、密码、登录按钮
    2、核心的业务流：用户的登录行为
"""

#继承
from selenium.webdriver.common.by import By
from selenium import webdriver
from base.base_page import BasePage


class LoginPage(BasePage):
    #核心元素
    url='http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    user=(By.NAME,'accounts')
    password=(By.NAME,'pwd')
    login_button=(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    #核心业务流
    def login(self,username,pwd):
        self.visit()
        self.input_keyword(self.user,username)
        self.input_keyword(self.password,pwd)
        self.click(self.login_button)

# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     username='xuzhu666'
#     password='123456'
#     print(type(username))
#     print(type(password))
#     lp=LoginPage(driver)
#     driver.implicitly_wait(50)
#     lp.login(username,password)