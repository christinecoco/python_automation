#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time 

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https://www.126.com')
time.sleep(2)

driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_xpath('//*[@class="j-inputtext dlemail"]').send_keys('Selenium switch test')

time.sleep(2)
driver.quit()