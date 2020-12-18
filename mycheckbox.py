from PyQt5 import QtCore, QtGui, QtWidgets

import pichub

class MyCheckBox(QtWidgets.QCheckBox):
    def mousePressEvent(self,event):
        super(MyCheckBox,self).mousePressEvent(event)
        pichub.updateKeywords()
        pichub.wpSource.run()
    