#coding=utf-8
import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setup()的代码，主要是测试的前提准备工作
        :return:
        """
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.driver.get('https://www.baidu.com')

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :param self:
        :return:
        """
        self.driver.quit()
    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        self.driver.find_element_by_id('su').send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            assert 'selenium' in self.driver.title
            print('test pass')
        except Exception as e:
            print('test fail',format(e))

if __name__=='__main__':
    unittest.main()

