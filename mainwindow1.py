import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import shutil
from enlarge_graph import Enlarge

class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.resize(1200, 750)
        self.setWindowTitle("pichub")
        self.graph=QLabel(self)
        self.graph.resize(1200,675)
        self.graph.move(0,50)
        self.enlarge_button = QPushButton('显示详图',self)
        self.enlarge_button.clicked.connect(self.enlarge)
        self.change_button = QPushButton('更改路径',self)
        self.change_button.clicked.connect(self.change_path)
        self.make_layout()
        self.path='C:\\appcache\\1.png'
        self.enlarge_graph=Enlarge(self.path)
        


    

    def make_layout(self):
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.enlarge_button)
        self.button_layout.addWidget(self.change_button)
        self.wholelayoyt = QVBoxLayout()
        self.wholelayoyt.addWidget(self.graph)
        self.wholelayoyt.addLayout(self.button_layout)
        self.setLayout(self.wholelayoyt)

    def enlarge(self):
        self.enlarge_graph=Enlarge(self.path)
        self.enlarge_graph.show()

    def show_messagebox(self):
        QMessageBox.about(self, '提示', '下载成功！') 

    def change_path(self):
        if self.path=='C:\\appcache\\1.png':
            self.path='C:\\appcache\\2.png'
        else:
            self.path='C:\\appcache\\1.png'
        QMessageBox.about(self,'提示','更改成功！')

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = mainwindow()  #临时文件位置
    my.show()
    sys.exit(app.exec_())