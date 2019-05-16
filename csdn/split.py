#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GetSubString(object):
    def get_search_result(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)

        driver.get('https://www.baidu.com')
        driver.find_element_by_xpath('html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input').send_keys('selenium')
        time.sleep(1)
        driver.find_element_by_id('su').send_keys(Keys.ENTER)
        time.sleep(2)
        search_result_string=driver.find_element_by_xpath('html/body/div[1]/div[5]/div[1]/div[2]/div/div[2]/span').text
        print(search_result_string)

        new_string=search_result_string.split(u'约')[1]
        print(new_string)
        last_result=new_string.split(u'个')[0]
        print(last_result)

getstring=GetSubString()
getstring.get_search_result()
