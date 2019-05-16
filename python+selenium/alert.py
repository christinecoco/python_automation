#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.set_window_size(1900,1900)
driver.implicitly_wait(3)

driver.get('https://www.baidu.com')
time.sleep(1)

driver.execute_script('window.alert("这是一个测试alert弹窗")')
time.sleep(2)
driver.switch_to_alert().accept()#新方法是switch_to.alert.accept()
#driver.switch_to_alert().dismiss()
driver.quit()