#coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sports_home import SportsNewsHomePage

class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse=BrowserEngine(self)
        self.driver=browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        #初始化百度首页，并点击新闻链接

        self.driver.find_element_by_xpath('html/body/div[1]/div[1]/div/div[3]/a[1]').click()
        # baiduhome=HomePage(self.driver)
        # baiduhome.click_news()

        #初始化一个百度新闻主页对象，点击体育
        newshome=NewsHomePage(self.driver)
        self.driver.find_element_by_xpath('html/body/div[2]/div[2]/div[2]/div/ul/li[7]/a').click()
        #newshome.click_sports()

        #初始化一个体育新闻主页，点击NBA
        sportsnewhome=SportsNewsHomePage(self.driver)
        self.driver.find_element_by_xpath('html/body/div[3]/div[3]/div[2]/div/div[1]/h3/a').click()
        time.sleep(6)
        # sportsnewhome.click_nba_link()
        sportsnewhome.get_window_img()

if __name__=='__main__':
    unittest.main()