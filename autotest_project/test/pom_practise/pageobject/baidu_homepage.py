from selenium.webdriver.common.by import By
from test.pom_practise.common.base_page import BasePage

class Baidu_Homepage(BasePage):
    input_loc=(By.ID,"kw")
    url="https://www.baidu.com"
    search_button=(By.ID,"su")

    def search_keyword(self,keyword):
        self.get_url(self.url)
        self.send_keys(self.input_loc,keyword)
        self.click_search(self.search_button)
