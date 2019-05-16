#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://news.baidu.com')
driver.implicitly_wait(4)
#driver.find_elements_by_xpath('')
for i in driver.find_elements_by_xpath('//*/input[@type="radio"]'):
	i.click()