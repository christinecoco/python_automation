#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://news.baidu.com')
time.sleep(1)

news_link=driver.find_element_by_xpath('html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[1]/strong/a')
page1_title_string=news_link.text
news_link.click()
time.sleep(2)

handles=driver.window_handles

for handle in handles:
	if handle!=driver.current_window_handle:
		print('switch to sceond window',handle)
		driver.close()
		driver.switch_to.window(handle)
page2_title_string=driver.find_element_by_xpath('html/body/div[3]/div/div[2]/div/p[1]/strong/font')

try:
	assert page1_title_string in page2_title_string
	print('test pass')
except Exception as e:
	print('test fail')