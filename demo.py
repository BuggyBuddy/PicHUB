# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import ListSelecter
import NewList

global listSelecterUI
global newListUI

def deleteListButtonClicked():
    listSelecterUI.listWidget.takeItem(listSelecterUI.listWidget.currentRow())

def newListConfirmButton():
    if newListUI.textEdit.toPlainText() != "":
        listSelecterUI.listWidget.addItem(newListUI.textEdit.toPlainText())

def newListButtonClicked():
    newListUI.textEdit.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    listSelecterDialog = QMainWindow()
    newListDialog = QMainWindow()
    listSelecterUI = ListSelecter.Ui_Dialog()
    newListUI = NewList.Ui_Dialog()
    listSelecterUI.setupUi(listSelecterDialog)
    newListUI.setupUi(newListDialog)
    listSelecterDialog.show()
    listSelecterUI.listWidget.addItem("我喜欢")
    listSelecterUI.pushButton.clicked.connect(newListDialog.show)
    listSelecterUI.pushButton.clicked.connect(newListButtonClicked)
    listSelecterUI.pushButton_2.clicked.connect(listSelecterDialog.close)
    listSelecterUI.pushButton_3.clicked.connect(deleteListButtonClicked)
    newListUI.pushButton.clicked.connect(newListDialog.close)
    newListUI.pushButton_2.clicked.connect(newListConfirmButton)
    newListUI.pushButton_2.clicked.connect(newListDialog.close)
    sys.exit(app.exec_())