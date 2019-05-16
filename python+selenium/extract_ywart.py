#coding=utf-8
from selenium import webdriver
import time
#提取网页链接
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)

driver.get('https://www.ywart.com/')
time.sleep(2)

for link in driver.find_elements_by_xpath(('//*[@src]')):
    print(link.get_attribute('src'))
driver.quit()