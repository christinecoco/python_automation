#coding=utf-8
import time
import os
from test1.logger import Logger

mylog=Logger(logger='BasePage').getlog()

class BasePage(object):
    """
    主要是把常用的几个selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        :return:
        """
        self.driver=driver
    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()
    def forward(self):
        """
        浏览器前进按钮
        :return:
        """
        self.driver.forward()
    def open_url(self,url):
        """
        打开URL站点
        :param url:
        :return:
        """
    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :return:
        """
        self.driver.quit()

    def take_screenshot(self):
        """
        截图并保存在根目录下的Screenshots文件夹下
        :return:
        """
        file_path=os.path.dirname(os.getcwd())+'/Screenshots/'
        rq=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info('开始截图并保存')
        except Exception as e:
            mylog.error('出现异常',format(e))
