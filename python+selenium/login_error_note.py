#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https:www.baidu.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
try:
	error_message=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__error" and text()="请您输入手机/邮箱/用户名"]').is_displayed()
	print('test pass,the error message is displayed')
except Exception as e:
	print('test failed')


#第二种方法
error_mes=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__error"]').text
try:
	assert error_mes==u'请您输入手机/邮箱/用户名'
	print('test pass')
except Exception as e:
	print('test fail',format(e))


driver.quit()