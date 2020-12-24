# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui

import threading

import test8
import settingWindow
import ListSelecter
import NewList
import WPPlayList

import Entrance
from WPImage import *
from Crawler import *
from WPSource import*
from Player import *
import inceptionv3
import initialize
import open_initialize
from enlarge_graph import *
from likeAWallPaper import *
import update_weights

page = 0
pageMax = 0
graghNum = 0
ui = test8.Ui_MainWindow()
wpSource = WPSource("Pixabay",keyWord = "people|landscape|animal|car|sports|anime|buildings|plants|sci-fi|")
paperlist = []
app = QApplication(sys.argv)
setWindow = settingWindow.Settings()

listSelecterDialog = QMainWindow()
newListDialog = QMainWindow()
listSelecterUI = ListSelecter.Ui_Dialog()
newListUI = NewList.Ui_Dialog()

def cycleButtonClicked():
    Player.playInOrder()

def randomButtonClicked():
    Player.playInShuffle()

def upButtonClicked():
    if pichub.page > 0:
        pichub.page = pichub.page - 1
        showWallPaper()
    
def downButtonClicked():
    pichub.wpSource.nextPage()
    pichub.page += 1
    pichub.pageMax = len(pichub.wpSource.getImageList())/9
    if pichub.page > pichub.pageMax:
        pichub.wpSource.run()
        pichub.pageMax = pichub.page
    else:
        showWallPaper()
    
def modeButtonClicked():
    if pichub.ui.pushButton_ModeSelect.text() == "单张播放":
        pichub.ui.pushButton_ModeSelect.setText("连续播放")
        Player.playInOrder()
    else:
        pichub.ui.pushButton_ModeSelect.setText("单张播放")
        Player.stop()

def deleteListButtonClicked():
    listSelecterUI.listWidget.takeItem(listSelecterUI.listWidget.currentRow())
    pichub.ui.listWidget.takeItem(listSelecterUI.listWidget.currentRow())
    del pichub.paperlist[listSelecterUI.listWidget.currentRow()]

def newListConfirmButton():
    if newListUI.textEdit.toPlainText() != "":
        listSelecterUI.listWidget.addItem(pichub.newListUI.textEdit.toPlainText())
        pichub.ui.listWidget.addItem(pichub.newListUI.textEdit.toPlainText())
        wp = WPPlayList.WPPlayList(pichub.newListUI.textEdit.toPlainText())
        pichub.paperlist.append(wp)

def queueChange():
    if (listSelecterUI.listWidget.currentRow() == -1):
        pichub.ui.label_Queue.setText(listSelecterUI.listWidget.item(listSelecterUI.listWidget.currentRow() + 1).text())
    else:
        pichub.ui.label_Queue.setText(listSelecterUI.listWidget.item(listSelecterUI.listWidget.currentRow()).text())

    Player.setWPList(pichub.paperlist[listSelecterUI.listWidget.currentRow()])

def collect():
    print(pichub.graghNum)
    if pichub.graghNum != 0:
        print("successful")
        rowIndex = 0
        if (listSelecterUI.listWidget.currentRow() == -1):
            rowIndex = listSelecterUI.listWidget.currentRow() + 1
        else:
            rowIndex = listSelecterUI.listWidget.currentRow()

        
        if pichub.graghNum == 1:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9])
        if pichub.graghNum == 2:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+1].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+1])
        if pichub.graghNum == 3:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+2].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+2])
        if pichub.graghNum == 4:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+3].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+3])
        if pichub.graghNum == 5:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+4].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+4])
        if pichub.graghNum == 6:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+5].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+5])
        if pichub.graghNum == 7:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+6].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+6])
        if pichub.graghNum == 8:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+7].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+7])
        if pichub.graghNum == 9:
            paperlist[rowIndex].append(os.path.abspath(pichub.wpSource.getImageList()[pichub.page*9+8].getFilePath()))
            likeAWallPaper(pichub.wpSource.getImageList()[pichub.page*9+8])
        print(paperlist[rowIndex].wallpapers)

def newListButtonClicked():
    newListUI.textEdit.setText("")

def queueButtonClicked():
    pichub.graghNum = 0

def enlarge1():
    pichub.graghNum = 1

