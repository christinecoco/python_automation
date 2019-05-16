# coding=utf-8
import time
import os.path
from selenium import webdriver
from test1.logger import Logger
import ConfigParser

logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver'
    #ie_driver_path = dir + '/tools/IEDriverServer'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'#获取当前项目路径
        config.read(file_path)

        browser = config.get('browserType','browserName')
        logger.info('you had select %s browser' % browser)
        url = config.get("testserver","URL")
        logger.info('The test server url is:%s' % url)

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info('Starting firefox browser.')
        elif browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('Starting Chrome browser')
        elif browser == 'IE':
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info('Starting IE browser')

        driver.get(url)
        logger.info('open url:%s' % url)
        #driver.maximize_window()
        logger.info('maximize the current window')
        driver.implicitly_wait(4)
        logger.info('set implicitly wait 4 seconds')
        return driver

    def quit_browser(self):
        logger.info('now,close and quit the browser')
        self.driver.quit()


