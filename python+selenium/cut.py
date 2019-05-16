#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https://www.baidu.com')
time.sleep(2)

#driver.get_screenshot_as_file('/Users/ywart/Desktop/python练习/baidu.png')
driver.get_screenshot_as_png()
driver.quit()