# -*- coding: UTF-8 -*-
import argparse
import math
import operator
from skimage.measure import compare_ssim
from functools import reduce
# 使用第三方库：Pillow
import cv2
import imutils
from PIL import Image
from CusBase import CusBase


class ImageCompare(CusBase):
    """
    image compare类
    """

    def __init__(self, running_param):
        super(ImageCompare, self).__init__(running_param)

    # 把图像对象转换为直方图数据，存在list h1、h2 中
    def get_expectname(self, picname):
        image1 = Image.open(self.running_param['expect_picture_dir'] + picname + '.png')
        h1 = image1.histogram()
        return h1

    def get_resultname(self, picname):
        image2 = Image.open(self.running_param['result_picture_dir'] + picname + '.png')
        h2 = image2.histogram()
        return h2

    def compare(self, picname):
        exp = self.get_expectname(picname)
        rel = self.get_resultname(picname)
        result = math.sqrt(reduce(operator.add,  list(
            map(lambda a, b: (a - b)**2, exp, rel))) / len(exp))
        if result < 1:
            print(result)
            return 'true'
        else:
            print(result)
            imageA = cv2.imread(
                self.running_param['expect_picture_dir'] + picname + '.png')
            imageB = cv2.imread(
                self.running_param['result_picture_dir'] + picname + '.png')

            grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            diff = (diff * 255).astype("uint8")
            print("SSIM:{}".format(score))
            thresh = cv2.threshold(
                diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(
                thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.imshow("Modified", imageB)
            cv2.imwrite(self.running_param[
                        'diff_picture_dir'] + picname + '.png', imageB)
            cv2.destroyAllWindows()
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return 'false'

        '''
           sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
           operator.add(x,y)对应表达式：x+y
           这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
        '''
        # result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样

    def get_hight(self, style):
        """
        输入style返回网页高度
        :param style:
        :return:
        """
        s = style
        a = s.split(' ')
        b = a[3].split('p')
        c = b[0]
        return c


if __name__ == '__main__':
    i = ImageCompare()
    picname = u'表格渲染'
    i.compare(picname)
