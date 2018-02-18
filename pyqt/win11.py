# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QWidget, QApplication
# import sys
# class Ico(QWidget):
    # def __init__(self):
        # super().__init__()
        # self.initUI()
        
    # def initUI(self):
        # self.setGeometry(100,200,300,400)
        # self.setWindowTitle('小信风')
        # self.setWindowIcon(QIcon('dog.ico'))
        # self.show()
        
        
# if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # w = Ico()
    # sys.exit(app.exec_())
    
    
#!/usr/bin/python3
#coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Ico(QWidget):

   def __init__(self):
       super().__init__()
       self.initUI()    

   def initUI(self):

       self.setGeometry(300, 300, 300, 220)
       self.setWindowTitle('学点编程吧出品')
       self.setWindowIcon(QIcon("D:\pyqt\dog.ico"))
    #    self.setWindowIcon(QIcon("dog.ico"))
       self.show()
 
 
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())





















