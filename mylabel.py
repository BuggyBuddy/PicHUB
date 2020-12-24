from PyQt5 import QtCore, QtGui, QtWidgets

from enlarge_graph import Enlarge

class MyLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()  # 定义clicked信号
    path = 'C:\\appcache\\1.png'
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()  # 发送clicked信号
    
    def enlarge(self):
        self.enlarge_graph=Enlarge(self.path)
        self.enlarge_graph.show()
        
