#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https://news.baidu.com')
time.sleep(1)
try:
	driver.find_element_by_xpath('//*[@id="news"]').is_selected()#验证按钮是否被选中
	print('test pass')
except Exception as e:
	print('test fail',format(e))
driver.get('https://www.baidu.com')
search_btn=driver.find_element_by_id('su')#获取“百度一下”按钮大小
print(search_btn.size)
driver.back()
time.sleep(2)
element=driver.find_element_by_link_text('热血沸腾！看习近平强军关键词').send_keys(Keys.CONTROL+'a')#组合键全选文字
driver.forward()
time.sleep(2)
ele=driver.find_element_by_id('kw')
ele.send_keys('Selenium automation')
time.sleep(1)
ele.send_keys(Keys.CONTROL+'a')#适用于火狐浏览器
ele.send_keys(Keys.BACKSPACE)#退格键删除文字
time.sleep(2)
driver.quit()