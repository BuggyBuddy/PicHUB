# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui

import threading

import test6
import test2
import settings
import settingWindow


import Entrance
from WPImage import *
from Crawler import *
from WPSource import*
import inceptionv3
import initialize
import open_initialize
from enlarge_graph import *

ui = test6.Ui_MainWindow()
setting = settings.Settings()
wpSource = WPSource("Pixabay",keyWord = "people|landscape|animal|car|sports|anime|buildings|plants|sci-fi|")

def cycleButtonClicked():
    pichub.setting.isCyclePlaying = True

def randomButtonClicked():
    pichub.setting.isCyclePlaying = False

def upButtonClicked():
    if pichub.setting.page > 0:
        pichub.setting.page = pichub.setting.page - 1
        showWallPaper()
    
def downButtonClicked():
    pichub.wpSource.nextPage()
    pichub.setting.page += 1
    if pichub.setting.page > pichub.setting.pageMax:
        pichub.wpSource.run()
        pichub.setting.pageMax = pichub.setting.page
    else:
        showWallPaper()
    

    
def modeButtonClicked():
    if pichub.ui.pushButton_ModeSelect.text() == "单张播放":
        pichub.ui.pushButton_ModeSelect.setText("连续播放")
        pichub.setting.isContinousPlayiing = True
    else:
        pichub.ui.pushButton_ModeSelect.setText("单张播放")
        pichub.setting.isContinousPlayiing = False

def queueButtonClicked():
    print(6)

def searchingButtonClicked():
    print(7)

def settingButtonClicked():
    print(8)

def showWallPaper():
    pichub.ui.label.path = pichub.wpSource.getImageList()[pichub.setting.page*9].getFilePath()
    pichub.ui.label_2.path = pichub.wpSource.getImageList()[pichub.setting.page*9+1].getFilePath()
    pichub.ui.label_3.path = pichub.wpSource.getImageList()[pichub.setting.page*9+2].getFilePath()
    pichub.ui.label_4.path = pichub.wpSource.getImageList()[pichub.setting.page*9+3].getFilePath()
    pichub.ui.label_5.path = pichub.wpSource.getImageList()[pichub.setting.page*9+4].getFilePath()
    pichub.ui.label_6.path = pichub.wpSource.getImageList()[pichub.setting.page*9+5].getFilePath()
    pichub.ui.label_7.path = pichub.wpSource.getImageList()[pichub.setting.page*9+6].getFilePath()
    pichub.ui.label_8.path = pichub.wpSource.getImageList()[pichub.setting.page*9+7].getFilePath()
    pichub.ui.label_9.path = pichub.wpSource.getImageList()[pichub.setting.page*9+8].getFilePath()
    pichub.ui.label.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9].getFilePath()))
    pichub.ui.label_2.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+1].getFilePath()))
    pichub.ui.label_3.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+2].getFilePath()))
    pichub.ui.label_4.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+3].getFilePath()))
    pichub.ui.label_5.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+4].getFilePath()))
    pichub.ui.label_6.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+5].getFilePath()))
    pichub.ui.label_7.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+6].getFilePath()))
    pichub.ui.label_8.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.setting.page*9+7].getFilePath()))
    pichub.ui.label_9.setPixmap(QtGui.QPixmap(pichub.pichub.wpSource.getImageList()[pichub.setting.page*9+8].getFilePath()))

def updateKeywords():
    keyword = ""
    if pichub.ui.checkBox_Animal.isChecked():
        keyword += "animal|"
    if pichub.ui.checkBox_Anime.isChecked():
        keyword += "anime|"
    if pichub.ui.checkBox_Car.isChecked():
        keyword += "car|"
    if pichub.ui.checkBox_Landscape.isChecked():
        keyword += "landscape|"
    if pichub.ui.checkBox_People.isChecked():
        keyword += "people|"
    if pichub.ui.checkBox_Plants.isChecked():
        keyword += "plants|"
    if pichub.ui.checkBox_Scifi.isChecked():
        keyword += "sci-fi|"
    if pichub.ui.checkBox_Sports.isChecked():
        keyword += "sports|"
    if pichub.ui.checkBox_Buildings.isChecked():
        keyword += "buildings|"
    if keyword is not "":
        keyword = keyword[:len(keyword)-1]
    pichub.wpSource.changeKeyWord(keyword)
    pichub.wpSource.run()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    setWindow = settingWindow.Settings()
    pichub.ui.setupUi(MainWindow)
    pichub.ui.pushButton_Cycle.clicked.connect(cycleButtonClicked)
    pichub.ui.pushButton_Random.clicked.connect(randomButtonClicked)
    pichub.ui.pushButton_Up.clicked.connect(upButtonClicked)
    pichub.ui.pushButton_Down.clicked.connect(downButtonClicked)
    pichub.ui.pushButton_ModeSelect.clicked.connect(modeButtonClicked)
    pichub.ui.pushButton_QueueSelect.clicked.connect(queueButtonClicked)
    pichub.ui.pushButton_Searching.clicked.connect(searchingButtonClicked)
    pichub.ui.pushButton_Settings.clicked.connect(settingButtonClicked)
    pichub.ui.pushButton_Settings.clicked.connect(setWindow.show)
    pichub.ui.label.clicked.connect(pichub.ui.label.enlarge)
    pichub.ui.label_2.clicked.connect(pichub.ui.label_2.enlarge)
    pichub.ui.label_3.clicked.connect(pichub.ui.label_3.enlarge)
    pichub.ui.label_4.clicked.connect(pichub.ui.label_4.enlarge)
    pichub.ui.label_5.clicked.connect(pichub.ui.label_5.enlarge)
    pichub.ui.label_6.clicked.connect(pichub.ui.label_6.enlarge)
    pichub.ui.label_7.clicked.connect(pichub.ui.label_7.enlarge)
    pichub.ui.label_8.clicked.connect(pichub.ui.label_8.enlarge)
    pichub.ui.label_9.clicked.connect(pichub.ui.label_9.enlarge)
    pichub.wpSource.run()
    MainWindow.show()
    sys.exit(app.exec_())
