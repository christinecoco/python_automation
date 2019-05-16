#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://www.ywart.com')
#time.sleep(2)
elem_news=driver.find_element_by_link_text('登录 / 注册')
elem_news.click()
#driver.find_element_by_xpath('//*[@id="owl-hero"]/div[1]/div/div[3]/div/a').click()
print(driver.current_url)
print(driver.title)
#time.sleep(2)
driver.back()
#time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()