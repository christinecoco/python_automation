#coding=utf-8
from selenium import webdriver
class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去控制启动不同的浏览器，这里主要是IE，firefox,chrome

    """
    def __init__(self,driver):
        self.driver=driver
    browser_type='Chrome'
    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认地洞Chrome
        :return:driver
        """
        if self.browser_type=='firefox':
            driver=webdriver.Firedox()
        elif self.browser_type=='Chrome':
            driver=webdriver.Chrome()
        elif self.browser_type=='IE':
            driver=webdriver.IE()
        else:
            driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)

        return driver
