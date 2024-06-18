import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Qtui import Ui_MainWindow

class MainWindow:#Khoi tao class ke thua giao dien da thiet ke va cua so chua co gi=> Khi goi MainWindow thi se vao init khoi tao het cai ben trong
    def __init__(self):
        self.main_ui = QMainWindow()#Khoi tao 1 thuoc tinh ke thua window khi khoi dong
        self.uic = Ui_MainWindow()#Khoi tao 1 thuoc tinh ke thua giao dien thiet ke khi khoi dong
        self.uic.setupUi(self.main_ui)#Day cac cau hinh vao cho window
        #Khoi tao nut show
        self.uic.s1.clicked.connect(self.show_1)
        self.uic.s2.clicked.connect(self.show_2)
        self.uic.s3.clicked.connect(self.show_3)

        #Khoi tao nut show text
        self.uic.show_button.clicked.connect(self.showtext)

    def show_1(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab)
    def show_2(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_2)
    def show_3(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_3)
    def showtext(self):
        self.uic.textEdit.setText('Hello!')
    def show(self):
        self.main_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)#Load giao dien
    #Khoi tao giao dien man hinh sau khi thiet ke
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
