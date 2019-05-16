#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get('https://www.baidu.com')
driver.maximize_window()
print(driver.get_window_size())
driver.implicitly_wait(4)

driver.set_window_size(1920,1000)#设置屏幕分辨率1920X1000
print(driver.get_window_size())#获取屏幕当前分辨率

driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__memberPass"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__memberPass"]').click()
time.sleep(2)
driver.quit()
