import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

import time
from PyQt5.QtCore import pyqtSignal, QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khai bao nut nhan
        self.uic.start1_button.clicked.connect(self.start_work1)
        self.uic.start2_button.clicked.connect(self.start_work2)
        self.uic.stop1_button.clicked.connect(self.stop_work1)
        self.uic.stop2_button.clicked.connect(self.stop_work2)

        #Khai bao 1 bien de luu cac thread
        self.thread = {}#Thuoc tinh chua cac thread

    def start_work1(self):
        self.thread[1] = ThreadClass(index=1)
        self.thread[1].signal.connect(self.lcd_dis)
        self.thread[1].start()
        #Tat nut start va bat nut stop
        self.uic.start1_button.setEnabled(False)
        self.uic.stop1_button.setEnabled(True)
    def stop_work1(self):
        # Bat nut start va tat nut stop
        self.uic.start1_button.setEnabled(True)
        self.uic.stop1_button.setEnabled(False)
        self.thread[1].stop()
    def start_work2(self):
        self.thread[2] = ThreadClass(index=2)
        self.thread[2].signal.connect(self.lcd_dis)
        self.thread[2].start()
        # Tat nut start va bat nut stop
        self.uic.start2_button.setEnabled(False)
        self.uic.stop2_button.setEnabled(True)
    def stop_work2(self):
        # Tat nut start va bat nut stop
        self.uic.start2_button.setEnabled(True)
        self.uic.stop2_button.setEnabled(False)
        self.thread[2].stop()

    #Tao ham ket noi de hien thi so len man hinh
    def lcd_dis(self, counter):
        m = counter
        i = self.sender().index
        if i == 1:
            self.uic.lcdNumber_1.display(m)
        if i == 2:
            self.uic.lcdNumber_2.display(m)


class ThreadClass(QThread):
    signal = pyqtSignal(int)
    def __init__(self, index=0):
        super().__init__()
        self.index = index

    def run(self):#Thiet ke ham chay cho thread
        global counter
        counter = 0
        while True:
            counter += 1
            self.signal.emit(counter)
            time.sleep(0.1)
            if counter == 5:
                counter = 0


    def stop(self):
        print("Stop Thread: ", self.index)
        self.terminate()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())