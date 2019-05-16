#coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#设置报告文件保存路径
report_path=os.path.dirname(os.path.abspath('.'))+'/test_report/'
#获取系统当前时间
now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile=report_path+now+"HTMLtemplate.html"
fp=file(HtmlFile,'wb')

#构建suite
suite=unittest.TestLoader().discover("testsuits")

if __name__=='__main__':
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"某某项目测试报告",description=u"用例测试情况")
    runner.run(suite)