import unittest
import time
from home_page import Query_baidu
from selenium import webdriver

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_search(self):
        keyword="翟帅"
        hp=Query_baidu(self.driver)
        hp.search_keyword(keyword)
        time.sleep(3)
        #断言
        #self.assertEqual()

if __name__ == '__main__':
    unittest.main()