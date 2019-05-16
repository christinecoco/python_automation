#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get('https://www.baidu.com')
try:
	driver.find_element_by_link_text('新闻')
	driver.find_element_by_class_name('s_ipt')
	driver.find_element_by_name('wd')
	print('test pass:link text found')
except Exception as e:
	print('test fail:link text not found',format(e))
time.sleep(2)
driver.quit()