# -*- coding: utf-8 -*-
import unittest
#import HTMLTestRunner
from BeautifulReport import BeautifulReport as bf  #导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
import initialize
import update_weights
import os
import glob
class TestClassifier(unittest.TestCase):
    def setUp(self):
        print("setUp begins!")
        initialize.initialize()
        preference_list=update_weights.open_initialize.getpreference_type_list()
        self.assertEqual(len(preference_list),1000,msg='the list is not 1000 length!')
        preference_poss=update_weights.open_initialize.getpreference_poss()
        self.assertEqual(len(preference_poss),1000,msg='the poss is not 1000 length!')
        

    def tearDown(self):
        print("tearDown begins!")
    def test1(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference1')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test2(self):
        print("test2 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference2')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test3(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference3')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test4(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference4')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test5(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference5')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test6(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference6')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test7(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference7')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test8(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference8')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    
    def test9(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference9')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    def test10(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference10')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    
    def test11(self):
        print("test1 begins!")
        model_dir=os.getcwd()
        image_dir=os.path.join(
          model_dir, 'preference11')
        paths = glob.glob(os.path.join(image_dir,'*.jpg'))
        temp_type,temp_possition=initialize.inceptionv3.predict(paths)
        i=0
        while i<len(temp_possition):
            self.assertLessEqual(temp_possition[i],1,msg='出现了大于1的概率')
            i=i+1
        result_poss1=update_weights.open_initialize.getpreference_poss()
        j=0
        update_weights.modify()
        result_poss2=update_weights.open_initialize.getpreference_poss()
        while j<len(result_poss1):
            self.assertLessEqual(result_poss1[j],result_poss2[j],msg='后概率大于前概率')
            j=j+1
    
            



suite = unittest.TestSuite()  #定义一个测试集合
suite.addTest(unittest.makeSuite(TestClassifier))  #把写的用例加进来（将TestCalc类）加进来
run = bf(suite) #实例化BeautifulReport模块
run.report(filename='testclassifier',description='分类器测试')