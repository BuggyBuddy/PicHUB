# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:29:11 2020

@author: y-yu18
"""

#open initialize
#初始化字典索引
def getpreference_type():
    i=0
    preference_dict={}
    for line in open("preference_type.txt","r"):   
        preference_dict[line[:-1]]=i
        i=i+1
    return preference_dict

def getpreference_poss():
    preference_list=[]#导入喜好值
    for line in open("preference_poss.txt","r"):
        preference_list.append(float(line[:-1]))
    #print(preference_list)
    return preference_list

def gettemp_type():
    i=0
    preference_dict={}
    for line in open("temp_tag.txt","r"):   
        preference_dict[line[:-1]]=i
        i=i+1
    return preference_dict

def gettemp_poss():
    preference_list=[]#导入喜好值
    for line in open("temp_possibility.txt","r"):
        preference_list.append(float(line[:-1]))
    #print(preference_list)
    return preference_list