#coding=utf-8

import unittest
# import testsuits
# from testsuits.test_baidu_search1 import BaiduSearch
# from testsuits.test_page_title import GetPageTitle

suite=unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))#addtest方法添加单个测试用例执行
# suite.addTest(BaiduSearch('test_search1'))
# suite.addTest(GetPageTitle('test_get_title'))

# suite=unittest.TestSuite(unittest.makeSuite(BaiduSearch))#makesuite方法可以添加整个类方法下的所有测试用例执行
# suite=unittest.TestSuite(unittest.makeSuite(GetPageTitle))

suite=unittest.TestLoader().discover("testsuits")#discover方法可以执行一个路径下的所有测试用例，使用此方法不需要倒入包文件的类

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)