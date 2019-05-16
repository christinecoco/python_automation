#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get('https://www.baidu.com')
time.sleep(2)
ele=driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')#火狐浏览器可用
driver.execute_script('window.open("https://www.ywart.com")')
time.sleep(1)
driver.quit()