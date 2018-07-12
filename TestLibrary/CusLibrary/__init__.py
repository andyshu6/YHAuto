# -*- coding: UTF-8 -*-

import os
from ImageCompare import ImageCompare
from MySelenium import MySelenium


class CusLibrary(MySelenium, ImageCompare):
    """
    用户自定义的Libraries
    """

    def __init__(self, running_param):
        super(CusLibrary, self).__init__(running_param)
        self.running_param = running_param


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
    test = CusLibrary(running_param)
    print test.running_param['DB']
    print test.running_param['BASE_URL']
    print test.running_param['screenshot_dir']
