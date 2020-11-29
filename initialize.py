# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:07:06 2020

@author: y-yu18
"""
import os
import inceptionv3
def initialize():
#initialize   
    code_dir=os.getcwd()
    file_dir1=os.path.join(code_dir,'preference_type.txt')
    with open(file_dir1,'w') as f1:
        node_lookup = inceptionv3.NodeLookup()
        for i in range(1,1001):#21842+1
            f1.write('%s\n'%(node_lookup.id_to_string(i)))
    f1.close()#设置初始的元组
    file_dir2=os.path.join(code_dir,'preference_poss.txt')
    with open(file_dir2,'w') as f2:
        for i in range(1,1001):
            f2.write('0\n')
    f2.close()#设置概率为0
#第一次打开软件时，运行该程序，之后不再运行