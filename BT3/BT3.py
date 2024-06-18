import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()#Chay window khi chua co gi
        self.uic = Ui_MainWindow()#Chay cac cau hinh ma ta thiet ke
        self.uic.setupUi(self.main_ui)#Day cac cau hinh len man hinh
        #Khoi tao nut bam ket noi toi tung trang
        self.uic.s1.clicked.connect(self.showp1)
        self.uic.s2.clicked.connect(self.showp2)
        self.uic.s3.clicked.connect(self.showp3)
        #Khoi tao nut nhan show
        self.uic.show_button.clicked.connect(self.showtext)
    def show(self):
        self.main_ui.show()

    def showp1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page)
    def showp2(self):
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
    def showp3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_3)
    def showtext(self):
        self.uic.textEdit.setText('Hello!')

if __name__ == '__main__':
    #Load giao dien
    app = QApplication(sys.argv)
    #Gan giao dien vua tao cho 1 bien
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