def enlarge2():
    pichub.graghNum = 2

def enlarge3():
    pichub.graghNum = 3

def enlarge4():
    pichub.graghNum = 4

def enlarge5():
    pichub.graghNum = 5

def enlarge6():
    pichub.graghNum = 6

def enlarge7():
    pichub.graghNum = 7

def enlarge8():
    pichub.graghNum = 8

def enlarge9():
    pichub.graghNum = 9

def searchingButtonClicked():
    if pichub.ui.lineEdit.text() is not "":
        pichub.ui.lineEdit.setText(pichub.ui.lineEdit.text().replace(' ','%20'))
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
    pichub.wpSource.run()

def confirmButtonClicked():
    pichub.updateKeywords()
    pichub.wpSource.changeSourceWeb(pichub.ui.comboBox.currentText())
    pichub.wpSource.WPList = []
    pichub.page = 0
    pichub.pageMax = 0
    pichub.wpSource.run()

def showList():
    print(pichub.ui.listWidget.currentRow())

def quit(self):#app退出
    inceptionv3.predict()
    print('the predict is execute.')
    update_weights.modify()
    self.close()
if __name__ == '__main__':
    #To Do:读settings参数，给Player设置
    Player.setIntervalTime(10)
    #Player.__play()




    pichub.listSelecterUI.setupUi(pichub.listSelecterDialog)
    pichub.newListUI.setupUi(pichub.newListDialog)
    pichub.listSelecterUI.listWidget.addItem("我喜欢")
    pichub.listSelecterUI.pushButton.clicked.connect(pichub.newListDialog.show)
    pichub.listSelecterUI.pushButton.clicked.connect(pichub.newListButtonClicked)
    pichub.listSelecterUI.pushButton_2.clicked.connect(pichub.listSelecterDialog.close)
    pichub.listSelecterUI.pushButton_2.clicked.connect(pichub.queueChange)
    pichub.listSelecterUI.pushButton_2.clicked.connect(pichub.collect)
    pichub.listSelecterUI.pushButton_3.clicked.connect(pichub.deleteListButtonClicked)
    pichub.newListUI.pushButton.clicked.connect(pichub.newListDialog.close)
    pichub.newListUI.pushButton_2.clicked.connect(pichub.newListConfirmButton)
    pichub.newListUI.pushButton_2.clicked.connect(pichub.newListDialog.close)



    MainWindow = QMainWindow()
    pichub.ui.setupUi(MainWindow)
    pichub.ui.pushButton_Cycle.clicked.connect(cycleButtonClicked)
    pichub.ui.pushButton_Random.clicked.connect(randomButtonClicked)
    pichub.ui.pushButton_Up.clicked.connect(upButtonClicked)
    pichub.ui.pushButton_Down.clicked.connect(downButtonClicked)
    pichub.ui.pushButton_ModeSelect.clicked.connect(modeButtonClicked)
    pichub.ui.pushButton_QueueSelect.clicked.connect(queueButtonClicked)
    pichub.ui.pushButton_QueueSelect.clicked.connect(pichub.listSelecterDialog.show)
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
    pichub.ui.label.clicked.connect(pichub.enlarge1)
    pichub.ui.label_2.clicked.connect(pichub.enlarge2)
    pichub.ui.label_3.clicked.connect(pichub.enlarge3)
    pichub.ui.label_4.clicked.connect(pichub.enlarge4)
    pichub.ui.label_5.clicked.connect(pichub.enlarge5)
    pichub.ui.label_6.clicked.connect(pichub.enlarge6)
    pichub.ui.label_7.clicked.connect(pichub.enlarge7)
    pichub.ui.label_8.clicked.connect(pichub.enlarge8)
    pichub.ui.label_9.clicked.connect(pichub.enlarge9)
    #pichub.ui.listWidget.itemDoubleClicked.connnect(pichub.showList)
    pichub.paperlist.append(WPPlayList.WPPlayList("我喜欢"))
    pichub.ui.label_Queue.adjustsFontSizeToFitWidth = True
    Player.setWPList(pichub.paperlist[0])



    
    pichub.wpSource.run()

    #加入更新偏好值的功能
    
    MainWindow.show()
    sys.exit(pichub.app.exec_())
    #self.quit()