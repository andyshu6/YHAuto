# -*- coding: UTF-8 -*-
"""
@Description:用户自定义的类
@Author: zhenhai.lai
"""
import time
import os
import sys
import subprocess
import shutil
import requests
from CusBase import CusBase
from selenium import webdriver


class MySelenium(CusBase):
    """
    用户自定义的类
    """

    def __init__(self, running_param):
        super(MySelenium, self).__init__(running_param)
        self.bi_home = self.running_param['BI_HOME']
        self.new_bi_home_path = os.path.join(self.bi_home, '../')
        self.base_url = self.running_param['BASE_URL']
        self.new_bi_home_folder_name = 'bihome_' + time.strftime("%Y_%m_%d", time.localtime())

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
        libs_file_path = os.path.join(current_dir, '../..', 'requirements.txt')
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
        drivers_src_path = os.path.join(current_dir, '../..', 'TestData\drivers')
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

    def _back_up_bi_home(self):
        """
        备份产品安装的bihome目录
        :return: True/False
        """
        if os.path.exists(self.bi_home):
            # new_bi_home_folder_name = 'bihome_' + time.strftime("%Y_%m_%d", time.localtime())
            new_bi_home_folder_path = os.path.join(self.new_bi_home_path, self.new_bi_home_folder_name)
            if os.path.exists(new_bi_home_folder_path):
                shutil.rmtree(new_bi_home_folder_path)
            shutil.copytree(self.bi_home, new_bi_home_folder_path)
            return True
        else:
            raise Exception('%s is not exist, please check!' % self.bi_home)

    def revert_bi_home(self):
        """
        恢复bihome为初始状态
        :return: True/False
        """
        if os.path.exists(self.bi_home):
            # new_bi_home_folder_name = 'bihome_' + time.strftime("%Y_%m_%d", time.localtime())
            new_bi_home_folder_path = os.path.join(self.new_bi_home_path, self.new_bi_home_folder_name)
            shutil.rmtree(self.bi_home)
            shutil.copytree(new_bi_home_folder_path, self.bi_home)
            return True
        else:
            os.mkdir(self.bi_home, 0777)
            raise Exception('%s is not exist, now make it, please try again!' % self.bi_home)

    def copy_db_to_bi_home(self, db_name):
        """
        数据初始化准备，先备份bihome目录,然后将TestData下对应的DB目录拷贝到产品安装的bihome目录
        :param db_name: 自动化DB数据的文件夹名称
        :return: True/False
        """
        current_dir = os.path.dirname(__file__)
        db_dir = current_dir + '/../../TestData/DB/'
        if db_name in os.listdir(db_dir):
            db_path = os.path.join(db_dir, db_name)
            self._back_up_bi_home()
            shutil.rmtree(self.bi_home)
            shutil.copytree(db_path, self.bi_home)
            return True
        else:
            print '%s is not exist, please check!' % db_name
            return False

    def start_server(self):
        """
        Start server开启tomcat服务
        :return:True or False
        """
        start_server_path = os.path.abspath(os.path.join(self.bi_home, '../../tomcat/bin/'))
        if self._check_server_status():
            print "Server start success, it's now running on %s" % self.base_url
            return True
        else:
            try:
                p = subprocess.Popen('catalina.bat start', stdout=subprocess.PIPE, shell=True, cwd=start_server_path)
                # 由于tomcat启动日志太大，开启以下日志打印后会有性能问题
                # for line in p.stdout.readlines():
                #     print line
                start_server_status = self._check_server_status()
                if start_server_status:
                    print "Server start success, it's now running on %s" % self.base_url
                    return True
                else:
                    print "Time out, server start on %s fail!" % self.base_url
                    return False
            except Exception as e:
                print e

    def stop_server(self):
        """
        Stop server关闭tomcat服务
        :return:True/False
        """
        stop_server_path = os.path.abspath(os.path.join(self.bi_home, '../../tomcat/bin/'))
        if not self._check_server_status():
            print 'Server stop success!'
            return True
        else:
            try:
                subprocess.Popen('catalina.bat stop', stdout=subprocess.PIPE, shell=True, cwd=stop_server_path)
                time.sleep(3)
                if not self._check_server_status():
                    print 'Server stop success!'
                    return True
                else:
                    print 'Server stop fail!'
                    return False
            except Exception as e:
                print e
                return False

    def _check_server_status(self):
        """
        check the server is running or not
        :return:True/False
        """
        for i in range(1, 11):
            try:
                time.sleep(i)
                r = requests.get(self.base_url)
                if str(r.status_code).startswith("2"):
                    return True
                else:
                    pass
            except Exception as e:
                print "Try %d times, server is not running" % i
        else:
            return False

    def kill_driver(self):
        driver_list = ['chromedriver.exe', 'geckodriver.exe', 'IEDriverServer.exe', 'MicrosoftWebDriver.exe']
        for driver in driver_list:
            try:
                cmd = 'taskkill /F /IM %s' % driver
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
                for line in p.stdout.readlines():
                    print line
                time.sleep(3)
            except Exception as e:
                print e
                return False
        return True
