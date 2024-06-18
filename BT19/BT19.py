import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from gui import Ui_MainWindow
#Tao 1 class ke thua QObject

class communicate(QObject):
    trigger = pyqtSignal()

#Khi su dung ham ke thua => bat buoc phai truyen QMainWindow => ta co the truyen cac thuoc tinh lien quan toi QMainWindow vao. con khong thi se khong truyen duoc gi vao
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = communicate()#Khai bao thuoc tinh chua emit
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.showdata)
        self.c.trigger.connect(self.close_list)


    def showdata(self):
        self.uic.listWidget.addItem('Hello!')
        #Boi vi cai nay cu dem tang dan => neu chi so sanh vs 4 thi khong on!
        if self.uic.listWidget.count() % 4 == 0:
            self.c.trigger.emit()
    def close_list(self):
        self.uic.listWidget.close()
        self.uic.label.setText('Hi!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())
