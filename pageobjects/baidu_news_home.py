#coding=utf-8
from framework.base_page import BasePage

class NewsHomePage(BasePage):
    #点击体育新闻入口
    sports_link='xpath=html/body/div[2]/div[2]/div[2]/div/ul/li[7]/a'

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
