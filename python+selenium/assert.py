#!/uesr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)
# try:
# 	assert u"百度一下" in driver.title
# 	print('assertion test pass')
# except Exception as e:
# 	print('test failed',foemat(e))#第一种方法

if u"百度一下，你就知道"==driver.title:
	print('test pass')
else:
	print('test failed')
driver.quit()