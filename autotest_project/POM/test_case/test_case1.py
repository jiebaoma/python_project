import unittest
from selenium import webdriver
from page_object.login_page import LoginPage
from time import sleep

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.quit()

    def test_01_login(self):
        username=r'xuzhu666'
        password=r'123456'
        lp=LoginPage(self.driver)
        lp.login(username,password)

if __name__ == '__main__':
    unittest.main()