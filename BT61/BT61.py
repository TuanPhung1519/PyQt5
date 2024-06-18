import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
import time
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        #Khoi tao nut nhan
        self.uic.start_button.clicked.connect(self.start_thread)
        self.uic.stop_button.clicked.connect(self.stop_thread)
        #Khoi tao bien quan ly thread
        self.thread = {}
        #Khoi tao khi chia dien thi so thread mac dinh =0
        self.number_thread = 0
        #Set kich thuoc cho cac cot cua bang
        self.uic.tableWidget.setColumnWidth(0, 100)
        self.uic.tableWidget.setColumnWidth(0, 150)
        self.uic.tableWidget.setColumnWidth(0, 170)
        #Tao 1 mang luu cac thread da duoc stop
        self.store_stopthread = []

    def start_thread(self):
        #Lay so thread lineEdit
        self.number_thread = int(self.uic.lineEdit.text())
        for i in range(self.number_thread):
            self.thread[i] = Thread_Class(index=i)
            self.thread[i].signal.connect(self.receive_data)
            self.thread[i].signal_stopthread.connect(self.receive_stopthread)
            self.thread[i].start()

    def receive_data(self, data):
        self.uic.tableWidget.setRowCount(self.number_thread)
        self.uic.tableWidget.setItem(data[2], 0, QTableWidgetItem(str(data[0])))
        self.uic.tableWidget.setItem(data[2], 1, QTableWidgetItem(data[1]))
        self.uic.tableWidget.setItem(data[2], 2, QTableWidgetItem("Thread: " + str(data[2])))
    #Khi tat ca cac thread deu stop thi ta bat dau lap lai
    def receive_stopthread(self, index):
        self.store_stopthread.append(index)
        if len(self.store_stopthread) == self.number_thread:
            self.start_thread()
            self.store_stopthread = []

    def stop_thread(self):
        for i in range(self.number_thread):
            self.thread[i].stop()



class Thread_Class(QThread):
    signal = pyqtSignal(object)
    #Tao 1 signal khac de truyen index
    signal_stopthread = pyqtSignal(object)
    def __init__(self, index=0):
        super().__init__()
        self.index = index
        print("Start Thread ", self.index)
    def run(self):
        # Bat dau dem tu gia tri ban dau khac nhau
        self.init_count = randint(0, 5)
        self.status = "start"
        for self.i in range(self.init_count, 10):
            data = [self.i, self.status, self.index]
            self.signal.emit(data)
            time.sleep(1)
        self.status = "stop"
        data = [self.i, self.status, self.index]
        self.signal_stopthread.emit(self.index)
        self.signal.emit(data)

    def stop(self):
        print("Stop Thread ", self.index)
        self.status = "stop"
        data = [self.i, self.status, self.index]
        self.signal.emit(data)
        self.terminate()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec_())