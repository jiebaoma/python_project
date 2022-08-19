#!/usr/bin/env python
#__*__ coding:utf-8 __*__
import HTMLTestReportCN
import unittest
import os
from time import strftime
testcase_path=os.path.dirname(os.path.abspath(__file__))+"\\test_case"
report_path=os.path.dirname(os.path.abspath(__file__))+"\\report"+"\\"
report_name=report_path+strftime("%Y-%m-%d-%H_%M_%S")+"report.html"
discover=unittest.defaultTestLoader.discover(testcase_path,pattern="Baidu_Search.py")
with open(report_name,"wb")as f:
    runner=HTMLTestReportCN.HTMLTestRunner(stream=f,title="测试用例标题",description="测试用例描述",tester="翟帅")
    runner.run(discover)
