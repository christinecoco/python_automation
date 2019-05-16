#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https://www.baidu.com')
time.sleep(2)
print(u"浏览器的版本是：",driver.capabilities['version'])#获取浏览器版本
driver.quit()