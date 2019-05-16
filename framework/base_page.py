#coding=utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os.path
from selenium.common.exceptions import NoSuchElementException
from test1.logger import Logger

logger=Logger(logger='BasePage').getlog()

class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self,driver):#初始方法
        self.driver=driver

    #quit browser and testing
    def quit_browser(self):
        self.driver.quit()

     #浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info('click forward on current page')

    #浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info('click back on current page')

    #隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('wait for %d seconds.'% seconds)

    #点击关闭当前窗口
    def close(self):
         try:
             self.driver.close()
             logger.info('closing and quit the browser')
         except Exception as e:
             logger.error('failed to quit the browser with %s'% e)

    #保存图片
    def get_window_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.Screenshots下
        :return:
        """
        file_path=os.path.dirname(os.path.abspath('.'))+'/Screenshots/'#获取相对路径
        rq=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take scrrenshot and save to folder:/Screenshots')
        except Exception as e:
            logger.error('failed to take screenshot!%s'% e)
            self.get_window_img()
    #定位元素方法
    def find_element(self,selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn='id=>su'
        login_link="xpath=>//*[@id='u1']/a[7]"  #百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个＝，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element=''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by=selector.split('=>')[0]
        selector_value=selector.split('=>')[1]

        if selector_by=='i' or selector_by=='id':
            try:
                element=self.driver.find_element_by_id(selector_value)
                logger.info('Had find the element \'%s \'successful '
                             'by %s via value:%s'%(element.text,selector_by,selector_value))
            except Exception as e:
                logger.error('No Such Element Exception:%s'% e)
                self.get_window_img()
        elif selector_by=='n' or selector_by=='name':
            element=self.driver.find_element_by_name(selector_value)
        elif selector_by=='c' or selector_by=='class_name':
            element=self.driver.find_element_by_class_name(selector_value)
        elif selector_by=='l' or selector_by=='link_text':
            element=self.driver.find_element_by_link_text(selector_value)
        elif selector_by=='p' or selector_by=='partial_link_text':
            element=self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by=='t' or selector_by=='tag_name':
            element=self.driver.find_element_by_tag_name(selector_value)
        elif selector_by=='x' or selector_by=='xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info('Had find the element \'%s\'successful '
                 'by %s via value:%s'%(element.text,selector_by,selector_value))
            except Exception as e:
                logger.error('NoSuchElementException:%s'% e)
                self.get_window_img()
        elif selector_by=='s' or selector_by=='selector_selector':
            element=self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError('Please enter a valid type of targeting elements.')
        return element

    #输入
    def type(self,selector,text):
        e1=self.find_element(selector)
        e1.clear()
        try:
            e1.send_keys(text)
            logger.info('Had type \'%s\'in inputBox'% text)
        except NameError as e:
            logger.error('Failed to type in input box with %s'% e)
            self.get_window_img()

    #清除文本框
    def clear(self,selector):
        e1=self.find_element(selector)
        try:
            e1.clear()
            logger.info('Clear text in input box before typing')
        except NameError as e:
            logger.error('Failed to clear in input box with %s'% e)
            self.get_window_img()

    #点击元素
    def click(self,selector):
        e1=self.find_element(selector)
        try:
            e1.click()
            time.sleep(1)
            logger.info('The element \'%s\' was clicked' %e1.text)
        except NameError as e:
            logger.error('Failed to click the element with %s'%e)

    #切换到新打开的窗口页面
    # def switch_window(self,selector,handles):
    #     e=self.driver.current_window_handle
    #     logger.info('current window is %s'% e)
    #     for handle in handles:
    #         if handle!= e:
    #             print('switch to second window',handle)
    #             self.driver.close()
    #             self.driver.switch_to.window(handle)
    #或者网页标题
    def get_page_title(self):
        logger.info('Current page title is %s'% self.driver.title)
        return self.driver.title
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info('Sleep for %d seconds'% seconds)