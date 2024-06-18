import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow

#Vi chi co 1 thread => ban dau danh cho su kien start => Sau do danh toan bo time cho while
#Vi dieu kien luon dung nen thread do luon chay while va vi vay cac su kien khac khong tham chieu vao duoc
#Vi la su kien chu khong phai la nam trong 1 loop nen no chi chay qua khi co su kien => ma lai luon chay while
#=> khong chay cac su kien kia => Danh rieng 1 thread cho while va 1 thread cho cac su kien kia
import threading
import time
class MainWindow:
    def __init__(self):
        self.main_ui = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_ui)
        #Khai bao cac nut nhan
        self.uic.start_button.clicked.connect(self.start)
        self.uic.stop_button.clicked.connect(self.stop)
    def start(self):
        global status
        status = True
        self.blink()

    def stop(self):
        global status
        status = False
        self.blink()

    def blink(self):
        def run():#Ham nay thuc thi chay lien tuc string "Blink" khi an start va khi an stop se dung
            while status == True:
                print('Blink!')
                time.sleep(0.1)#second

        thread1 = threading.Thread(target=run)
        thread1.start()



    def show(self):
        self.main_ui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())