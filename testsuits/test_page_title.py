#coding=utf-8
import unittest
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser=BrowserEngine(cls)
        cls.driver=browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        homepage=HomePage(self.driver)
        print(homepage.get_page_title())