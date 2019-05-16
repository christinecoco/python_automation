#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://www.baidu.com')
driver.find_element_by_id("kw").send_keys("selenium")
try:
	driver.find_element_by_id("kw").clear()
	print('test pass;clean successful')
	time.sleep(2)
	driver.refresh()#刷新当前页面
	time.sleep(2)
	print('test pass:refresh successful')
except Exception as e:
	print('Exception found',format(e))
driver.quit()