#coding=utf-8
from framework.base_page import BasePage

class SportsNewsHomePage(BasePage):
    #NBA入口
    nba_link='xpath=html/body/div[3]/div[3]/div[2]/div/div[1]/h3/a'

    def click_nba_link(self):
        self.click(self.nba_link)
        #self.switch_window()
        self.sleep(2)