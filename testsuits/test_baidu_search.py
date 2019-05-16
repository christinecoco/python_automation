#coding=utf-8
import time
import unittest
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse=BrowserEngine(self)
        self.driver=browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        """

        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        homepage=HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print('Test Pass')
        except Exception as e:
            print('Test Fail',format(e))

    def test_search1(self):
        homepage=HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

if __name__=='__main__':
    unittest.main()