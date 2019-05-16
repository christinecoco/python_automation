#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()

#driver.implicitly_wait(8)

driver.get('https://www.ywart.com')
driver.find_element_by_xpath('//*[@id="owl-hero"]/div[1]/div/div[3]/div/a').is_displayed()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/a[2]/span').click()
time.sleep(2)
driver.find_element_by_xpath('html/body/div[2]/section[1]/div[2]/div[2]/div[1]/ul/a[1]').click()
time.sleep(2)

driver.quit()