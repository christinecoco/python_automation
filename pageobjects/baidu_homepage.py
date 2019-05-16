#coding=utf-8
from framework.base_page import BasePage

class HomePage(BasePage):
    input_box='id=>kw'
    search_submit_btn='xpath=>//*[@id="su"]'
    news_link="xpath=html/body/div[2]/div[1]/div/div[3]/a[1]"

    def type_search(self,text):
        self.type(self.input_box,text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        #self.switch_window()
        self.sleep(2)