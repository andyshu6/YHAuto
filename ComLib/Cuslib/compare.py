#coding=utf-8  
from PIL import Image
#使用第三方库：Pillow
import math
import operator
from functools import reduce
class compare(object):
	def get_expectname(self,picname):
		image1=Image.open('F:\\screen\\expect\\'+picname+'.png')
	#把图像对象转换为直方图数据，存在list h1、h2 中
		h1=image1.histogram()
		return h1
	def get_resultname(self,picname):
		image2=Image.open('F:\\screen\\result\\'+picname+'.png')
		h2=image2.histogram()
		return h2
	def compare(self,picname):
		exp=get_expectname(picname)
		rel=get_resultname(picname)
		result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, exp, rel)))/len(exp) )
		if result<10:
			return 'true'
		return 'false'

	'''
	sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
	operator.add(x,y)对应表达式：x+y
	这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
	'''
	#result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
	def get_hight(self,style):
		s=style
		a=s.split(' ')
		b=a[3].split('p')
		c=b[0]
		return c
	#输入style返回网页高度