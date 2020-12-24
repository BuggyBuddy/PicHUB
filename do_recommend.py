# -*- coding: utf-8 -*-
#整合
import inceptionv3
import initialize
import open_initialize
from WPImage import *
from Crawler import *
from WPSource import *

def do_recommend():
    wpSource = WPSource("Unsplash", keyWord = "girl")
    maxPoss,maxType= get_max_dict()
    for i in range(5):
        maxType[i]=maxType[i].replace(' ','%20')
    recommenderThread = threading.Thread(target = localRecommender, args = [maxPoss, maxType, wpSource])
    recommenderThread.start()