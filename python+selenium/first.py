#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window()#最大化浏览器
driver.get('https://www.ywart.com')
time.sleep(3)#暂停3秒钟
driver.quit()

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.ywart.com")
# time.sleep(3)
# driver.quit()