from selenium.webdriver.common.by import By
from base_function import Base_function

#pageobject需要调用基础类中的方法，所以需要集成基础类
class Query_baidu(Base_function):
    #封装页面的元素
    url="http://www.baidu.com"
    keyword=(By.ID,"kw")
    search_button=(By.ID,"su")

    #封装页面动作
    def search_keyword(self,keyword):
        self.get_url(self.url)
        self.input_keyword(self.keyword,keyword)
        self.click(self.search_button)
