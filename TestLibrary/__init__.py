# -*- coding: utf-8 -*-
"""
@Description:CustomLibrary methods
@Author: zhenhai.lai
"""
import os
import sys
from TestLibrary.CusLibrary.CusBase import *
from CusLibrary import CusLibrary


class TestLibrary(CusLibrary):
    """
    TestLibrary class, include all the methods
    """

    def __init__(self, running_param):
        # 获取配置文件中的running_case_para参数字典
        current_dir = os.path.dirname(__file__)
        sys.path.append(current_dir[:current_dir.find('TestLibrary')])
        # print sys.path
        env_module = __import__('env_param')
        self.running_param = getattr(env_module, 'running_case_para')
        super(TestLibrary, self).__init__(running_param)


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)
    running_param = {
        'DB': ['DBPainter', 'Chart'],
        'BI_HOME': 'D:\Yonghong_Z-Suite_8.0.1\Yonghong\\bihome',
        'BASE_URL': 'http://127.0.0.1:8081/bi/Viewer',
        'BROWSER': 'Chrome',
        'DELAY': 1,
        'screenshot_dir': base_path + '/TestData/Screen/Result',
        'expect_picture_dir': base_path + '/TestData/Screen/Expect',
        'result_picture_dir': base_path + '/TestData/Screen/Result',
        'diff_picture_dir': base_path + '/TestData/Screen/Diff'
    }

    test = TestLibrary(running_param)
    # print test.running_param['DB']
    # print test.running_param['BASE_URL']
    # print test.running_param['screenshot_dir']
    print test.copy_db_to_bi_home('DBPainter')
    # print test.revert_bi_home()
    # print test._check_server_status()
    # print test.start_server()
    # print test.stop_server()
    # print test.kill_driver()
