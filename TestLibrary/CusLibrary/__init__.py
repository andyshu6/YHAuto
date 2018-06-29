# -*- coding: UTF-8 -*-

from ImageCompare import ImageCompare
from MySelenium import MySelenium


class CusLibrary(MySelenium, ImageCompare):
    """
    用户自定义的Libraries
    """

    def __init__(self, running_param):
        super(CusLibrary, self).__init__(running_param)


if __name__ == '__main__':
    running_param = {
        'HTTP_TYPE': 'http://',
        'IP': '192.168.0.146',
        'PORT': '8082',
        'user': 'admin',
        'password': 'g5'
    }
    test = CusLibrary(running_param)
    print test.running_param['HTTP_TYPE']
    print test.running_param['user']
    print test.running_param['password']
    test.dr_init()
