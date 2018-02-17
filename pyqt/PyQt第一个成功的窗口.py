# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tax_rate(object):
    def setupUi(self, tax_rate):
        tax_rate.setObjectName("tax_rate")
        tax_rate.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(tax_rate)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(240, 80, 421, 71))
        self.price_box.setObjectName("price_box")
        self.Price = QtWidgets.QLabel(self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(60, 80, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Price.setFont(font)
        self.Price.setObjectName("Price")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(200, 300, 211, 101))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 300, 121, 81))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 200, 89, 51))
        self.radioButton.setObjectName("radioButton")
#         Form = QtGui.QWidget()这行换成 Form = QtGui.QMainWindow()
# 因为你在pyqt中创建的是MainWindow，不是Widget或者dialog
        tax_rate.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tax_rate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menumenu = QtWidgets.QMenu(self.menubar)
        self.menumenu.setObjectName("menumenu")
        tax_rate.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tax_rate)
        self.statusbar.setObjectName("statusbar")
        tax_rate.setStatusBar(self.statusbar)
        self.menumenu.addSeparator()
        self.menumenu.addSeparator()
        self.menumenu.addSeparator()
        self.menubar.addAction(self.menumenu.menuAction())

        self.retranslateUi(tax_rate)
        QtCore.QMetaObject.connectSlotsByName(tax_rate)

    def retranslateUi(self, tax_rate):
        _translate = QtCore.QCoreApplication.translate
        tax_rate.setWindowTitle(_translate("tax_rate", "MainWindow"))
        self.Price.setText(_translate("tax_rate", "<html><head/><body><p align=\"center\"><span style=\" color:#ff55ff;\">Price:</span></p></body></html>"))
        self.pushButton.setText(_translate("tax_rate", "PushButton"))
        self.radioButton.setText(_translate("tax_rate", "RadioButton"))
        self.menumenu.setTitle(_translate("tax_rate", "menu"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     widget = QtWidgets.QWidget(None)
#     Ui_tax_rate().setupUi(widget)
#     sys.exit(app.exec_())
#     pass
# Form = QtGui.QWidget()这行换成 Form = QtGui.QMainWindow()
# 因为你在pyqt中创建的是MainWindow，不是Widget或者dialog
if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    widget=QtWidgets.QMainWindow()  
    ui=Ui_tax_rate()  
    ui.setupUi(widget)  
    widget.show()  
    sys.exit(app.exec_())  
