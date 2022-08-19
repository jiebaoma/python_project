from selenium import webdriver
import unittest
from test.pom_practise.pageobject.baidu_homepage import Baidu_Homepage
from time import sleep
from ddt import ddt,file_data
import os

@ddt
class Test_baidu_Search(unittest.TestCase):
    keyword_path=os.path.join(os.path.abspath(os.path.join(os.getcwd(),'..')),"data\search_keyword.yaml")
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()

    @file_data(keyword_path)
    def test_search_keyword(self,keyword):
        bp=Baidu_Homepage(self.driver)
        bp.search_keyword(keyword)

if __name__ == '__main__':
    unittest.main()