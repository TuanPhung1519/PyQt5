import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow
from PyQt5.QtCore import QTimer
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self dung 1 minh la self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)#Truyen self.main_ui
        #Khoi tao nut nhan
        self.uic.pushButton.clicked.connect(self.start)

    def start(self):
        timer = QTimer(self)
        timer.timeout.connect(self.loop)
        timer.start(1000)  # 1s
    def loop(self):#Can tao while loop run lien tuc => nhung dung while loop mat time => QTimer
        print('run')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())