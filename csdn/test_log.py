#coding=utf-8
import time
from selenium import webdriver
from test1.logger import Logger

mylogger=Logger(logger='TestMyLog').getlog()
class TestMyLog(object):

    def print_log(self):
        driver=webdriver.Chrome()
        mylogger.info('打开浏览器')
        driver.maximize_window()
        mylogger.info('最大化浏览器窗口')
        driver.implicitly_wait(4)

        driver.get('https://www.baidu.com')
        mylogger.info('打开百度首页')
        time.sleep(2)
        mylogger.info('暂停2秒')
        driver.quit()
        mylogger.info('关闭并退出浏览器')

testlog=TestMyLog()
testlog.print_log()