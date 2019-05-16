#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://www.baidu.com')
time.sleep(2)

for link in driver.find_elements_by_xpath('//*[@href]'):
	print(link.get_attribute('href'))
driver.quit()