import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import shutil

class Enlarge(QWidget):
    def __init__(self,_Path):
        super(Enlarge, self).__init__()
        self.resize(1200, 750)
        self.path=_Path
        self.setWindowTitle("显示图片")
        self.graph=QLabel(self)
        self.graph.resize(1200,675)
        self.graph.move(0,50)
        self.open_image()
        self.download_button = QPushButton('下载',self)
        self.download_button.clicked.connect(self.download)
        self.change_button = QPushButton('下载并设为壁纸',self)
        self.collect_button = QPushButton('收藏',self)
        self.make_layout()
        


    def open_image(self):
        self.jpg = QtGui.QPixmap(self.path).scaled(self.graph.width(), self.graph.height(),aspectRatioMode=Qt.KeepAspectRatio)
        self.graph.setPixmap(self.jpg)

    def make_layout(self):
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.download_button)
        self.button_layout.addWidget(self.change_button)
        self.button_layout.addWidget(self.collect_button)
        self.wholelayoyt = QVBoxLayout()
        self.wholelayoyt.addWidget(self.graph)
        self.wholelayoyt.addLayout(self.button_layout)
        self.setLayout(self.wholelayoyt)

    def download(self):
        imgName, imgType = QFileDialog.getSaveFileName(self, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
        shutil.copyfile(self.path,  imgName)  #保存到用户选择的位置
        self.show_messagebox()
        self.close()

    def show_messagebox(self):
        QMessageBox.about(self, '提示', '下载成功！') 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = Enlarge(_Path = 'C:\\appcache\\1.png')  #临时文件位置
    my.show()
    sys.exit(app.exec_())