#coding=utf-8
import time
from selenium import webdriver

class ClassA(object):
    def open_baidu(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get('https://www.baidu.com')
        time.sleep(2)
        driver.quit()