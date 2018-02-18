# from PyQt5 import QtWidgets  
# from PyQt第一个成功的窗口 import Ui_tax_rate  
  
# class mywindow(QtWidgets.QWidget):  
#     def __init__(self):  
#         super(mywindow,self).__init__()  
#         self.new=Ui_tax_rate()  
#         self.new.setupUi(self)  
  
# if __name__=="__main__":  
#     import sys  
  
#     app=QtWidgets.QApplication(sys.argv)  
#     myshow=mywindow()  
#     myshow.show()  
#     sys.exit(app.exec_())  

# from PyQt5 import QtWidgets  
# from untitled import Ui_Form  
  


# Third solution:

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent=parent)
#         self.setupUi(self)
# class mywindow(QtWidgets.QWidget,Ui_tax_rate):  
#     def __init__(self):  
#         super(mywindow,self).__init__()  
#         self.setupUi(self)  
  
# if __name__=="__main__":  
#     import sys  
  
#     app=QtWidgets.QApplication(sys.argv)  
#     myshow=mywindow()  
#     myshow.show()  
#     sys.exit(app.exec_())  


from PyQt5 import QtWidgets  
from untitled import Ui_Form  
  
class mywindow(QtWidgets.QWidget):   # 创建一个窗口类  该类的父类是QtWidgets.QWidget
    def __init__(self):             # 定义一个初始化方法
        super(mywindow,self).__init__()  
        self.new=Ui_Form()  
        self.new.setupUi(self)  
  
if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_())  
