# -*- coding: utf-8 -*-
"""
    和环境绑定的参数文件，传入../TestLibrary
    :param BI_HOME: 安装的BI产品的bihome所在路径
    :param BASE_URL: BI产品启动后的访问URL
    :param BROWSER: 浏览器类型, 支持Chrome,Firefox,IE,Edge
    :param DELAY: 每个Selenium Webdriver命令发送之间的间隔时间,默认单位为秒
"""
import os


base_path = os.path.dirname(__file__)
running_case_para = {
    'DB': ['DBPainter', 'Chart'],
    'BI_HOME': 'D:\Yonghong_Z-Suite_8.0.1\Yonghong\\bihome',
    'BASE_URL': 'http://127.0.0.1:8081/bi/Viewer',
    'BROWSER': 'ff',
    'DELAY': 0.2,
    'screenshot_dir': base_path + '/TestData/Screen/Result',
    'expect_picture_dir': base_path + '/TestData/Screen/Expect',
    'result_picture_dir': base_path + '/TestData/Screen/Result',
    'diff_picture_dir': base_path + '/TestData/Screen/Diff'
}
