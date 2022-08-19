"""
封装一下公共的方法：
打开网页、元素定位、关闭浏览器等
"""
from selenium import webdriver

class Base_function:

    #test_baidu.search中会调用home_page中的方法，home_page又是继承base_function类，所以test_baidu.search中
    # hp=Query_baidu(self.driver)传递了driver对象，相当于把driver传递到了base_function中的self.driver
    def __init__(self,driver):
        self.driver=driver

    def get_url(self,url):
        self.driver.get(url)

    def locator(self,loc):
        #通过*lco进行解包，解成两个值
        return self.driver.find_element(*loc)

    def input_keyword(self,loc,txt):
        self.locator(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()

