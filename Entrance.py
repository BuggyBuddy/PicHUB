# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:11:39 2020

@author: y-yu18
"""

'''
Edited on Sat Dec 5

@author: cthmd

调用当前文件进行分类器、推荐器、爬虫操作
可调用函数：
分类器
	获取分类列表与数组    classifer(bool 是否第一次运行)
		输出为1. string[] 分类列表 2. float[] 对于标签的数值

推荐器


爬虫 
	爬虫类 WPSource
	构造函数             WPSource(string 网站源, string 图片类别, string 搜索词)
	获取下一页搜索结果    nextPage()
	更改网站源           changeSourceWeb(string 网站源)
	开始爬虫             run()
	获取壁纸列表         getImageList()

	壁纸图片类 WPImage 通过壁纸列表访问
		获取标签列表     getLabel()
		添加标签        	addLabel(string 标签)
		获取图片路径     getFilePath()

'''

import inceptionv3
import initialize
import open_initialize
from WPImage import *
from Crawler import *
from WPSource import *

wpSource = None

def classifer(firstRun):
	if firstRun == True:
		initialize.initialize()#第一次运行的时候运行，后面把这行注释掉
	return inceptionv3.predict()

def recommender(result_type, result_poss):
	#添加推荐器，返回需要搜索的结果
	return result_type[1]

	

if __name__ == "__main__":
	result_type, result_poss = classifer(True)
	keywordList = recommender(result_type, result_poss)

	wpSource = WPSource("Pexels", keyWord = keywordList)
	wpSource.nextPage()#获取下一页，每一页9张
	wpSource.changeSourceWeb("Unsplash")#更改网站源
	wpSource.run()#开始爬

