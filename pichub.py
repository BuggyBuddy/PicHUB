# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui

import threading

import test8
import settingWindow
import ListSelecter
import NewList
from WPPlayList import WPPlayList
import Player

import Entrance
from WPImage import *
from Crawler import *
from WPSource import*
import inceptionv3
import initialize
import open_initialize
from enlarge_graph import *

page = 0
pageMax = 0
ui = test8.Ui_MainWindow()
wpSource = WPSource("Pixabay",keyWord = "people|landscape|animal|car|sports|anime|buildings|plants|sci-fi|")
listDic = {}
paperlist = []


global listSelecterUI
global newListUI


def cycleButtonClicked():
    print(1)

def randomButtonClicked():
    print(2)

def upButtonClicked():
    if pichub.page > 0:
        pichub.page = pichub.page - 1
        showWallPaper()
    
def downButtonClicked():
    pichub.wpSource.nextPage()
    pichub.page += 1
    if pichub.page > pichub.pageMax:
        pichub.wpSource.run()
        pichub.pageMax = pichub.page
    else:
        showWallPaper()
    
def modeButtonClicked():
    if pichub.ui.pushButton_ModeSelect.text() == "单张播放":
        pichub.ui.pushButton_ModeSelect.setText("连续播放")
    else:
        pichub.ui.pushButton_ModeSelect.setText("单张播放")

def deleteListButtonClicked():
    listSelecterUI.listWidget.takeItem(listSelecterUI.listWidget.currentRow())
    pichub.ui.listWidget.takeItem(listSelecterUI.listWidget.currentRow())
    del pichub.paperlist[listSelecterUI.listWidget.currentRow()]
    print(pichub.paperlist)

def newListConfirmButton():
    if newListUI.textEdit.toPlainText() != "":
        listSelecterUI.listWidget.addItem(newListUI.textEdit.toPlainText())
        pichub.ui.listWidget.addItem(newListUI.textEdit.toPlainText())
        wp = WPPlayList(newListUI.textEdit.toPlainText())
        pichub.paperlist.append(wp)
        print(pichub.paperlist)

def queueChange():
    pichub.ui.label_Queue.setText(listSelecterUI.listWidget.item(listSelecterUI.listWidget.currentRow()).text())
    pichub.paperlist[listSelecterUI.listWidget.currentRow()]#当前被选中的壁纸列表

def newListButtonClicked():
    newListUI.textEdit.setText("")

def queueButtonClicked():
    print(6)

def searchingButtonClicked():
    if pichub.ui.lineEdit.text() is not "":
        pichub.wpSource.changeKeyWord(pichub.ui.lineEdit.text())
        pichub.wpSource.changeSourceWeb(pichub.ui.comboBox.currentText())
        pichub.wpSource.WPList = []
        pichub.page = 0
        pichub.pageMax = 0
        pichub.wpSource.run()


def settingButtonClicked():
    print(8)

def showWallPaper():
    pichub.ui.label.path = pichub.wpSource.getImageList()[pichub.page*9].getFilePath()
    pichub.ui.label_2.path = pichub.wpSource.getImageList()[pichub.page*9+1].getFilePath()
    pichub.ui.label_3.path = pichub.wpSource.getImageList()[pichub.page*9+2].getFilePath()
    pichub.ui.label_4.path = pichub.wpSource.getImageList()[pichub.page*9+3].getFilePath()
    pichub.ui.label_5.path = pichub.wpSource.getImageList()[pichub.page*9+4].getFilePath()
    pichub.ui.label_6.path = pichub.wpSource.getImageList()[pichub.page*9+5].getFilePath()
    pichub.ui.label_7.path = pichub.wpSource.getImageList()[pichub.page*9+6].getFilePath()
    pichub.ui.label_8.path = pichub.wpSource.getImageList()[pichub.page*9+7].getFilePath()
    pichub.ui.label_9.path = pichub.wpSource.getImageList()[pichub.page*9+8].getFilePath()
    pichub.ui.label.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9].getFilePath()))
    pichub.ui.label_2.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+1].getFilePath()))
    pichub.ui.label_3.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+2].getFilePath()))
    pichub.ui.label_4.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+3].getFilePath()))
    pichub.ui.label_5.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+4].getFilePath()))
    pichub.ui.label_6.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+5].getFilePath()))
    pichub.ui.label_7.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+6].getFilePath()))
    pichub.ui.label_8.setPixmap(QtGui.QPixmap(pichub.wpSource.getImageList()[pichub.page*9+7].getFilePath()))
    pichub.ui.label_9.setPixmap(QtGui.QPixmap(pichub.pichub.wpSource.getImageList()[pichub.page*9+8].getFilePath()))

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
    pichub.wpSource.WPList = []
    pichub.page = 0
    pichub.pageMax = 0
    print(keyword)
    pichub.wpSource.run()

