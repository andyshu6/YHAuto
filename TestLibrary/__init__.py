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
    running_param = {
        'HTTP_TYPE': 'http://',
        'IP': '192.168.0.146',
        'PORT': '8083',
        'user': 'admin',
        'password': 'g5'
    }

    test = TestLibrary(running_param)
    print test.running_param['PORT']
    print test.base_url
    test.dr_init()
