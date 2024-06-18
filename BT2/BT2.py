import sys
from PyQt5.QtWidgets import QApplication, QMainWindow # Load 2 class de load giao dien len va chay man hinh khi chua co gi
from copy_ui import Ui_MainWindow #Chay man hinh khi da dc thiet ke

class MainWindow: #Tao 1 class ke thua 2 giao dien chua co gi va da duoc thiet ke
    def __init__(self): #Khi run nhay va day chay 2 giao dien tren
        self.main_win = QMainWindow()#Tao thuoc tinh de load giao dien chua co gi
        self.uic = Ui_MainWindow()#Tao thuoc tinh run giao dien da thiet ke
        self.uic.setupUi(self.main_win) #Chay cac cau hinh bang viecj truyen man hinh chua co gi vao
        self.uic.start_button.clicked.connect(self.show_data)#Khoi tao nut nhan start khi an chay show ra data o dong 1
        self.uic.stop_button.clicked.connect(self.main_win.close)
        #Khoi tao nut nhan copy
        self.uic.copy_button.clicked.connect(self.copytext)
    def copytext(self):
        data_copy = self.uic.textEdit.toPlainText()#Lay data tu textEdit qua
        #Chuyen data qua man hinh text_copy()
        self.uic.text_copy.setText(data_copy)
    def show(self):
        self.main_win.show()#Show man hinh

    def show_data(self):#Hien thi data mac dinh khi nhan start
        self.uic.textEdit.setText('Hello!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()#Run man hinh sau khi da cau hinh
    main_win.show()
    sys.exit(app.exec_())

