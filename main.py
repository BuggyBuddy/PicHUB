# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui


import test5
import test2
import settings
import setting

import Entrance
from WPImage import *
from Crawler import *
from WPSource import*
import inceptionv3
import initialize
import open_initialize
from enlarge_graph import *

global ui
global setting
global graph1
global imageList
global wpSource

def cycleButtonClicked():
    setting.isCyclePlaying = True

def randomButtonClicked():
    setting.isCyclePlaying = False

def upButtonClicked():
    print(3)
    
def downButtonClicked():
    wpSource.nextPage()
    wpSource.run()
    imageList = ["C:\\Users\\ASUS\\wallpaper\\" + wpSource.genre + "\\" + x.fileName for x in wpSource.getImageList()]
    ui.label.setPixmap(QtGui.QPixmap(imageList[9]))
    ui.label_2.setPixmap(QtGui.QPixmap(imageList[10]))
    ui.label_3.setPixmap(QtGui.QPixmap(imageList[11]))
    ui.label_4.setPixmap(QtGui.QPixmap(imageList[12]))
    ui.label_5.setPixmap(QtGui.QPixmap(imageList[13]))
    ui.label_6.setPixmap(QtGui.QPixmap(imageList[14]))
    ui.label_7.setPixmap(QtGui.QPixmap(imageList[15]))
    ui.label_8.setPixmap(QtGui.QPixmap(imageList[16]))
    ui.label_9.setPixmap(QtGui.QPixmap(imageList[17]))

    
def modeButtonClicked():
    if ui.pushButton_ModeSelect.text() == "单张播放":
        ui.pushButton_ModeSelect.setText("连续播放")
        setting.isContinousPlayiing = True
    else:
        ui.pushButton_ModeSelect.setText("单张播放")
        setting.isContinousPlayiing = False

def queueButtonClicked():
    print(6)

def searchingButtonClicked():
    print(7)

def settingButtonClicked():
    print(8)

def widget1():
    graph1 = Enlarge(_Path = imageList[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test5.Ui_MainWindow()
    wpSource = WPSource("Pixabay",keyWord = "people|landscape|animal|car|sports")
    setWindow = setting.Settings()
    ui.setupUi(MainWindow)
    app1 = QApplication(sys.argv)
    graph1 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app2 = QApplication(sys.argv)
    graph2 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app3 = QApplication(sys.argv)
    graph3 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app4 = QApplication(sys.argv)
    graph4 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app5 = QApplication(sys.argv)
    graph5 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app6 = QApplication(sys.argv)
    graph6 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app7 = QApplication(sys.argv)
    graph7 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app8 = QApplication(sys.argv)
    graph8 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    app9 = QApplication(sys.argv)
    graph9 = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    ui.pushButton_Cycle.clicked.connect(cycleButtonClicked)
    ui.pushButton_Random.clicked.connect(randomButtonClicked)
    ui.pushButton_Up.clicked.connect(upButtonClicked)
    ui.pushButton_Down.clicked.connect(downButtonClicked)
    ui.pushButton_ModeSelect.clicked.connect(modeButtonClicked)
    ui.pushButton_QueueSelect.clicked.connect(queueButtonClicked)
    ui.pushButton_Searching.clicked.connect(searchingButtonClicked)
    ui.pushButton_Settings.clicked.connect(settingButtonClicked)
    ui.pushButton_Settings.clicked.connect(setWindow.show)
    ui.label.clicked.connect(widget1)
    ui.label.clicked.connect(graph1.show)
    ui.label_2.clicked.connect(graph2.show)
    ui.label_3.clicked.connect(graph3.show)
    ui.label_4.clicked.connect(graph4.show)
    ui.label_5.clicked.connect(graph5.show)
    ui.label_6.clicked.connect(graph6.show)
    ui.label_7.clicked.connect(graph7.show)
    ui.label_8.clicked.connect(graph8.show)
    ui.label_9.clicked.connect(graph9.show)
    wpSource.run()
    imageList = ["C:\\Users\\ASUS\\wallpaper\\" + wpSource.genre + "\\" + x.fileName for x in wpSource.getImageList()]
    MainWindow.show()
    ui.label.setPixmap(QtGui.QPixmap(imageList[0]))
    ui.label_2.setPixmap(QtGui.QPixmap(imageList[1]))
    ui.label_3.setPixmap(QtGui.QPixmap(imageList[2]))
    ui.label_4.setPixmap(QtGui.QPixmap(imageList[3]))
    ui.label_5.setPixmap(QtGui.QPixmap(imageList[4]))
    ui.label_6.setPixmap(QtGui.QPixmap(imageList[5]))
    ui.label_7.setPixmap(QtGui.QPixmap(imageList[6]))
    ui.label_8.setPixmap(QtGui.QPixmap(imageList[7]))
    ui.label_9.setPixmap(QtGui.QPixmap(imageList[8]))
    sys.exit(app.exec_())
