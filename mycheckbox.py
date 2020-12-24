from PyQt5 import QtCore, QtGui, QtWidgets

import pichub

class MyCheckBox(QtWidgets.QCheckBox):
    def mouseReleaseEvent(self,event):
        super(MyCheckBox,self).mouseReleaseEvent(event)
    