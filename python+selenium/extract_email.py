#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time 
import re
driver=webdriver.Chrome()
driver.set_window_size(1900,1900)
driver.implicitly_wait(5)

driver.get('http://home.baidu.com/contact.html')

doc=driver.page_source
emails=re.findall(r'[\w]+@[\w\.-]+',doc)

for email in emails:
	print(email)
driver.quit()