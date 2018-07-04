# -*- coding: UTF-8 -*-
"""
@Description:CusBase基类
@Author: zhenhai.lai
"""
import functools
from time import strftime, localtime
import pickle


class CusBase(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """
    用户自定义的基类
    """

    def __init__(self, running_param):
        super(CusBase, self).__init__()
        self.running_param = running_param
        # # 获取URL
        # self.base_url = self.running_param[
        #     'HTTP_TYPE'] + self.running_param['IP'] + ':' + self.running_param['PORT'] + '/bi/Viewer'
        # # 获取登陆用户名和密码
        # self.user = self.running_param['user']
        # self.password = self.running_param['password']


if __name__ == '__main__':
    running_param = {
        'HTTP_TYPE': 'http://',
        'IP': '192.168.0.146',
        'PORT': '8080',
        'user': 'admin',
        'password': 'g5'
    }
    test = CusBase(running_param)
    print test.running_param['HTTP_TYPE']
    print test.running_param['user']
    print test.running_param['password']