def confirmButtonClicked():
    pichub.updateKeywords()
    pichub.wpSource.changeSourceWeb(pichub.ui.comboBox.currentText())
    pichub.wpSource.WPList = []
    pichub.page = 0
    pichub.pageMax = 0
    pichub.wpSource.run()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    
    listSelecterDialog = QMainWindow()
    newListDialog = QMainWindow()
    listSelecterUI = ListSelecter.Ui_Dialog()
    newListUI = NewList.Ui_Dialog()
    listSelecterUI.setupUi(listSelecterDialog)
    newListUI.setupUi(newListDialog)
    listSelecterUI.listWidget.addItem("我喜欢")
    listSelecterUI.pushButton.clicked.connect(newListDialog.show)
    listSelecterUI.pushButton.clicked.connect(newListButtonClicked)
    listSelecterUI.pushButton_2.clicked.connect(listSelecterDialog.close)
    listSelecterUI.pushButton_2.clicked.connect(queueChange)
    listSelecterUI.pushButton_3.clicked.connect(deleteListButtonClicked)
    newListUI.pushButton.clicked.connect(newListDialog.close)
    newListUI.pushButton_2.clicked.connect(newListConfirmButton)
    newListUI.pushButton_2.clicked.connect(newListDialog.close)



    MainWindow = QMainWindow()
    setWindow = settingWindow.Settings()
    pichub.ui.setupUi(MainWindow)
    pichub.ui.pushButton_Cycle.clicked.connect(cycleButtonClicked)
    pichub.ui.pushButton_Random.clicked.connect(randomButtonClicked)
    pichub.ui.pushButton_Up.clicked.connect(upButtonClicked)
    pichub.ui.pushButton_Down.clicked.connect(downButtonClicked)
    pichub.ui.pushButton_ModeSelect.clicked.connect(modeButtonClicked)
    pichub.ui.pushButton_QueueSelect.clicked.connect(queueButtonClicked)
    pichub.ui.pushButton_QueueSelect.clicked.connect(listSelecterDialog.show)
    pichub.ui.pushButton_Searching.clicked.connect(searchingButtonClicked)
    pichub.ui.pushButton_Settings.clicked.connect(settingButtonClicked)
    pichub.ui.pushButton_Settings.clicked.connect(setWindow.show)
    pichub.ui.pushButton_Confirm.clicked.connect(confirmButtonClicked)
    pichub.ui.label.clicked.connect(pichub.ui.label.enlarge)
    pichub.ui.label_2.clicked.connect(pichub.ui.label_2.enlarge)
    pichub.ui.label_3.clicked.connect(pichub.ui.label_3.enlarge)
    pichub.ui.label_4.clicked.connect(pichub.ui.label_4.enlarge)
    pichub.ui.label_5.clicked.connect(pichub.ui.label_5.enlarge)
    pichub.ui.label_6.clicked.connect(pichub.ui.label_6.enlarge)
    pichub.ui.label_7.clicked.connect(pichub.ui.label_7.enlarge)
    pichub.ui.label_8.clicked.connect(pichub.ui.label_8.enlarge)
    pichub.ui.label_9.clicked.connect(pichub.ui.label_9.enlarge)
    pichub.paperlist.append(WPPlayList("我喜欢"))
    pichub.ui.label_Queue.adjustsFontSizeToFitWidth = True


    
    pichub.wpSource.run()
    MainWindow.show()
    sys.exit(app.exec_())
