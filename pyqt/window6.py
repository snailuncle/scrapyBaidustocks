# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test01.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_parent(object):
    def setupUi(self, parent):
        parent.setObjectName("parent")
        parent.resize(728, 615)
        self.pushButton = QtWidgets.QPushButton(parent)
        self.pushButton.setGeometry(QtCore.QRect(230, 370, 241, 141))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(parent)
        self.pushButton.toggled['bool'].connect(parent.close)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        _translate = QtCore.QCoreApplication.translate
        parent.setWindowTitle(_translate("parent", "Form"))
        self.pushButton.setText(_translate("parent", "PushButton"))


if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    widget=QtWidgets.QWidget()  
    ui=Ui_parent()  
    ui.setupUi(widget)  
    widget.show()  
    sys.exit(app.exec_())  
