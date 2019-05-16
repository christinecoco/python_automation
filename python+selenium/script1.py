#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()#最大化浏览器
driver.get('https://www.baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="2"]/h3/a/em[text()="Selenium"]').is_displayed()
driver.quit()




import time
from selenium import webdriver
 
driver = webdriver.Chrome() # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
driver.maximize_window()    # 最大化浏览器窗口
driver.implicitly_wait(8)   # 设置隐式时间等待
 
driver.get("https://www.baidu.com")  # 地址栏输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  #点击百度一下按钮
 
# 导入time模块，等待2秒
 
time.sleep(2) 
# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# 这里采用了相对元素定位方法/../
# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
str1=driver.find_element_by_xpath('//*[@id="2"]/h3/a/em[text()="Selenium"]').text
if (str1==u"Selenium"):
	print('测试成功，结果和预期结果相匹配')
driver.quit()