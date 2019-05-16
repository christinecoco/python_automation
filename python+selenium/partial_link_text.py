#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get('https://www.baidu.com')
try:
	driver.find_element_by_partial_link_text('把百度设为主页').click()
	print('test pass:set success')
except Exception as e:
	print('test fail',format(e))
time.sleep(2)
driver.quit()