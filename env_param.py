# -*- coding: utf-8 -*-
"""
    和各个环境绑定的参数文件，传入../TestLibrary/CusLibrary
"""
import os


base_path = os.path.dirname(__file__)
running_case_para = {
    'HTTP_TYPE': 'http://',
    'IP': '192.168.0.146',
    'PORT': '8081',
    'base_url': 'http://127.0.0.1:8081/bi/Viewer',
    'user': 'admin',
    'password': 'g5',
    'expect_picture_dir': base_path + '/TestData/Screen/Expect',
    'result_picture_dir': base_path + '/TestData/Screen/Result',
    'diff_picture_dir': base_path + '/TestData/Screen/Diff',
    'screenshot_dir': base_path + '/TestData/Screen/Result'
}
