#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://news.baidu.com')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a').click()
print driver.current_window_handle
handles=driver.window_handles
print handles

for handle  in handles:
	if handle !=driver.current_window_handle:
		print 'switch to second window',handle
		#driver.close()
		driver.switch_to.window(handle)