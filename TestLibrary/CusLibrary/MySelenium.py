# -*- coding: UTF-8 -*-
"""
@Description:用户自定义的类
@Author: zhenhai.lai
"""
from selenium import webdriver
import time
import os
import sys
import subprocess
import shutil
from CusBase import CusBase


class MySelenium(CusBase):
    """
    用户自定义的类
    """

    def __init__(self, running_param):
        super(MySelenium, self).__init__(running_param)

    def dr_init(self):
        dr = webdriver.Chrome()
        time.sleep(1)
        dr.maximize_window()

    def install_rf_libs(self):
        """
        安装RF第三方库
        libs_file_path: RF第三方库的依赖文件'requirements.txt'所在路径,自动拼接
        :return:True
        """
        current_dir = os.path.dirname(__file__)
        # print current_dir
        libs_file_path = os.path.join(current_dir, '..\..', 'requirements.txt')
        cmd = "pip install -r %s" % libs_file_path
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line
        return True

    def copy_drivers_to_local(self):
        """
        将webdriver驱动拷贝到python安装目录
        :return: True
        """
        python_exe_path = sys.executable
        python_dir = python_exe_path[0:python_exe_path.rfind(os.sep)]
        current_dir = os.path.dirname(__file__)
        drivers_src_path = os.path.join(current_dir, '..\..', 'TestData\drivers')
        print drivers_src_path
        drivers = os.listdir(drivers_src_path)
        for driver in drivers:
            driver_path = os.path.join(drivers_src_path, driver)
            print driver_path
            if os.path.isfile(driver_path):  # 判断是否为文件
                print 'drivers coping, it will take several seconds, please wait……\n %s --> %s' % (driver_path, python_dir)
                shutil.copy2(driver_path, python_dir)
        print 'drivers copy done.'
        return True


if __name__ == '__main__':
    running_param = {
        'HTTP_TYPE': 'http://',
        'IP': '192.168.0.146',
        'PORT': '8081',
        'user': 'admin',
        'password': 'g5'
    }
    test = MySelenium(running_param)
    print test.running_param['HTTP_TYPE']
    print test.running_param['user']
    print test.running_param['password']
    # test.dr_init()
    # test.install_rf_libs()
    # test.copy_drivers_to_local()
