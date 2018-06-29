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


def handle_func_doc(func):
    """
    处理函数的文档说明,将函数的参数整理到文档说明中
    :param func: 函数
    :return:整理后的参数和文档说明
    """
    func_arg = list(func.func_code.co_varnames[:func.func_code.co_argcount][::-1])
    if func_arg[-1] == 'self':
        func_arg.pop()
    arg = []
    if func.func_defaults is not None:
        func_defaults = func.func_defaults[::-1]
        for i in range(len(func_defaults)):
            if isinstance(func_defaults[i], (int, float, type(None), list, tuple)):
                temp = str(func_defaults[i])
            elif isinstance(func_defaults[i], unicode):
                temp = '"' + func_defaults[i].encode("utf-8") + '"'
            else:
                temp = '"' + func_defaults[i] + '"'
            arg.append(func_arg[i] + "=" + temp)
        arg += list(func_arg[len(func_defaults):])
    else:
        arg = func_arg
    arg = arg[::-1]
    if func.__doc__ is not None:
        func.__doc__ = "参数列表: [" + ", ".join(arg) + "]   功能：" + func.__doc__.strip()
    else:
        func.__doc__ = "参数列表: [" + ", ".join(arg) + "]"


def running_func(func, *arg, **kwargs):
    """
    运行函数，并作参数处理
    :param func:
    :param arg:
    :param kwargs:
    :return:func result
    """
    print u'******************** enter function: 【%s】 time:%s ********************'\
          % (func.__name__, strftime("%H:%M:%S", localtime()))
    print u'║==function args is ', arg
    print u'║==function kwargs is ', kwargs
    arg_list = []
    for item in arg:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        arg_list.append(item)
    arg = tuple(arg_list)
    for item in kwargs:
        if isinstance(kwargs[item], unicode):
            kwargs[item] = kwargs[item].encode('utf-8')
    return_value = func(*arg, **kwargs)
    print u'║==function return value is ', return_value
    print u'******************** exit function: 【%s】 time:%s  ********************'\
          % (func.__name__, strftime("%H:%M:%S", localtime()))
    return return_value


def add_logs_and_check_result(func):
    """
    @summary: 函数装饰器，给函数标记上时间,并判断返回值
    """
    handle_func_doc(func)

    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        # 判断是否关心返回值(引用方式为 flag=false)
        check_flag = True
        if kwargs.get('flag', 'true').lower() == 'false':
            check_flag = False
            kwargs.pop('flag')
        # 判断值为错误，如果为正确直接异常(引用方式为 ret=false)
        check_ret = True
        if kwargs.get('ret', 'true').lower() == 'false':
            check_ret = False
            kwargs.pop('ret')
        return_value = running_func(func, *arg, **kwargs)
        # 判断是否当前结果为False， ret=false 表示返回值必须是False
        if not check_ret:
            if return_value:
                raise AssertionError('Result is not correct, expect false but true!')
            else:
                return True
        # 判断是否关心返回值，check_flag = False 表示不关心
        if (not check_flag) or return_value:
            return return_value
        else:
            raise AssertionError('Result is not correct, expect true but false!')
    return wrapper


def add_logs_for_functions(func):
    """
    @summary: 函数装饰器，给函数标记上时间
    """
    handle_func_doc(func)

    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        return running_func(func, *arg, **kwargs)
    return wrapper


def pickle_running_case_para(running_case_para):
    """
    将系统变量序列化，用以后面的运行
    :param:running_case_para: 系统变量字典
    :return:None
    """
    with open('system_variables.txt', 'wb') as f:
        pickle.dump(running_case_para, f)
    with open('system_variables.txt', 'rb') as f:
        read_para = pickle.load(f)
        print read_para
        if read_para != running_case_para:
            raise AssertionError('pickle running case para failed')


def unpickle_running_case_para(key):
    """
    反序列化系统变量，并返回key值
    :param key:running_case_para中的key
    :return:value值
    """
    with open('system_variables.txt', 'rb') as f:
        read_para = pickle.load(f)
        try:
            print read_para[key]
            return read_para[key]
        except AssertionError:
            raise AssertionError('unpickle running case para failed')


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
