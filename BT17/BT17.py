#Trong cac BT16 ta nhan thay khi run while neu ta an dau "X" tren win
#=> Se tat duoc man hinh nhung van run ra Blink!
#=> Ly do: La vi trong class MainWindow ta khong sd ham ke thua va truyen QMainWindow(chua cac thao tac tren win)
#=> Dan den cac thao tac tren win khong co tac dung
#=> Trong BT17 ta se sd ham ke thua
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow

import time
import threading

class MainWindow(QMainWindow):#Ta se tao 1 win nhung ke thua tu cai ta ve trong designer
    def __init__(self):
        super().__init__()
        #Vi ke thua tu QMainWindow => khong can goi main_ui
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.start_button.clicked.connect(self.start)

    #Vi khong con self.main_ui => khong can tao ham show
    def start(self):
        global status
        status = True
        self.blink()
    #Ham nay cua pyqt5 sinh ra cho viec nhan su kien nut "X" tren window
    def closeEvent(self, event):
        global status
        status = False
    def blink(self):
        def run():
            while status == True:
                print('Blink!')
                time.sleep(0.1)
        thread1 = threading.Thread(target=run)
        thread1.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())
