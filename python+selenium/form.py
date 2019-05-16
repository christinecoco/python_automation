#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get('https://www.baidu.com')
try:
	driver.find_element_by_tag_name('form')
	print('test pass:tagname found')
except Exception as e:
	print('test failed:tagname not found',format(e))
time.sleep(3)
driver.quit()