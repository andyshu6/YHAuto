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
