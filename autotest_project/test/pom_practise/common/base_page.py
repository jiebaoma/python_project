from selenium import webdriver

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def get_url(self,url):
        self.driver.get(url)

    def locator(self,loc):
       return self.driver.find_element(*loc)

    def send_keys(self,loc,keyword):
        self.locator(loc).send_keys(keyword)

    def click_search(self,loc):
        self.locator(loc).click()
