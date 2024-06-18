import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from startstop_gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #Khoi tao nut start va khi an nut start se thuc thi 1 phuong thuc
        self.uic.start_button.clicked.connect(self.showscreen)
        #Khoi tao nut stop va khi an se tat giao dien => sd giao dien
        self.uic.stop_button.clicked.connect(self.main_win.close)
    def showscreen(self):# Vi lam cho phan thiet ke => sd giao dien tu tao
        self.uic.label.setText('Chao ban!')
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())