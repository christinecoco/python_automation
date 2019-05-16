#coding=utf-8
import time
import unittest
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse=BrowserEngine(cls)
        cls.driver=browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        """
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print('test pass')
        except Exception as e:
            print('test fail',format(e))

    def test_search1(self):
        homepage=HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_window_img()

if __name__=='__main__':
    unittest.main()