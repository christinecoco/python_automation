#coding=utf-8
import time
from selenium import webdriver
from test1.basepage import BasePage

class Baidusearch(object):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)

    basepage=BasePage(driver)

    def open_baidu(self):
        self.driver.get('https://www.baidu.com')
        time.sleep(2)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("selenium")
        time.sleep(2)
        self.basepage.back()
        time.sleep(2)
        self.basepage.forward()
        time.sleep(2)
        self.basepage.quit_browser()
        #print(self.driver.title)
        # try:
        #     assert 'selenium' in self.driver.title
        #     print('test pass')
        # except Exception as e:
        #     print('test fail')
        #     self.driver.quit()
baidu=Baidusearch()
baidu.open_baidu()
baidu.test_search()#需要自己手动点击"百度一下"搜索才能testpass