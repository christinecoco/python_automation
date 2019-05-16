#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

element=driver.find_element_by_xpath('//*[@id="lg"]/map/area')
actionChains=ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

# driver.execute_script('window.alert("这是一个alert弹框。");')#执行js脚本触发一个alert弹出框
# time.sleep(2)

driver.get('https://tieba.baidu.com/index.html')
time.sleep(1)

target_elem=driver.find_element_by_xpath('//*[@id="f-d-w"]/div[12]/div/div[1]/a')#执行js脚本控制浏览器竖向滚动到左侧“地区”
driver.execute_script("return arguments[0].scrollIntoView();",target_elem)#用目标元素参考去滚动
#driver.execute_script("scroll(0,2400)")#第二种方法
#driver.quit()