import unittest
from time import sleep
from selenium import webdriver
from BaiduHome import BaiduPage
#from PageObject_practise.common.logger import Logger


class MyTestCase(unittest.TestCase):
    #Logger=Logger()
    def setUp(self):
        #Logger.info("开始测试...")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
        assert self.driver.title, "百度一下，你就知道"
        sleep(2)

    def test_searchChinese(self):
        # 测试用例
        homePage = BaiduPage(self.driver)
        homePage.searchChinese()
        sleep(2)
        assert homePage.getTitle(), homePage.responseTitle
        # 断言搜索结果页标题
        assert homePage.getText(homePage.oneResult), homePage.oneResultText
        # 断言搜索结果第一行的文本

    def tearDown(self):
        #Logger.info("结束测试...")
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()