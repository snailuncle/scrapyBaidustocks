
# 5
#coding:utf-8
 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)
 
class SigSlot(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)   # 基类的__init__方法
        self.setWindowTitle('XXOO') # 设置窗口标题
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal,self)
        lcd2 = QLCDNumber(self)
        slider2 = QSlider(Qt.Horizontal,self)         
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        vbox.addWidget(lcd2)
        vbox.addWidget(slider2)
         
        self.setLayout(vbox)
         
        slider.valueChanged.connect(lcd.display)
        slider2.valueChanged.connect(lcd2.display)
        self.resize(350,250)
print(type(sys.argv))

print(sys.argv)  
app = QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())
