# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:11:39 2020

@author: y-yu18
"""

'''
Updated on Sat Dec 19

@author: cthmd

调用当前文件进行分类器、推荐器、爬虫操作
可调用函数：
分类器
	获取分类列表与数组    classifer(bool 是否第一次运行)
		输出为1. string[] 分类列表 2. float[] 对于标签的数值

推荐器
	爬虫推荐器类 WebRecommender
	构造函数            WebRecommender(string 关键词)
	获取推荐            getRecommendList()
        更新器        renew() 更新用户的喜好值。
爬虫 
	爬虫类 WPSource
	构造函数             WPSource(string 网站源, string 图片类别, string 搜索词)
	获取下一页搜索结果    nextPage()
	获取第n页搜索结果     toPage(int 页码)
	更改搜索词           changeKeyWord(string 关键词)
	更改网站源           changeSourceWeb(string 网站源)
	记录已使用           markUsed(string 壁纸文件名)
	记录喜欢             markLike(string 壁纸文件名, bool 喜欢)
	返回喜欢列表         getLike()
	库存数量             inStock()
	开始爬虫             run()
	获取未使用壁纸列表    getImageList()

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

def get_max_dict():
    preference_dict=open_initialize.getpreference_type_list()
    preference_poss=open_initialize.getpreference_poss()
    max_poss=[0,0,0,0,0]
    max_dict=['','','','','']
    for i in range(len(preference_poss)):
        if preference_poss[i]>min(max_poss):
            #print(i)
            c=max_poss.index(min(max_poss))
            #print(c)
            max_poss[c]=preference_poss[i]
            max_dict[c]=preference_dict[i]
            sum_poss=sum(max_poss)
            for i in range(1,5):
                max_poss[i]=max_poss[i]/sum_poss
    return max_poss,max_dict

def classifer(firstRun):
	if firstRun == True:
		initialize.initialize()
	return inceptionv3.predict()

def localRecommender(maxPoss, maxType):
	for i in range(5):
		wpSource.changeKeyWord(maxType[i])
		for p in range(int(maxPoss[i]*10)):
			wpSource.nextPage()
			wpSource.run()

if __name__ == "__main__":
	wpSource = WPSource("Unsplash", keyWord = "cat")

	result_type, result_poss = classifer(True)
	max_poss, max_dict = get_max_dict()
	keywordList = localRecommender(max_poss, max_dict)

	print(["\\wallpaper\\" + wpSource.genre + "\\" + x.fileName for x in wpSource.getImageList()])


