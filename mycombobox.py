from PyQt5 import QtCore, QtGui, QtWidgets

import pichub

class MyComboBox(QtWidgets.QComboBox):
    def mouseReleaseEvent(self,event):
        super(MyComboBox,self).mouseReleaseEvent(event)
        print(1)
        pichub.wpSource.changeSourceWeb = self.currentText()
        pichub.wpSource.run()
